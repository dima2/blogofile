<%inherit file="skeleton.mako" />

<%def name="header()">
  ## using preudo random to avoid header modifications if page was not changed
  <%include file="header.mako" args="random=len(post.content)"/>
</%def>

<%def name="head()">
  <%include file="head_ext.mako" args="title=post.title, 
                                 description=post.description, 
                                    keywords=post.tags_str()"/>
</%def>

<%include file="post.mako" args="post=post" />

${self.prev_next()}

<%
  disqus_identifier=str(post.id)+'http://thexnews.com/?p='+str(post.id)
%>

<%include file="comments.mako" args="post=post"/>

<%def name="prev_next()">
  <div class="date">
  %if prev_post:
    <div class="aleft">
      « <a href="${prev_post.permalink}" rel="bookmark">${prev_post.title}</a>
    </div>
  %endif

  %if next_post:
    <div class="aright">
      <a href="${next_post.permalink}" rel="bookmark">${next_post.title}</a> »
    </div>
  %endif  
  <div class="clr2"></div>
  <div class="clr"></div>
  </div>
</%def>
