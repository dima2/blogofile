<%inherit file="post.mako" />
<%def name="post_prose(post)">
  ${post.excerpt}
</%def>

<%def name="post_title(post)">
  <h3><a href="${post.permalink}" rel="bookmark">${post.title}</a></h3>
</%def>

<%def name="socials(post)">
  <%include file="socials.mako" args="url=post.shortlink(),title=post.title,clazz='relative'" />
</%def>

<%def name="comment_link(post)">
  <div class="after_post"><a data-disqus-identifier="${post.disqus_identifier}" href="${post.permalink}#disqus_thread">Read and Post Comments</a></div>
</%def>

<%def name="after_post(post)">
</%def>


