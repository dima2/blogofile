secret_key="Yw7WCQhl7Oyqn48M8tLPcCnLFNypUU644AThgsxwhF6OTAgpnbjdMY4QJXfiKLij"
public_key="0QSkIqz00VUIuNUGlHTkdtSKq8QpmhVJqCTGoUM49VcETfcOjtYDxO2X4JnFML7y"
forum='blogdimy'
step=100

import time,os
import json
import logging
import datetime
from disqusapi import DisqusAPI
disqus = DisqusAPI(secret_key, public_key)

logging.root.setLevel(logging.DEBUG)

def get_comments(offset):
  cnt=1
  i=0
  comments=[]

  logging.info("Getting comments starting from %s" % (offset))
  while cnt!=0:
    response=disqus.posts.list(forum=forum,offset=offset,limit=step, order='asc')

    cnt=len(response)   
    comments+=response
    offset+=step
    
    i+=1
    logging.info("Step %s: got %s comments" % (i, cnt))
    

  return comments




if os.path.isfile('threads.json'):
  f=open('threads.json','r')
  comments = json.loads(f.read())
  f.close()
else:
  logging.info("No file threads.json found. Creating new file")
  logging.info("(!) Note: disqus limit of 1000 req per hour may apply")
  comments={}
  comments['threads']={}
  comments['id2permalink']={}
  comments['offset']=0


comments_cnt = 0
for comment in get_comments(comments['offset']):
  threadId=comment['thread']
  if not threadId in comments['id2permalink']:
    thread=disqus.forums.listThreads(forum=forum,thread=threadId)[0]
    permalink=thread['permalink'] = "/"+thread['link'].split("/")[-1]
    comments['id2permalink'][threadId]=permalink
    comments['threads'][permalink]={}
  
  threadLink=comments['id2permalink'][threadId]
  thread=comments['threads'][threadLink]
  thread[comment['id']]=comment
  logging.debug(comment['message'])
  
  comments_cnt+=1

logging.info("Got %s new comments" % comments_cnt)
comments['offset']=comments['offset']+comments_cnt

f=open('threads.json','w')
f.write(json.dumps(comments))
f.close()
