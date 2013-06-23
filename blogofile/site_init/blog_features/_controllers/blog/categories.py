# -*- coding: utf-8 -*-

import os
import shutil
import operator
import feed
from blogofile.cache import bf
import logging

blog = bf.config.controllers.blog

logger = logging.getLogger("blogofile.category")


def run():
    write_categories()


def sort_into_categories():
    categories = set()
    for post in blog.posts:
        categories.update(post.catags)
    
    for category in categories:
        category_posts = [post for post in blog.posts
                            if category in post.catags]
        blog.categorized_posts[category] = category_posts
    
    for category, posts in sorted(
        blog.categorized_posts.items(), key=operator.itemgetter(0)):
        blog.all_categories.append((category, len(posts)))

    maxsize=0
    cat={}
    for category in blog.all_categories:
        catsize=category[1] 
        if catsize>maxsize:
            maxsize=catsize
        cat[category[0].name]=cat['size']=catsize       

    for post in blog.posts:
        for tag in post.catags:
            tag.cnt=cat[tag.name]
            tag.em=round(1+cat[tag.name]/4*3/float(maxsize),1)



def write_categories():
    """Write all the blog posts in categories"""
    catpath = bf.util.path_join(blog.path, blog.category_dir, "index.html")
    tagpath = bf.util.path_join(blog.path, "tag", "index.html")

    categories=[]
    tags=[]
    for category in blog.all_categories:

        cat={}
        cat['name']=category[0].name
        cat['path']=category[0].path
        cat['size']=category[1]

        if cat['size']>blog.min_tag_count_for_page:
            if category[0].type=="category":
                categories.append(cat)
            elif category[0].type=="tag":
                tags.append(cat)

            posts=[]
            for post in blog.categorized_posts[category[0]]:
                posts.append({'name':post.title,'path':post.permalink,'desc':post.description,'size':0})


            bf.writer.materialize_template("links.mako", cat['path'], {"title":category[0].name,"links":posts,"cloud":False})
 
    bf.writer.materialize_template("links.mako", catpath, {"title":"Категории".decode('utf-8'),"links":categories,"cloud":True})
    bf.writer.materialize_template("links.mako", tagpath, {"title":"Метки".decode('utf-8'),"links":tags,"cloud":True})
    