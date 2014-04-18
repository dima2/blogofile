#!/bin/bash
cd $(dirname "${BASH_SOURCE[0]}")/blog_features
latest_post_number=$(ls _posts/ -1 | sort -r | grep -o ^[0-9]* -m 1)
post_number=`expr $latest_post_number + 1`

read -p "Post title: $post_number-" post_title
post_path="_posts/$post_number-$post_title.md"

cp _drafts/template.md $post_path
gedit $post_path
