#!/bin/bash
cd $(dirname "${BASH_SOURCE[0]}")
./build.sh

cd blog_features
killall blogofile
blogofile serve&
cd -

