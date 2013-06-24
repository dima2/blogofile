<%page args="post"/>

<div id="comments" class="round"><div class="gwtext">

  <%
    from django.utils.encoding import smart_str
    permalink = smart_str(post.permapath())
    if permalink in bf.config.controllers.blog.comments:
      comments = bf.config.controllers.blog.comments[permalink]
    else:
      comments= []
  %>

<div id="disqus_thread">
    <div id="dsq-content">
    <ul id="dsq-comments">
      % for comment in comments:
            <li style="margin-left:${comment['leftShift']*30}px;" class="dsq-comment dsq-clearfix dsq-comment-is-parent"
            data-dsq-comment-id="${comment['id']}" id="dsq-comment-${comment['id']}">
              <div class="dsq-avatar dsq-tt">
                <img alt="" class="" src="${comment['author']['avatar']['permalink']}">
              </div>
              <div class="dsq-comment-body" id="dsq-comment-body-${comment['id']}">
                <div class="dsq-comment-header">
                  <span class="dsq-commenter-name">${comment['author']['name']}</span>
                </div>
                <div id="dsq-comment-message-${comment['id']}" class="dsq-comment-message">
                  <div id="dsq-comment-text-${comment['id']}" class="dsq-comment-text">
                    <p>${comment['message']}</p>
                  </div>
                </div>
              </div>
            </li>

      % endfor
    </ul>
  </div>
  </div>

</div></div>


  <script type="text/javascript">

      var disqus_shortname = '${bf.config.blog.disqus.name}';
      var disqus_identifier = '${post.disqus_identifier}';


      (function() {
          var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
          dsq.src = 'http://' + disqus_shortname + '.disqus.com/embed.js';
          (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
      })();

  </script>
  <noscript>Please enable JavaScript to view the <a href="http://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>










