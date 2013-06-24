<%inherit file="skeleton.mako" />

<%def name="header()">
  ## using preudo random to avoid header modifications if page was not changed
  <%include file="header.mako" args="random=len(posts[0].content)+1"/>
</%def>

<%def name="menu()">
</%def>

% for post in posts:
  <%include file="post_excerpt.mako" args="post=post" />
% endfor


<div id="pager" class="date">
% if prev_link:
  <div class="aleft">
    <a href="${prev_link}">« Prev</a>
  </div>
% endif

% if next_link:
  <div class="aright">
    <a href="${next_link}">Next »</a>
  </div>
% endif

<div class="paginator" id="paginator1"></div>

<div class="clr2"></div>
<div class="clr"></div>
</div>

<script type="text/javascript">
  pag1 = new Paginator('paginator1', ${pages_total}, 8, ${current_page}, "${bf.config.blog.url}page/");
</script>

<script type="text/javascript">
    var disqus_shortname = '${bf.config.blog.disqus.name}';

    /* * * DON'T EDIT BELOW THIS LINE * * */
    (function () {
        var s = document.createElement('script'); s.async = true;
        s.type = 'text/javascript';
        s.src = 'http://' + disqus_shortname + '.disqus.com/count.js';
        (document.getElementsByTagName('HEAD')[0] || document.getElementsByTagName('BODY')[0]).appendChild(s);
    }());
</script>
