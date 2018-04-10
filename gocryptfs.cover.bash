#!/bin/bash
#
# Compile gocryptfs.test using:
# go test -c -covermode=count -coverpkg=./... -tags testrunmain
#
MYDIR=$(dirname "$0")
exec $MYDIR/gocryptfs.test -test.run "^TestRunMain$" -test.coverprofile=out.cov "$@"
