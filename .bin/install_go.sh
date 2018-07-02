#!/bin/bash
mkdir -p $GOPATH/src/golang.org/x \
  && git clone https://github.com/golang/lint.git $GOPATH/src/golang.org/x/lint \
  && go get -u golang.org/x/lint/golint
cd $GOPATH/src/golang.org/x/lint
go install .
