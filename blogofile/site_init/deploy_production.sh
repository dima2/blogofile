#!/bin/bash

cd $(dirname "${BASH_SOURCE[0]}")

#set users & passwords
. ./profile.sh

#updating top
wget http://dmi3.net/plusminus/plusminus.php?supertop -O blog_features/_top.json

#getting new comments from disquss
python comments/get_disqus_comments.py $blog_disqus_secret_key $blog_disqus_public_key $blog_disqus_forum

./build.sh "http://thexnews.com"

cd $(dirname "${BASH_SOURCE[0]}")
HOST=$blog_ftp_ip
USERPASS=$blog_user_password
LCD="$(pwd)/blog_features/_site"
RCD="/www/blog"
lftp -c "set ftp:list-options -a;
set ftp:ssl-allow off
open ftp://$USERPASS@$HOST; 
lcd $LCD;
cd $RCD;
mirror --reverse \
       --only-newer \
       --delete \
       --ignore-time \
       --use-cache \
       --verbose"

curl https://www.cloudflare.com/api_json.html \
  -d 'a=fpurge_ts' \
  -d "tkn=$blog_cloudflare_api_key" \
  -d 'email=dima@thexnews.com' \
  -d 'z=thexnews.com' \
  -d 'v=1'

if $deploy_content_as_branch ; then
  rm -R $content_branch_dir*
  cp -R blog_features/_posts "$content_branch_dir"  
  cp -R blog_features/_pages "$content_branch_dir"
  cd "$content_branch_dir"
  git add *
  git commit -a -m 'content update' && git push origin content
fi