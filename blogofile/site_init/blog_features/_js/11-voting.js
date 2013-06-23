var url = "http://dmi3.net/plusminus/plusminus.php"

function vote(vote_id, amount, action)
{
  hide_buttons(vote_id);
  
  $.ajax({
    url: url+"?target="+vote_id+"&amount="+amount+"&action="+action,
    dataType: 'jsonp'
  }).done(function(msg) {
    $.cookie("vote_"+vote_id, msg.cnt);
    show_result(vote_id, msg.cnt)
  });  
}

function hide_buttons(vote_id) {
  var vote='.vote[vote_id='+vote_id+']';
  var vote_bg=$(vote).children(".vote_bg");  
  vote_bg.fadeOut();
}

function show_result(vote_id, cnt) {
  var vote='.vote[vote_id='+vote_id+']';
  var result=$(vote).children(".vote_result");

  $(result).text(cnt);
  $(result).fadeIn();
}

$(document).ready(function(){

  $(".vote").each(function(el) {
    var vote_id=$(this).attr('vote_id');
    
    if ($.cookie("vote_"+vote_id) != null) {
      hide_buttons(vote_id)
      show_result(vote_id, $.cookie("vote_"+vote_id));
    } else {
      var vote_bg=$(this).children(".vote_bg"); 
      
      $(vote_bg).children('.vote_up').click(function() {
        vote(vote_id, 1, "button");
      });

      $(vote_bg).children('.vote_down').click(function() {
        vote(vote_id, -1, "button");
      });

      $(vote_bg).children('.vote_up').mouseover(function() {
        $(this).parent().css("background-position","0px -63px");
      });
      
      $(vote_bg).children('.vote_down').mouseover(function() {
        $(this).parent().css("background-position","0px -126px");
      });

      $(vote_bg).children('.vote_down, .vote_up').mouseout(function() {
        $(this).parent().css("background-position","0px -0px");
      });      
    }

    $(this).children('.vote_result').click(function() {
      //refresh
      vote(vote_id, 0, "button");
    });   
  });  
});
