#!/bin/bash
sudo gem install $(grep -vE "^\s*#" gem-requirements.txt  | tr "\n" " ")
