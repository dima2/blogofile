#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
post.py parses post sources from the ./_post directory.
"""

__author__ = "Ryan McGuire (ryan@enigmacurry.com)"
__date__   = "Mon Feb  2 21:21:04 2009"

import os
import sys
import datetime
import re
import operator
import urlparse
import hashlib
import codecs

import pytz
import yaml
import logging
import BeautifulSoup
import tidy
import urllib

import blogofile_bf as bf

from django.utils.encoding import smart_str

logger = logging.getLogger("blogofile.post")
#logger.setLevel(logging.DEBUG)
# hdlr = logging.FileHandler('post.log')
# formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
# hdlr.setFormatter(formatter)
# logger.addHandler(hdlr) 


config = bf.config.controllers.blog.post
config.mod = sys.modules[globals()["__name__"]]

# These are all the Blogofile reserved field names for posts. It is not
# recommended that users re-use any of these field names for purposes other
# than the one stated.
reserved_field_names = {
    "title"      :"A one-line free-form title for the post",
    "tagline"    : "The idea behind the concept is to create a memorable phrase that will sum up the tone and premise of a brand or product (like a film), or to reinforce the audience's memory of a product.",
    "date"       :"The date that the post was originally created",
    "updated"    :"The date that the post was last updated",
    "description":"Short description of post",
    "catags" :"Ctegories + Tags",
    "tags"       :"A list of tags that the post pertains to, "\
        "each seperated by commas",
    "permalink"  :"The full permanent URL for this post. "\
        "Automatically created if not provided",
    "path"       :"The path from the permalink of the post",
    "guid"       :"A unique hash for the post, if not provided it "\
        "is assumed that the permalink is the guid",
    "slug"       :"The title part of the URL for the post, if not "\
        "provided it is automatically generated from the title."\
        "It is not used if permalink does not contain :title",
    "author"     :"The name of the author of the post",
    "filters"    :"The filter chain to apply to the entire post. "\
        "If not specified, a default chain based on the file extension is "\
        "applied. If set to 'None' it disables all filters, even default ones.",
    "filter"     :"synonym for filters",
    "draft"      :"If 'true' or 'True', the post is considered to be only a "\
        "draft and not to be published.",
    "source"     :"Reserved internally",
    "yaml"       :"Reserved internally",
    "content"    :"Reserved internally",
    "filename"   :"Reserved internally",
    "id"   : "Unique id (for legacy wp_post_id support)",
    "disqus_identifier":"disqus_identifier"
    }


class PostParseException(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class Post(object):
    """
    Class to describe a blog post and associated metadata
    """
    def __init__(self, source, filename="Untitled"):
        self.source = source
        self.yaml = None
        self.title = None
        self.tagline = None
        self.__timezone = bf.config.controllers.blog.timezone
        self.date = None
        self.updated = None
        self.catags = set()
        self.permalink = None
        self.content = u""
        self.excerpt = u""
        self.filename = filename
        self.author = ""
        self.guid = None
        self.slug = None
        self.description = ""
        self.draft = False
        self.filters = None
        self.id = None
        self.disqus_identifier=""
        self.__parse()
        self.__post_process()
        
    def __repr__(self): #pragma: no cover
        return u"<Post title='{0}' date='{1}'>".format(
            self.title, self.date.strftime("%Y/%m/%d %H:%M:%S"))
     
    def __parse(self):
        """Parse the yaml and fill fields"""
        yaml_sep = re.compile("^---$", re.MULTILINE)
        content_parts = yaml_sep.split(self.source, maxsplit=2)
        if len(content_parts) < 2:
            raise PostParseException(u"{0}: Post has no YAML section".format(
                    self.filename))
        else:
            #Extract the yaml at the top
            self.__parse_yaml(content_parts[1])
            post_src = content_parts[2]
        self.__apply_filters(post_src)
        #Do post excerpting
        self.__parse_post_excerpting()
        self.content=re.sub(r"<!--more (.*?)-->",r"<span id='more'></span>\1",self.content)
        
        if self.description=="":
            clear_content=re.sub(r"<.*?>", "", self.content).replace("\n","")
            self.description = " ".join(clear_content.split(" ")[:30])
            logger.debug(self.description)

    def __apply_filters(self, post_src):
        """Apply filters to the post"""
        #Apply block level filters (filters on only part of the post)
        # TODO: block level filters on posts
        #Apply post level filters (filters on the entire post)
        #If filter is unspecified, use the default filter based on
        #the file extension:
        if self.filters is None:
            try:
                file_extension = os.path.splitext(self.filename)[-1][1:]
                self.filters = bf.config.controllers.blog.post_default_filters[
                    file_extension]
            except KeyError:
                self.filters = []
        self.content = bf.filter.run_chain(self.filters, post_src)
        
    def __parse_post_excerpting(self):
        if bf.config.controllers.blog.post_excerpts.enabled:
            length = bf.config.controllers.blog.post_excerpts.word_length
            try:
                self.excerpt = bf.config.post_excerpt(self.content, length)
            except AttributeError:
                self.excerpt = self.__excerpt(length)

    def __excerpt(self, num_words=50):
        #Default post excerpting function
        #Can be overridden in _config.py by
        #defining post_excerpt(content,num_words)
        if len(self.excerpt) == 0:
          post_excerpt=self.content
          if post_excerpt.count("<!--more")>0:
            link_text=re.findall(r'<!--more\ (.*)-->',post_excerpt)
            if not link_text:
              link_text="Read more"
            else:
              link_text=link_text[0]
            link='<a  class="more-link" href="%s#more">%s</a>' % (self.permalink,link_text)
            post_excerpt=post_excerpt.split("<!--more")[0]+link
            post_excerpt=str(tidy.parseString(post_excerpt, show_body_only=True)).decode('utf-8')

            #make full links
            post_excerpt=post_excerpt.replace("href='#","href='"+self.permalink+"#")
            post_excerpt=post_excerpt.replace("href=\"#","href=\""+self.permalink+"#")

          return post_excerpt
        
    def __post_process(self):
        # fill in empty default value
        if not self.title:
            self.title = u"Untitled - {0}".format(
                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        self.id=int(self.filename.split("-")[0]) 

        self.disqus_identifier=str(self.id)        
        
        if not self.slug:
            self.slug = re.sub("[ ?]", "-", self.title).lower()

        if not self.date:
            self.date = datetime.datetime.now(pytz.timezone(self.__timezone))
        if not self.updated:
            self.updated = self.date

        if not self.description:
            self.description = self.tagline

        if not self.catags or len(self.catags) == 0:
            self.catags = set([Catag('Uncategorized')])
        if not self.permalink and \
                bf.config.controllers.blog.auto_permalink.enabled:
            self.permalink = bf.config.site.url.rstrip("/") + \
                bf.config.controllers.blog.auto_permalink.path
            self.permalink = \
                    re.sub(":blog_path", bf.config.blog.path, self.permalink)
            self.permalink = \
                    re.sub(":year", self.date.strftime("%Y"), self.permalink)
            self.permalink = \
                    re.sub(":month", self.date.strftime("%m"), self.permalink)
            self.permalink = \
                    re.sub(":day", self.date.strftime("%d"), self.permalink)
            self.permalink = \
                    re.sub(":title", self.slug, self.permalink)

            # TODO: slugification should be abstracted out somewhere reusable
            self.permalink = re.sub(
                    ":filename", re.sub(
                            "[ ?]", "-", self.filename).lower(), self.permalink)

            # Generate sha hash based on title
            self.permalink = re.sub(":uuid", hashlib.sha1(
                    self.title.encode('utf-8')).hexdigest(), self.permalink)

        logger.debug(u"Permalink: {0}".format(self.permalink))
     
    def __parse_yaml(self, yaml_src):
        y = yaml.load(yaml_src)
        # Load all the fields that require special processing first:
        fields_need_processing = ('permalink', 'guid', 'date', 'updated',
                                  'categories', 'tags', 'draft')
        try:
            self.permalink = y['permalink']
            if self.permalink.startswith("/"):
                self.permalink = urlparse.urljoin(bf.config.site.url,
                        self.permalink)
            #Ensure that the permalink is for the same site as bf.config.site.url
            if not self.permalink.startswith(bf.config.site.url):
                raise PostParseException(u"{0}: permalink for a different site"
                        " than configured".format(self.filename))
            logger.debug(u"path from permalink: {0}".format(self.path))
        except KeyError:
            pass
        try:
            self.guid = y['guid']
        except KeyError:
            self.guid = self.permalink
        try:
            self.date = pytz.timezone(self.__timezone).localize(
                datetime.datetime.strptime(y['date'], config.date_format))
        except KeyError:
            pass
        try:
            self.updated = pytz.timezone(self.__timezone).localize(
                datetime.datetime.strptime(y['updated'], config.date_format))
        except KeyError:
            pass
        try:
            self.catags = set([Catag(x.strip(),"category") for x in \
                                       y['categories'].split(",")])
            self.catags.update(set([Catag(x.strip().lower(),"tag") for x in \
                                       y['tags'].split(",")]))

        except:
            pass

        try:
            self.filters = y['filter'] #filter is a synonym for filters
        except KeyError:
            pass
        try:
            if y['draft'] and bf.config.site.url!="http://localhost:8080":
                self.draft = True
                logger.info(u"Post {0} is set to draft, "
                        "ignoring this post".format(self.filename))
            else:
                self.draft = False
        except KeyError:
            self.draft = False
        # Load the rest of the fields that don't need processing:
        for field, value in y.items():
            if field not in fields_need_processing:
                setattr(self,field,value)

    def getCatags(self,type):
        result = []
        for catag in self.catags:
            if catag.type==type:
                result.append(catag)

        return result

    def tags(self):
        return self.getCatags('tag')

    def categories(self):
        return self.getCatags('category')

    def tags_str(self):
        result = ""
        for tag in self.catags:
            if tag.type=='tag':
                result=result+tag.name+","

        return result.rstrip(",")

    def categories_str(self):
        pass
        
    def permapath(self):
        """Get just the path portion of a permalink"""
        return urlparse.urlparse(self.permalink)[2]

    def shortlink(self):
        """Get the short url for a post"""
        return bf.config.site.url+"/p/"+str(self.id)

    def __cmp__(self, other_post):
        "Posts should be comparable by date"
        return cmp(self.date, other_post.date)

    def __eq__(self, other_post):
        return self is other_post

    def __getattr__(self, name):
        if name == "path":
            #Always generate the path from the permalink
            return self.permapath()
        else:
            raise AttributeError, name


class Catag(object):

    def __init__(self, name, type):
        self.name = unicode(name)
        self.type = type
        self.cnt = 0
        self.em = 1.0
        # TODO: consider making url_name and path read-only properties?
        self.url_name = self.name.lower().replace(" ", "-")
        self.path = bf.util.site_path_helper(
                bf.config.controllers.blog.path,
                type,
                self.url_name+".html")

    def __eq__(self, other):
        if self.name == other.name and self.type == other.type:
            return True
        return False

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return self.name
    
    def __cmp__(self, other):
        return cmp(self.name, other.name)


def parse_posts(directory):
    """Retrieve all the posts from the directory specified.

    Returns a list of the posts sorted in reverse by date."""
    posts = []
    post_filename_re = re.compile(
        ".*((\.textile$)|(\.markdown$)|(\.org$)|(\.html$)|(\.txt$)|(\.rst$)|(\.md$))")
    if not os.path.isdir("_posts"):
        logger.warn("This site has no _posts directory.")
        return []
    post_paths = [f.decode("utf-8") for f in bf.util.recursive_file_list(
            directory, post_filename_re) if post_filename_re.match(f)]

    for post_path in post_paths:
        post_fn = os.path.split(post_path)[1]
        logger.debug(u"Parsing post: {0}".format(post_path))
        #IMO codecs.open is broken on Win32.
        #It refuses to open files without replacing newlines with CR+LF
        #reverting to regular open and decode:
        try:
            src = open(post_path, "r").read().decode(
                    bf.config.controllers.blog.post_encoding)
        except:
            logger.exception(u"Error reading post: {0}".format(post_path))
            raise
        try:

            src=src.replace("permalink: "+bf.config.controllers.blog.old_url, "permalink: "+bf.config.controllers.blog.url)

            p = Post(src, filename=post_fn)
        except PostParseException as e:
            logger.warning(u"{0} : Skipping this post.".format(e.value))
            continue
        #Exclude some posts
        if not (p.permalink is None or p.draft is True):
            posts.append(p)
    posts.sort(key=operator.attrgetter('date'), reverse=True)
    return posts
