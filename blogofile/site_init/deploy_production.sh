#!/bin/bash

cd $(dirname "${BASH_SOURCE[0]}")

#updating top
wget http://dmi3.net/plusminus/plusminus.php?supertop -O blogofile/_top.json

#getting new comments from disquss
python comments/get_disqus_comments.py

./build.sh "http://thexnews.com"

cd $(dirname "${BASH_SOURCE[0]}")
HOST=$(cat /home/graf/incoming/ftp_ip) #ip of ftp
USERPASS=$(cat /home/graf/incoming/esk_pass) #user in format user:password
LCD="$(pwd)/blogofile/_site"
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
  -d 'tkn=$(cat /home/graf/incoming/cloudflare_api)' \ #cloudflare api key
  -d 'email=dima@thexnews.com' \
  -d 'z=thexnews.com' \
  -d 'v=1'