---
categories: Webmaster
date: 2012/08/05 15:25:00
title: Универсальные кнопки для оценки статей на сайте III
permalink: http://thexnews.com/Универсальные-кнопки-для-оценки-статей-на-сайте.html
tags: минимализм, идиотизм, скачать,web development,python
description: Универсальное и быстрое решение для любого сайта чтобы узнать мнение посетителей о статьях
---
<div class="vote" style="float:left;" vote_id="0">
  <div class="vote_bg">
    <span class="vote_up">&nbsp;</span>
    <span class="vote_down">&nbsp;</span>
  </div>
  <div class="vote_result"></div>
</div>

Как бы не рулили [социальные кнопки][y], моя статистика показывает, что лучшим способом узнать что думают посетители о статье по прежнему являются старые добрые кнопки "за" и "против".

Чтобы проголосовать, посетителю не требуется ровно никаких дополнительных действий - ни думать что написать в комментарии, ни решать достойна ли статья появления в ленте его уютной соцсети. И займёт голосование ровно полсекунды времени. И еще одно преимущество перед социальщиной - возможность проголосовать *против*. Из отрицательной статистики тоже можно сделать множество полезных выводов. 

Чтобы оценки давали больше посетителей, я предлагаю показывать большие [интуитивно понятные :)][6] кнопки, которые легко сразу заметить. (не то что маленькие плюсики как например на [d3][d3] или Хабре). 

Во-общем это работает. По указанным кнопкам по прежнему на [этом блоге][blog] нажимают чаще чем по кнопкам соцсетей.

Я уже выкладывал кнопки для голосования в качестве [плагина для Wordpress][p] Но оно было сделано на основе другого плагина [Vote It Up][v], который делал бешеное количество обращений к базе (что тормозило]), да от самого Wordpress я недавно [отказался][b]. По этому представляю <!--more новое, универсальное и быстрое решение для любого сайта-->

Главная цель нового решения - сделать все максимально просто, а так же минимизировать обращения к базе данных.

Например, не будет обращений к базе при каждой загрузке страницы, поскольку результат показывается только после нажатия кнопки.

На каждый новый голос будет только два обращения к базе, после чего результат будет храниться у пользователя cookies (плюс еще два обращения для обновления результата, если пользователь нажмет на кнопку повторно) 

Для защиты от накруток - валидация происходит на стороне базы. Id поста, IP пользователя, и действие - это уникальный (primary) ключ, то есть такую комбинацию можно записать только один раз.

### Требования
* Данные храняться в базе MySql. Для работы с ними есть скрипт на PHP (мне очень стыдно за php, но в там где у меня этот скрипт крутиться ничего другого нет).
* Требуется JQuery и JQuery.cookie. Необходимые библиотеки можно [подгурузить с Яндекса][e] :)

### Установка

Смотрите **[пример на Github][g]** или

* Выполните в базе комманду:
[code lang='sql']
CREATE TABLE `actions` (
   `target` int(10) unsigned not null,
   `actor` int(10) unsigned not null,
   `action` varchar(10) not null,
   `amount` smallint(3) default '0',
   `comment` varchar(30),
   `action_date` timestamp not null default CURRENT_TIMESTAMP,
   PRIMARY KEY (`target`,`actor`,`action`),
   KEY `target` (`target`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
[/code]
* Введите в скрипт plusminus.php параметры вашей базы `($host, $user, $pass, $database)` и загрузите его на хостинг.
* В файле voting.js укажите url (`var url`) файла plusminus.php
* На места где вы хотите видеть кнопки вставьте следующий код:
[code lang='html']
<div class="vote" vote_id=" < id_поста> ">
  <div class="vote_bg">
    <span class="vote_up"></span>
    <span class="vote_down"></span>
  </div>
  <div class="vote_result"></div>
</div>
[/code] 
* В любом месте страницы вызовите voting.js:
[code lang='javascript']
<script type="text/javascript" src="voting.js"></script>
[/code]

### Использование

* Если вызывать `plusminus.php?stats` с параметром stats он вернёт список самых популярных постов в формате json `{id_поста:количество_глосов}`.
* Если вызывать `plusminus.php?pulse` с параметром pulse будут показаны 10 последних голосов.
<--* Как сгенерировать вижет лучщих постов для [blogofile][b] смотрите [1]() [2]()-->
* Плюс с этим скриптом вам предоставляется универсальная функция:
[code lang='javascript']
vote( < id_объекта >, < оценка >, < действие > );
[/code]
* где:
    * `< id_объекта >` положительный integer
    * `< оценка >` может 1, -1, или 0. за против, или обновить соответственно.
    * `< действие >` строка
* C помощью которой можно считать что угодно.
Например я прикрутил ее к [социальным кнопкам от Яндекса][y], что-бы каждое упонинание в соцсети, считалось за положительный голос:
[code lang='javascript']
<script type="text/javascript">
  $.getScript("http://yandex.st/share/share.js", function(data, textStatus, jqxhr) {
      $(".yashare-auto-init").click(function() {
          var url = $(this).attr('data-yashareLink');
          var post_id = url.substring(url.lastIndexOf('/') + 1);
          vote(post_id,1,"social");
      });      
    });  
</script>
[/code]

[download plusminus c Github]https://github.com/dmi3/plusminus/zipball/master[/download]
[github]plusminus[/github]


[y]: http://thexnews.com/кнопки-соцсетей-от-Яндекса.html ""
[blog]: http://thexnews.com
[6]: http://ru.wikipedia.org/wiki/%D0%93%D0%BB%D0%B0%D0%B4%D0%B8%D0%B0%D1%82%D0%BE%D1%80#.D0.96.D0.B5.D1.81.D1.82_.D0.BF.D0.B0.D0.BB.D1.8C.D1.86.D0.B5.D0.BC
[d3]: http://dirty.ru
[p]: http://thexnews.com/wordpress-%D0%BF%D0%BB%D0%B0%D0%B3%D0%B8%D0%BD-%D0%B4%D0%BB%D1%8F-%D0%B3%D0%BE%D0%BB%D0%BE%D1%81%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F-2.html "плагин для голосования на сайте"
[b]: http://thexnews.com/%D1%81%D1%82%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9-%D0%B1%D0%BB%D0%BE%D0%B3-blogofile.html
[v]: http://wordpress.org/extend/plugins/vote-it-up/ "Wordpress плагин для голосования на сайте"
[g]: https://github.com/dmi3/plusminus/
[e]: https://github.com/dmi3/plusminus/blob/master/example.html
