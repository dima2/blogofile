#!/bin/bash
cd $(dirname "${BASH_SOURCE[0]}")
./build.sh

pwd
if [ -z "$(pgrep twistd)" ]
then
  echo "Starting twistd server"
  twistd -no web --path=blog_features/_site
fi


