#!/usr/bin/env bash

tar -zxf ./dependences/swig-*.tar.gz
cp ./dependences/pcre-*.tar.gz ./swig-*
cd ./swig-*
./Tools/pcre-build.sh
echo 'Install swig...'
./configure
make
make install