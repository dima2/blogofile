# -*- coding: utf-8 -*-

import logging
import re
import json
import blogofile_bf as bf
import os
from django.utils.encoding import smart_str
import ConfigParser


logger=logging.getLogger()

config = {
    'name': "wordpress_legacy",
    'description': "wordpress_legacy",
    'aliases': ['wordpress_legacy']
    }

def full_paths(content):
    url=bf.config.controllers.blog.url
    content=content.replace("src=\"/","src=\""+url)
    content=content.replace("href=\"/","href=\""+url)
    return content

def create_images_legacy(content):
    gid="gallery"+str(len(content)) #galery id for fancybox
    images=re.findall(r'(\[caption id="(.*)" align="(.*)" width="(.*)" caption="(.*)"\](.*?)\[/caption\])',content)
    i=0
    for image in images:
      iid=image[1]
      if iid=="":
        iid="image_"+str(i)
      href=image[5].replace('<a',"<a rel='"+gid+"'")

      html="""
<div id=\"%s\" class=\"wp-caption %s\" style=\"width: %spx\">
<div class=\"wp-image-container\">%s</div>
<p class=\"wp-caption-text\">%s</p>
</div>
      """ % (iid,image[2],image[3],href,image[4])
      content=content.replace(image[0],html)
      i+=1
    return content

def get_option(src,s,default=""):
  opt=re.findall("%s\s*=\s*\"(.*?)\"" % s,src)
  if len(opt)>0:
    return opt[0]
  else:
    return default

def create_images_new(content):
    galId="gallery"+str(len(content)) #galery id for fancybox
    images=re.findall(r'(\[img(.*?)\](.*?)\[/img\])',content)

    i=0
    for image in images:
      imageId="image_"+str(i)
      imageClass = get_option(image[1],"class")
      imageWidth = get_option(image[1],"width",150)
      caption = get_option(image[1],"caption")
      imageName,imageExt = os.path.splitext(image[2])
             

      html="""
<div id=\"%s\" class=\"wp-caption %s\" style=\"width: %spx\">
  <div class=\"wp-image-container\">
    <a rel='%s' href="/uploads/%s%s">
      <img class="size-thumbnail" src="/uploads/%s-%sx%s"/>
    </a>
  </div>
  <p class=\"wp-caption-text\">%s</p>
</div>
      """ % (imageId,imageClass,imageWidth,galId,imageName,imageExt,imageName,imageWidth,imageExt,caption)
      content=content.replace(image[0],html)
      i+=1
    return content

def create_files_new(content):
    files=re.findall(r'(\[download (.*?)\](.*?)\[/download\])',content)

    if len(files)>0:
        for f in files:
          aclass="download-button"          
          html='<a class="%s" title="%s" href="%s">Скачать %s</a>'.decode('utf-8') % (aclass,f[1],f[2],f[1])

          content=content.replace(f[0],html)
                        
    return content

def create_files_legacy(content):
    files=re.findall(r'(\[download#([0-9]*)(.*?)\])',content)

    if len(files)>0:
        f=open('downloads/downloads.json','r')
        downloads=json.loads(f.read())
        f.close()

        for f in files:
          html=""
          for download in downloads:
            if download['id']==f[1]:
              # if f[2]=='#nohits':
              aclass="download-link"
              if f[2]=='#image':
                aclass="download-button"
              
              html='<a class="%s" title="%s" href="%s">Скачать %s</a>'.decode('utf-8') % (aclass,download['title'],bf.config.blog.path+"downloads/"+download['filename'],download['title'])

              content=content.replace("<code>"+f[0]+"</code>",html) #legacy fix
              content=content.replace(f[0],html)
              break
                        
    return content

def special_cases(content):
    content = content.replace("<grey>","<span style='color:#665'>") 
    content = content.replace("</grey>","</span >") 

    files=re.findall(r'(\[github\](.*?)\[/github\])',content)

    if len(files)>0:
        for f in files:
          html='<div class="centered padded"><a class="github_big" href="https://github.com/dima2/%s">Github</a></a>' % (f[1])
          content=content.replace(f[0],html)
                        
    return content


def create_toc(content):
    headers=re.findall(r'(<h([0-9]).*?>(.*?)</h[0-9]>)',content)
    
    toc=None

    tocr=re.findall(r'(\[toc(.*?)\])',content)    
    if len(tocr)>0:
      if tocr[0][1]=="":
        tclass='class="toc toc-right"'
      else:
        tclass=tocr[0][1]

      toc='<div %s><span class="toc-header">Оглавление</span><ul>'.decode('utf-8') % tclass
      
    
    for header in headers:      
      title=header[2]
      lvl=header[1]
      link=''.join(e for e in title if (e.isalnum() or e==" ")).lower().replace(" ","-")
      linkedHeader="<h%s id='%s'>%s</h%s>" % (lvl,link,title,lvl)      
      content=content.replace(header[0],linkedHeader)
      if toc:
        toc+='<li class="toc-level-%s"><a title="%s" href="#%s" rel="bookmark nofollow">%s</a></li>' % (lvl,title,link,title)


    if toc:
      toc+='</ul></div>'
      content=content.replace(tocr[0][0],toc)
                        
    return content

def run(content):
    content=create_images_legacy(content)
    content=create_images_new(content)
    content=create_files_legacy(content)
    content=create_files_new(content)
    content=create_toc(content)
    content=full_paths(content)
    content=special_cases(content)


    content=content.replace(":???:", '<img class="wp-smiley" alt="WTF?" src="/images/icon_confused.png"/>')
    content=content.replace(":evil:", '<img class="wp-smiley" alt=">:)" src="/images/icon_evil.png"/>')

    content=content.replace("[hide]", "(<small><a style='border-bottom: 1px dashed blue; color:blue; padding-bottom:0px;' onClick='$(\"#hidden1\").toggle(400);'>показать</a></small>)<div id='hidden1' style='display:none'>".decode('utf-8'))
    content=content.replace("[/hide]", "</div>")
  
    content=content.replace("[postovoy]", "<div class='postovoy'><b>Постовой:</b><br/>".decode('utf-8'))
    content=content.replace("[/postovoy]", "</div>")
    
    content=content.replace("[warning]", "<div class='warning'><b>ВНИМАНИЕ!</b><div class='warning_text'>".decode('utf-8'))
    content=content.replace("[/warning]", "</div></div>")
  
    content=content.replace("[info]", "<div class='info'><b>Информация</b><div class='info_text'>".decode('utf-8'))
    content=content.replace("[/info]", "</div></div>")

    content=content.replace("[/info]", "</div></div>")


    return content
