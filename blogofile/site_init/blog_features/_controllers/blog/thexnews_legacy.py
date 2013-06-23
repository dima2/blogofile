# -*- coding: utf-8 -*-

from blogofile.cache import bf
import urllib
from django.utils.encoding import smart_str

blog = bf.config.controllers.blog


def run():
  do_legacy_stuff()

def disqus_identifier_migration(post):
  if post.id==45 or post.id==324:
      post.disqus_identifier=str(post.id) + ' http://thexnews.com/?page_id=' + str(post.id)
  elif post.id==62:
      post.disqus_identifier='62 http://thexnews.com/trash-box.html'
  elif post.id==62:
      post.disqus_identifier='77 http://thexnews.com/%d0%b2%d0%b8%d0%b4%d0%b5%d0%be-%d0%bd%d0%b0-%d1%81%d1%82%d0%b0%d1%80%d1%8b%d1%85-%d0%ba%d0%be%d0%bc%d0%bf%d0%b0%d1%85.html'
  elif post.id<=172 and post.id>=52:
      post.disqus_identifier=str(post.id) + ' http://thexnews.com' + urllib.pathname2url(smart_str(post.permapath())).lower()
  elif post.id<1146:
      post.disqus_identifier=str(post.id) + ' http://thexnews.com/?p=' + str(post.id)
  else:
      post.disqus_identifier=str(post.id)

def do_legacy_stuff():
  for post in blog.posts+blog.pages:
    disqus_identifier_migration(post)
