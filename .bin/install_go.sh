#!/bin/bash
go get -u golang.org/x/lint/golint
cd $GOPATH/src/golang.org/x/lint
go install .
