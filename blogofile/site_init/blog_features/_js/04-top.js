
function dw(str) {
  document.write(str);
}

function the_top() {
  dw('<div class="votewidget_skin"><ul>');
    dw('<li style="font-size:1.2em">');
    dw('<a style="color:#eee" href="http://localhost:8080/софт-для-ubuntu-версия-2.html">Софт для Ubuntu: Версия 2</a>');
    dw('<div class="votescomments">');
    dw('804 голосов');
    dw('</div>');
    dw('</li>');
    dw('<li style="font-size:1.0em">');
    dw('<a style="color:#eee" href="http://localhost:8080/ubuntu-linux-vs-windows-vista.html">Ubuntu Linux vs Windows Vista</a>');
    dw('<div class="votescomments">');
    dw('500 голосов');
    dw('</div>');
    dw('</li>');
    dw('<li style="font-size:0.9em">');
    dw('<a style="color:#eee" href="http://localhost:8080/wordpress-плагин-для-голосования-2.html">Wordpress плагин для голосования 2</a>');
    dw('<div class="votescomments">');
    dw('265 голосов');
    dw('</div>');
    dw('</li>');
    dw('<li style="font-size:0.9em">');
    dw('<a style="color:#eee" href="http://localhost:8080/sansa-clip-rockbox.html">Sansa Clip и альтернативная прошивка RockBox.</a>');
    dw('<div class="votescomments">');
    dw('246 голосов');
    dw('</div>');
    dw('</li>');
    dw('<li style="font-size:0.8em">');
    dw('<a style="color:#eee" href="http://localhost:8080/док-удобная-замена-панели-задач.html">Док - удобная замена панели задач</a>');
    dw('<div class="votescomments">');
    dw('213 голосов');
    dw('</div>');
    dw('</li>');
    dw('<li style="font-size:0.8em">');
    dw('<a style="color:#eee" href="http://localhost:8080/ubuntu-faq.html">Ubuntu FAQ</a>');
    dw('<div class="votescomments">');
    dw('198 голосов');
    dw('</div>');
    dw('</li>');
    dw('<li style="font-size:0.8em">');
    dw('<a style="color:#eee" href="http://localhost:8080/плагины-для-firefox-3.html">Плагины для Firefox 3</a>');
    dw('<div class="votescomments">');
    dw('163 голосов');
    dw('</div>');
    dw('</li>');
  dw('</ul></div>');
}

function shuffle(){
  return (Math.round(Math.random())-0.5);
}

