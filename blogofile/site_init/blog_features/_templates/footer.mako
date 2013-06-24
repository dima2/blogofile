<%
from datetime import date
%>

<div id="copyright">
  Powered by <a href="http://blogofile.com/">Blogofile</a> | <a href="http://disqus.com" class="dsq-brlink">Blog comments powered by <span class="logo-disqus">Disqus</span></a> | Design by <a href="http://dmi3.net/">Дима</a><br/>
  Theme inspired by "Ellipse" tool from MS Paint.<br/>
  &copy; копируя, поставьте ссылку.<br/>
  The X News: Season ${date.today().year-2007}<br/>
  <a href="http://thexnews.com/contacts.html">Contacts</a> | <a href="http://thexnews.com/stats">Statistics</a> <br/>
</div>

<script type="text/javascript">
  $.getScript("http://site.yandex.net/load/form/1/form.js");
  $.getScript("http://yandex.st/share/share.js", function(data, textStatus, jqxhr) {
      $(".yashare-auto-init").click(function() {
          var url = $(this).attr('data-yashareLink');
          var post_id = url.substring(url.lastIndexOf('/') + 1);
          vote(post_id,1,"social");
      });      
    });  
</script>

<!-- Yandex.Metrika counter --><script type="text/javascript">(function (d, w, c) { (w[c] = w[c] || []).push(function() { try { w.yaCounter11742112 = new Ya.Metrika({id:11742112, enableAll: true}); } catch(e) {} }); var n = d.getElementsByTagName("script")[0], s = d.createElement("script"), f = function () { n.parentNode.insertBefore(s, n); }; s.type = "text/javascript"; s.async = true; s.src = (d.location.protocol == "https:" ? "https:" : "http:") + "//mc.yandex.ru/metrika/watch.js"; if (w.opera == "[object Opera]") { d.addEventListener("DOMContentLoaded", f); } else { f(); } })(document, window, "yandex_metrika_callbacks");</script><noscript><div><img src="//mc.yandex.ru/watch/11742112" style="position:absolute; left:-9999px;" alt="" /></div></noscript><!-- /Yandex.Metrika counter -->


