# -*- coding: utf-8 -*-
import urlparse,urllib
from blogofile.cache import bf
import re
import json
from django.utils.encoding import smart_str
import logging
import os

blog = bf.config.controllers.blog

logger = logging.getLogger("blogofile.comments")

def get_comments():
  if not os.path.isfile('../threads.json'):
    logger.error('No coments file found! Please run get_disqus_comments.py')
    return []

  f=open('../threads.json','r')
  source=json.loads(f.read())
  f.close() 

  posts=source['threads'].items()

  readyPosts={}
  for post,comments  in posts:
      readyComments=[]
      for key in sorted(comments.keys()):
        comment=comments[key]
        comment['leftShift']=0

        if comment['parent']!=None:
          pos=0
          for c in readyComments:
            pos+=1            
            if str(c['id'])==str(comment['parent']):
              comment['leftShift']=c['leftShift']+1
              break
            
          readyComments.insert(pos,comment)
        else:
          readyComments.append(comment)



      post2 = urllib.unquote(smart_str(post))
      readyPosts[post2]=readyComments

  return readyPosts