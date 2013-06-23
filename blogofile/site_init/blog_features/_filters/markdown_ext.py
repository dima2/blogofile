import markdown
import logging
import re

config = {
    'name': "Markdown_ext",
    'description': "Renders markdown formatted text to HTML",
    'aliases': ['markdown_ext']
    }


#Markdown logging is noisy, pot it down:
logging.getLogger("MARKDOWN").setLevel(logging.ERROR)


def run(content):
  content = re.sub(r"~~(.*?)~~",r"<del>\1</del>", content)

  #one liners
  content = re.sub(r"<gr[a|e]y>(.*?)</gr[a|e]y>",r"<span style='color:#777'>\1</span>", content)

  #multi liners
  content = re.sub(r"<gr[a|e]y>","<div style='color:#777'>",content)
  content = re.sub(r"</gr[a|e]y>","</div>",content)

  content = create_footnotes(content)

  return content


def create_footnotes(content):
  bottoms="<div class='footnotes'><ol>"

  footnote_placheholders=re.findall(r'\[\^(.*)\]:',content)
  footnotes=re.findall(r'\[\^(.*\]:.*)',content)
  
  n = 1
  for placheholder in footnote_placheholders:



    for footnote in footnotes:
    

      if footnote.startswith(placheholder):
        footnote_text = footnote.replace(placheholder+"]:","").replace("</p>","")
        footnote_html = "<a class='footnote' id='fnref:%s' href='#fn:%s' title='%s'>%s</a>" % (placheholder, placheholder, footnote_text, n)
        
        content = content.replace("[^"+footnote,"") #delete footnote
        content = content.replace("[^"+placheholder+"]", footnote_html)
        n = n+1
        
        bottoms = bottoms + "<li id='fn:%s'>%s <a href='#fnref:%s'>&#8617</a></li>" % (placheholder, footnote_text, placheholder)

  if n>1:
    content = content + bottoms + "</ol></div>" 

  return content 
