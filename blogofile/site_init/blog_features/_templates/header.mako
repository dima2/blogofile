<%page args="random"/>

<script type="text/javascript">
  destoryed();
  whatisyourproblem();
  st();
</script>

<%
  phrases="""Klaatu barada nikto
  Pleased to meet you. Hope you guess my name!
  Oh, brave new world!
  Sorry, but I'm too busy being delicious.
  Sorry, but I'm too busy watching November Rain on loop
  Sorry, but I'm too busy finding first gear in my Giant Robot Car.
  java.lang.NullPointerException
  system compromised itself and should be destroyed_
  n a hiway2l
  57005
  If I Had A Rocket Launcher...
  Blah Blah Blah with the bits of violence
  A tout le monde, à tous mes amis, je vous aime, je dois partir. (Hate french)
  Helvetin Elop!
  Herro, Senior!
  How do you kill that which has no life?
  This monkey gone to heaven.
  Another one bites the dust!
  Hollowed be thy name.
  Dirty deeds done dirt cheap
  Have any tobacco?
  Wherever the problem is, clint eastwood is gonna fix it.
  Episode 2: The Realm of Black Magic. Ancient castles and strange beasts ahead.
  Mother F* snakes on a Mother F* plane!
  The Computer made me do it!"""


  title=bf.config.blog.name.decode('utf-8')
  description=bf.config.blog.description.decode('utf-8')
  url=bf.config.blog.url
  pharses=phrases.split("\n")
  word=pharses[random % len(pharses)].decode('utf-8')
%>

     <img src='${url}images/fancybox_loading.gif'/ style="position:absolute; display:none;">
     <a title="${word}" id="logolink" href="${url}wtf"><span id="logogo"></span></a>
     <h1 id="blog-title" title="${description}"><a href="${url}">${title}</a></h1>
     <div id="description">${description}</div>
     
     <div id="menu">
       <%def name="menu()">
       <div id="b1" class="bt"><a title='${"На главную!".decode("utf-8")}' href="${bf.config.blog.url}">Homes</a></div>
       </%def>
       ${self.menu()}

       <div id="b2" class="bt"><a title="Золотые посты, ага." href="${url}best.html">Best</a></div>
       <div id="b4" class="bt"><a title="О блоге и авторе" href="${url}wtf.html">About</a></div>
       <div id="b3" class="bt"><a title="Как до меня достучатся" href="${url}contacts.html">Contacts</a></div>

       <div id="sb" class="sbt">       
          <div class="yandexform" onclick="return {'bg': '#130f09', 'language': 'ru', 'encoding': '', 'suggest': true, 'tld': 'ru', 'site_suggest': true, 'webopt': false, 'fontsize': 14, 'arrow': false, 'fg': '#000000', 'logo': 'rw', 'websearch': false, 'type': 3}"><form action="${url}search.html" method="get"><input type="hidden" name="searchid" value="1834267"/><input name="text"/><input type="submit" value="Найти"/></form></div>
          ##script defined in footer
       </div>
      </div>

     <div style="clear:left"></div> 