function top_images() {
  var items = Array();

      var post = new Object();
      post.image='uploads/ubuntu-soft-150x109.png';
      post.url='http://localhost:8080/софт-для-ubuntu-версия-2.html';
      post.id='328';
      post.name='Софт для Ubuntu: Версия 2';
      post.desc='\П\о\д\б\о\р\к\а\ \п\р\а\в\и\л\ь\н\о\г\о\ \с\о\ф\т\а\ \д\л\я\ Ubuntu\ Linux\.';
      items.push(post);

      var post = new Object();
      post.image='uploads/vote1-150x63.jpg';
      post.url='http://localhost:8080/wordpress-плагин-для-голосования-2.html';
      post.id='192';
      post.name='Wordpress плагин для голосования 2';
      post.desc='\У\з\н\а\й\т\е\ \к\а\к\ \о\ц\е\н\и\в\а\ю\т\ \в\а\ш\и\ \п\о\с\т\ы\ \ч\и\т\а\т\е\л\и\ \б\л\о\г\а\!';
      items.push(post);

      var post = new Object();
      post.image='http://localhost:8080/uploads/rockdoom.png';
      post.url='http://localhost:8080/sansa-clip-rockbox.html';
      post.id='969';
      post.name='Sansa Clip и альтернативная прошивка RockBox.';
      post.desc='\В\и\д\е\о\ \с\ Doo\м\ \в\ \п\л\е\е\р\е\-\п\р\и\щ\е\п\к\е\.\ 3\ \ц\в\е\т\а\ \и\ \р\а\з\р\е\ш\е\н\и\е\ 128\х64\.';
      items.push(post);

      var post = new Object();
      post.image='uploads/dockbarx2-150x150.png';
      post.url='http://localhost:8080/док-удобная-замена-панели-задач.html';
      post.id='371';
      post.name='Док - удобная замена панели задач';
      post.desc='DockBarX\ \-\ \у\д\о\б\н\ы\й\,\ \б\ы\с\т\р\ы\й\ \и\ \к\о\м\п\а\к\т\н\ы\й\ \д\о\к\ \д\л\я\ Ubuntu\.\ \Л\у\ч\ш\е\ \ч\е\м\ \н\а\ MacOS\ \и\л\и\ Windows\ 7\ \:\)\.';
      items.push(post);

      var post = new Object();
      post.image='uploads/ubuntu-faq-150x150.png';
      post.url='http://localhost:8080/ubuntu-faq.html';
      post.id='186';
      post.name='Ubuntu FAQ';
      post.desc='\Р\е\ш\е\н\и\е\ \н\а\и\б\о\л\е\е\ \ч\а\с\т\ы\х\ \п\о\ \м\о\е\м\у\ \о\п\ы\т\у\ \п\р\о\б\л\е\м\ \с\в\я\з\а\н\н\ы\х\ \с\ Ubuntu\ Linux\.';
      items.push(post);

      var post = new Object();
      post.image='http://localhost:8080/uploads/robots.png';
      post.url='http://localhost:8080/плагины-для-firefox-3.html';
      post.id='172';
      post.name='Плагины для Firefox 3';
      post.desc='\П\о\д\б\о\р\к\а\ \н\е\о\б\х\о\д\и\м\ы\х\ \п\л\а\г\и\н\о\в\ \д\л\я\ \э\т\о\г\о\ \б\р\а\у\з\е\р\а\.\ \П\р\о\в\е\р\ь\т\е\,\ \у\ \в\а\с\ \в\с\е\ \е\с\т\ь\?';
      items.push(post);

      var post = new Object();
      post.image='http://localhost:8080/uploads/yandex-buttons-stats-150x.png';
      post.url='http://localhost:8080/кнопки-соцсетей-от-Яндекса.html';
      post.id='1148';
      post.name='Рецепт по правильному использованию кнопок социальных сетей с помощью Yandex.Api';
      post.desc='\О\ \п\р\е\и\м\у\щ\е\с\т\в\а\х\ \к\н\о\п\о\к\ \с\о\ц\и\а\л\ь\н\ы\х\ \с\е\т\е\й\ \о\т\ \Я\н\д\е\к\с\а\ \н\а\д\ \в\с\е\м\и\ \д\р\у\г\и\м\и\ \к\н\о\п\к\а\м\и\.';
      items.push(post);

      var post = new Object();
      post.image='http://localhost:8080/uploads/cloudflare-ping-150x.png';
      post.url='http://localhost:8080/ускоряем-загрузку-сайта-cloudflare-cdn.html';
      post.id='1154';
      post.name='Ускоряем загрузку сайта с помощью простого и бесплатного CDN от Cloudflare';
      post.desc='\Е\щ\е\ \о\д\и\н\ \п\р\о\с\т\о\й\ \с\п\о\с\о\б\ \с\е\р\ь\е\з\н\о\ \у\с\к\о\р\и\т\ь\ \з\а\г\р\у\з\к\у\ \в\а\ш\е\г\о\ \с\а\й\т\а\ \с\ \п\о\м\о\щ\ь\ю\ \ \и\ \б\е\с\п\л\а\т\н\о\г\о\ CDN\ \о\т\ Cloudflare';
      items.push(post);

      var post = new Object();
      post.image='http://localhost:8080/uploads/fastmail-150x.png';
      post.url='http://localhost:8080/gmail-vs-альтернативы-vs-fastmail.html';
      post.id='1153';
      post.name='Как я ушел с Gmail и стал платить за электронную почту';
      post.desc='';
      items.push(post);

      var post = new Object();
      post.image='http://localhost:8080/uploads/seafile2-150x.png';
      post.url='http://localhost:8080/seafile-лучшая-альтернатива-dropbox.html';
      post.id='1155';
      post.name='Seafile, да это просто праздник какой-то!';
      post.desc='\П\р\а\в\и\л\ь\н\а\я\ \а\л\ь\т\е\р\н\а\т\и\в\а\ Dropbox\ \с\ \в\о\з\м\о\ж\н\о\с\т\ь\ю\ \з\а\п\у\с\к\а\ \н\а\ \с\в\о\е\м\ \с\е\р\в\е\р\е';
      items.push(post);

      var post = new Object();
      post.image='http://localhost:8080/uploads/apple-vs-samsung-300x.jpg';
      post.url='http://localhost:8080/обзор-ubuntu-for-arm-на-samsung-chromebook.html';
      post.id='1152';
      post.name='Обзор Ubuntu for ARM на Samsung Chromebook';
      post.desc='\О\б\з\о\р\ \н\а\ш\у\м\е\в\ш\е\г\о\ Chromebook\ \з\а\ \$249\ \о\т\ Samsung\,\ \к\о\т\о\р\ы\й\ \у\ж\ \о\ч\е\н\ь\ \п\о\х\о\ж\ \н\а\ Macbook\ Air\.\ \П\о\п\ы\т\к\а\ \п\о\с\т\а\в\и\т\ь\ \т\у\д\а\ Ubuntu\ for\ Arm\ \и\ \п\е\р\в\ы\е\ \в\п\е\ч\а\т\л\е\н\и\я\.';
      items.push(post);

  items.sort(shuffle);

  for (var i=0; i<3; i++) {
    post=items[i];
    dw('<hr class="clear"><a class="attention" href="'+post.url+'"><img src="'+post.image+'"/><span class="title">'+post.name+'</span>'+post.desc+'</a>');
  }

  dw('<div class="clear"></div>'); 
}

