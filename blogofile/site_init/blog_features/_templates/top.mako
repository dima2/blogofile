
function dw(str) {
  document.write(str);
}

function the_top() {
  dw('<div class="votewidget_skin"><ul>');
  % for post in posts[:7]:
    dw('<li style="font-size:${post['size']}em">');
    dw('<a style="color:#eee" href="${post['url']}">${post['name'].decode('utf-8')}</a>');
    dw('<div class="votescomments">');
    dw('${post['votes']} голосов');
    % if post['comments']>0:
      dw('/ <a href="${post['url']}#comments">${post['comments']} комментов</a>');
    % endif
    dw('</div>');
    dw('</li>');
  % endfor
  dw('</ul></div>');
}

function shuffle(){
  return (Math.round(Math.random())-0.5);
}

function top_images() {
  var items = Array();

  % for post in posts:
    % if post['image']!="":
      var post = new Object();
      post.image='${post['image']}';
      post.url='${post['url']}';
      post.id='${post['id']}';
      post.name='${post['name'].decode('utf-8')}';
      post.desc='${post['desc'].decode('utf-8')}';
      items.push(post);

    % endif
  % endfor
  items.sort(shuffle);

  for (var i=0; i<3; i++) {
    post=items[i];
    dw('<hr class="clear"><a class="attention" href="'+post.url+'"><img src="'+post.image+'"/><span class="title">'+post.name+'</span>'+post.desc+'</a>');
  }

  dw('<div class="clear"></div>'); 
}

