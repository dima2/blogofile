#!/bin/bash

cd $(dirname "${BASH_SOURCE[0]}")
./build.sh "http://blog.dmi3.net"

cd $(dirname "${BASH_SOURCE[0]}")
HOST="thexnews.com"
USERPASS=$(cat /home/graf/incoming/esk_pass)
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