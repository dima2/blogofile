#!/bin/bash
echo "buildin..."

cd blog_features

#set profile for blogofile
if [ -z "$@" ]; then
  #default
  echo "http://localhost:8080" > _profile
else
  echo $@ > _profile
fi

blogofile build

#compress js
cat _js/*.js | uglifyjs -nc > _site/dirtydeeds.js

#compress css
cat _css/*.css | cssoptimizer -i -o > _site/style.css

if [ ! $(find ./_uploads/* -maxdepth 1| wc -l) -eq 0 ]; then
  #generate thumbnails for *new* pngs
  cd _uploads
  for f in $(find *.png ! -iname "*-300x*" ! -iname "*-150x*")
  do
    #convert "$f" -resize 300x $(basename "$f" .png)-300x.png
    convert "$f" -resize 150x $(basename "$f" .png)-150x.png
  done 
  cd ..

  #optimize *new* pngs
  trimage -f _uploads

  mv _uploads/* uploads/
fi

echo "done."
