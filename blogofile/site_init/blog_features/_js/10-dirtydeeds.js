$.extend({
  parseQuerystring: function(){
    var nvpair = {};
    var qs = window.location.search.replace('?', '');
    var pairs = qs.split('&');
    $.each(pairs, function(i, v){
      var pair = v.split('=');
      nvpair[pair[0]] = pair[1];
    });
    return nvpair;
  }
});

$(document).ready(function(){

  //set correct captions
  $(".wp-caption").each(function(el) {
    var hre=$(this).find(".wp-caption-text").html();    
    $(this).find("a").attr('title', hre);
  });
  
  $(".wp-image-container a").fancybox({
      fitToView:'true',
      loop:'false',
      arrows:'true',
      padding: 10,
      helpers:  {
        title : {
            type : 'inside'
        }
      }
  });
  });

function arise() {
  $.cookie("destroyed", null);
  location.reload();  
}

function destoryed() {
if ($.cookie("destroyed")=="yep") {
  vote(0,1,"destrooooy!");
  $('#megadiv').hide(); 
  $('body').append('<div style="color:#fff;">Блог уничтожен! Мы осознали свои ошибки, и больше так не будем, честное слово. Пожалуйста, <a href="javascript:arise();">верните все как было</a>.</div>');
 }
}

function st() {
  var qs = $.parseQuerystring();
  if (qs['cid']!=undefined) {
    vote(qs['cid'],0,"block");  
  }
}

function whatisyourproblem() {
  if (document.referrer.indexOf("follow")!=-1) {
    $.cookie("megaoptimizator", "aga");
  }
}


function zadrali() {
if ($.cookie("megaoptimizator")=="aga") {
  $('#reply').hide(); 
  $('#respond').hide(); 
  $('#comments').hide();
  $('body').append('<img onclick="$(\'#reply\').show();" src="http://thexnews.com/wp-content/plugins/graff_stuff/icon_confused.png"/>');
 }
}

function destroy() {
  if (confirm('Уничтожить блог?')) {
    $.cookie("destroyed", "yep");
    destoryed();
  }
}

$(document).ready(function() {$('.having_tooltip, .footnote, #blog-title, #logolink, .graf-related,.g_vote,.g_vote2, .twitter, #krisomamont, #krisomamonts, .votewidget_skin a, #menu a, #logogo, .wp-image-669, #likesmile').tooltip({delay: 0, extraClass: "ttipz", showURL:false});});

$(document).ready(function(){
  $(".bt").hover(
  function(){
    $('#sb').css('overflow','hidden');
    $(this).animate({width: "200px"},  { queue:false, duration:500 } );
    $('#sb').animate({width: "40px"}, { queue:false, duration:500 } );
  },

  function(){
    $('#sb').css('overflow','visible');
    $(this).animate({width: "40px"}, { queue:false, duration:500 } );
    $('#sb').animate({width: "200px"}, { queue:false, duration:500 } );
  }
  );
});


function shakeItBaby(el)
{
  var dir="";
  for (i=0; i<8; i++)
  {
    dir = (i % 2 == 0) ? "+" : "-";
    $(el).animate({top: dir+'=20'}, { queue:true, duration:150 } );
  }
}

$(document).ready(function(){
  $('.vote_up').click(function() {
    shakeItBaby(".socials");
  });
});

$(document).ready(function(){
  $('#more').parent().after('<a class="github ozzy-zig-needs-a-gig" href="https://www.digitalocean.com/?refcode=550d5b856a3c"><div class="line1">Быстрый Ubuntu сервер за $5 в месяц</div>    <div class="line3">Для VPN, Proxy, Pandora и необходимого 24/7 софта.</div>  <div class="line2">VPS в Нью Йорке или Амстердаме. Рекомендую.</div></a>');
});



