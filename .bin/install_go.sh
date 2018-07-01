#!/bin/bash
mkdir -p $GOPATH/src/golang.org/golang/lint \
  && git clone https://github.com/golang/lint.git $GOPATH/src/golang.org/golang/lint \
  && go get -u golang.org/golang/lint
cd $GOPATH/src/github.com/golang/lint
go install .
