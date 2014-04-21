#!/bin/bash
cd $(dirname "${BASH_SOURCE[0]}")/blog_features
latest_post_number=$(ls _posts/ -1 | sort -r | grep -o ^[0-9]* -m 1)
post_number=`expr $latest_post_number + 1`

read -p "Post title: $post_number-" post_title
post_path="_posts/$post_number-$post_title.md"

cp _drafts/template.md $post_path
sed -i "s/%title%/$post_title/g" $post_path
date="s/%date%/"$(date +"%Y\/%m\/%d\ %H\:%M\:%S")"/g"
sed -i "$date" $post_path

sublime-text ../../../thexnews.sublime-project $post_path
