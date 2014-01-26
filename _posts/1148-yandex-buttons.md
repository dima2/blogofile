---
categories: Webmaster
date: 2012/07/21 15:25:00
title: Рецепт по правильному использованию кнопок социальных сетей с помощью Yandex.Api 
permalink: http://thexnews.com/кнопки-соцсетей-от-Яндекса.html
tags: paranoya in my head, минимализм, идиотизм, web development, полезные советы, Яндекс, многокода
description: О преимуществах кнопок социальных сетей от Яндекса над всеми другими кнопками.
---

<img class="alignleft size-thumbnail" width="100" height="100" alt="" src="/uploads/yandex-buttons.png" title="Кнопки социальных сетей от Яндекса">Казалось бы, кнопки социальных сетей и так установлены на каждом сайте, потому что сделать это проще простого. Но тут есть несколько хитростей.

Вместо того чтобы ставить каждую кнопку отдельно или использовать [addthis.com][a] (или даже odnaknopka.ru) лучше всего выбрать [Блок «Поделиться» от Yandex][y]. И вот почему:

* **JavaScript и HTML код от Яндекса - минималистичен.** Если вставлять код кнопок по отдельности, или с помощью [addthis.com][a], каждая кнопка будет тянуть тонны бесполезного JavaScript'а, который еще не известно что сделает на вашей странице (уж не ускорит точно).
[caption id="" align="alignright" width="150" caption="Статистика на Яндекс.Метрике"]<a href="/uploads/yandex-buttons-stats.png"><img class="size-thumbnail" src="/uploads/yandex-buttons-stats-150x.png"/></a>[/caption]
* **Новые посты** на вашем блоге с Яндекс кнопками почти мгновенно **попадают в индекс**. Как только Яндекс узнает о новом url на котором установлены кнопки, страница сразу становятся на очередь в индексацию.
* Если у вы пользуетесь [метрикой от Яндекса][m], вас будет доступна **удобная статистика** по нажатию кнопок.
* **Возможна асинхронная загрузка**. Когда какой нибудь из социальных сервисов ляжет, или просто будет заблокирован у конкретного посетителя, то его загрузка будет [тормозить а то и вообще останавливать][h] загрузку *вашего* сайта.
С Яндексом же, вы просто можете отметить места где нужны кнопки элементом div:
$$code(lang=html)
<div class="yashare-auto-init" 
  data-yashareL10n="ru"
  data-yashareType="none"
  data-yashareLink=" < url страницы которую шарим >"
  data-yashareTitle="title"
  data-yashareQuickServices="gplus,twitter,facebook,vkontakte"></div>
$$/code
* а в самом низу страницы, когда все содержание вашего сайта уже будет загружено, вызвать асинхронную загрузку скрипта с помощью jQuery, который заменит вышеупомянутые div'ы на кнопки:
$$code(lang=javascript)
<script>
  $.getScript("http://yandex.st/share/share.js");
</script>
$$/code
* Можно легко повесить свой JavaScript метод на нажатие кнопок:
$$code(lang=javascript)
  <script>
  $.getScript("http://yandex.st/share/share.js", function(data, textStatus, jqxhr) {
      $(".yashare-auto-init").click(function() {
        alert('share button was pressed');
      });      
    });
  </script>
$$/code
* Я использую для личной статистики, например. Ну или сообщение с благодарностью показывать можно, тоже вариант :)
* **Кнопки Яндекса - это один сервис**, который уже потом редиректит на соответствующую соцсеть. Я не хочу сливать свою [статистику посещений][s] сразу Фейсбуку, Контакту, Addthis, да и еще черт знает кому через их партнерские соглашения. А Яндекс и так все про мой блог знает :).

Единственный минус - кнопки маленькие, и в стандартной форме нельзя изменить их внешний вид. <!--more Но это легко исправить :) -->

Изменить внешний вид кнопок можно переопределением CSS:

* Чтобы кнопки располагались в одну строку:
<img src="/uploads/yandex-buttons-row.png">
$$code(lang=css)
.b-share__handle, .b-share-icon {
  padding:2px !important;
}
$$/code

* Чтобы каждая находилась на своей строке:

<img style="float:left" height="100" title="Кнопки социальных сетей от Яндекса" src="/uploads/yandex-buttons.png" alt=""/><div style="float:left; margin-top: -20px;">
$$code(lang=css)
.b-share__handle, .b-share-icon {
  float:none !important;
  display:block !important;
  padding:2px !important;
}
$$/code
</div>
<div style="clear:both"></div>

Устанавливаем размер, и общую [картинку][i], которая содержит внешний вид наших кнопок:
$$code(lang=css)
.b-share-icon {
  background: url("images/1984.png") no-repeat scroll 0 0 transparent !important;
  height: 20px !important;
  width: 62px !important;
}
$$/code

Делаем сдвиг картинки для кнопки каждой соцсети:
$$code(lang=css)
.b-share-icon_gplus {
  background-position: 0 0 !important;
}

.b-share-icon_twitter {
    background-position: 0 -62px !important;
    height:19px !important;
}

.b-share-icon_facebook {
    background-position: 0 -42px !important;
    height:19px !important;
}

.b-share-icon_vkontakte {
    background-position: 0 -20px !important;
}
$$/code

Так вы можете адаптировать внешний вид кнопок под любой дизайн.

[download#32#image]

[a]: http://addthis.com "кнопки социальных сетей google plus twitter facebook vkontakte для сайта"
[s]: http://thexnews.com/stats "Статистика сайта"
[h]: http://habrahabr.ru/post/139895/ "Потеря посетителей из за кнопок vkontakte odnoklassniki"
[y]: http://api.yandex.ru/share/ "Блок «Поделиться» для вашего сайта"
[i]: http://thexnews.com/images/1984.png
[m]: http://metrika.yandex.ru "статистика по социальным сервисам"