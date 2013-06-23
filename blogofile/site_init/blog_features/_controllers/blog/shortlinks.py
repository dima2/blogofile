# -*- coding: utf-8 -*-

from blogofile.cache import bf
import os,urllib
from django.utils.encoding import smart_str

blog = bf.config.controllers.blog


def run():
    generate_shortlinks()


def generate_shortlinks():
    if not os.path.exists("_site/p"):
        os.makedirs("_site/p")

    f=open("_site/p/.htaccess","w")
    for post in blog.posts+blog.pages:

      url='http://thexnews.com' + urllib.pathname2url(smart_str(post.permapath())).lower()
      f.write("Redirect 301 /p/%s %s\n" % (post.id,url))
    f.close()
