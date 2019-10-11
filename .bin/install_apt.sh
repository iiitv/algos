#!/bin/bash

# PPA for latest go
sudo add-apt-repository -y ppa:longsleep/golang-backports

sudo apt-get update
sudo apt-get install -y $(grep -vE "^\s*#" apt-requirements.txt  | tr "\n" " ")
