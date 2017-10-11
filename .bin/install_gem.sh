#!/bin/bash
wget https://cache.ruby-lang.org/pub/ruby/2.4/ruby-2.4.2.tar.gz
tar -xf ruby-2.4.2.tar.gz
cd ruby*
./configure
make -j4
sudo make install
ruby -v
cd ..
sudo gem install $(grep -vE "^\s*#" gem-requirements.txt  | tr "\n" " ")
