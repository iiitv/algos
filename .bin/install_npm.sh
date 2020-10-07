#!/bin/bash
npm install -g $(grep -vE "^\s*#" npm-requirements.txt  | tr "\n" " ")
