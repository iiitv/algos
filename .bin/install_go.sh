#!/bin/bash
go get -u github.com/golang/lint/golint
cd $GOPATH/src/github.com/golang/lint
go install .
