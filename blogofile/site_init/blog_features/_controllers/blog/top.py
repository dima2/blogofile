# -*- coding: utf-8 -*-

from blogofile.cache import bf
import re
import json
from django.utils.encoding import smart_str
import glob

blog = bf.config.controllers.blog


exclude=['60','108','106','155','358']
include=['1152']

def get_thumbnail(image):
  pattern='/'.join(image.split('/')[3:])
  pattern=pattern.split('.')[0]+'-150*.*'

  files=glob.glob(pattern)
  if len(files)>0:
    return files[0]
  else:
    return image




def run():
  f=open('_top.json','r')
  top_posts=json.loads(f.read().strip("(").strip(") "))
  f.close()

  posts={}
  for post in blog.posts:
    post_id=str(post.id)
    if (top_posts.has_key(post_id) or post_id in include) and not post_id in exclude:
      champ={}
      champ['id']=post_id
      champ['name']=smart_str(post.title)
      if top_posts.has_key(post_id):
        champ['votes']=top_posts[post_id]
      else:
        champ['votes']=0
      if post.permapath() in blog.comments:
        champ['comments']=len(blog.comments[post.permapath()])
      else:
        champ['comments']=0
      champ['url']=post.permalink
      if post.description:
        champ['desc']=smart_str(re.escape(post.description))
      else:
        champ['desc']=""
      images=re.findall(r'<img.*?src="(.*?)".*?/>',post.content)
      if len(images)>0:
        champ['image']=get_thumbnail(images[0])
      else:
        champ['image']="" 

      rating=champ['votes']+champ['comments']

      posts[rating]=champ

  keylist = posts.keys()
  keylist.sort(reverse=True)

  champs=[]
  maxsize=keylist[0]

  for key in keylist:
    post=posts[key]
    post['size']=round(0.7+key/2/float(maxsize),1)
    champs.append(post)

  env = {
    "posts": champs
  }

  path = bf.util.path_join(blog.path, "../_js/04-top.js")
  bf.writer.materialize_template("top.mako", path, env)


