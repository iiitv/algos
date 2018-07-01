#!/bin/bash
mkdir -p $GOPATH/src/golang.org/golang \
  && git clone https://github.com/golang/lint.git $GOPATH/src/golang.org/golang/lint \
  && go get -u golang.org/golang/lint/golang
cd $GOPATH/src/github.com/golang/lint
go install .
