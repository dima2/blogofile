<%page args="post"/>

  <div class="date">
    % for cat in post.categories():
      <a title="Views all posts in ${cat.name}" rel="category tag" href='${cat.path}'>${cat.name}</a>
    % endfor
    →
  </div>

  <div class="ptitle">
    ${self.post_title(post)}

    %if post.tagline!=None and post.tagline!="":
      <h4>${post.tagline}</h4>
    %endif
  </div>

<%def name="post_title(post)">
  <h1>${post.title}</h1>
</%def>



<div class="round"><div class="gwtext">
  <div class="storycontent">
    ${self.socials(post)}
    <a name="${post.slug}"></a>
    ${self.post_prose(post)}
  </div>
  <div class="clr"></div>

  ${self.after_post(post)}

  <div class="feedback">
    <div class="aleft">
    Написал
    <a href="http://thexnews.com/wtf" style="color:#777">Дима</a>
        ${post.date.strftime('%d %b %Y')}
    </div>
    <div class="aright">
    <span class="commentlink">
      ${self.comment_link(post)}
    </span>
    </div>
    <div class="clr"></div>
  </div>
</div>
</div>

    <%def name="post_prose(post)">
      ${post.content}
    </%def>

    <%def name="socials(post)">
      <%include file="socials.mako" args="url=post.shortlink(),title=post.title,clazz='fixed'" />
    </%def>

    <%def name="comment_link(post)">
    </%def>

    <%def name="after_post(post)">
      <div class="vote" vote_id="${post.id}">
        Оцените статью
        <div class="vote_bg">
          <span class="vote_up"></span>
          <span class="vote_down"></span>
        </div>
        <div class="vote_result"></div>
      </div>

      <script type="text/javascript">
        top_images();
      </script>
    </%def>

<div class="tags">
  Метки:
  % for tag in post.tags():
    % if tag.cnt>3:
      <a style="font-size:${tag.em}em" title="Views all posts tagged in ${tag}" rel="category tag" href='${tag.path}'>${tag.name}</a>
    % else:
      <a style="font-size:${tag.em}em" rel="category tag">${tag.name}</a>
    % endif
  % endfor
</div>








