#!/bin/bash
cd $(dirname "${BASH_SOURCE[0]}")
./build.sh

cd blogofile
blogofile serve
cd -

