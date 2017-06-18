#!/bin/bash
sudo apt-get update
sudo apt-get install -y $(grep -vE "^\s*#" apt-requirements.txt  | tr "\n" " ")
