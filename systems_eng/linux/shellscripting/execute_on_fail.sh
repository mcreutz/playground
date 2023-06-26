#!/bin/bash -e

function cleanup {
  echo "Removing /tmp/foo"
  rm  -r /tmp/foo
}

trap cleanup EXIT
mkdir /tmp/foo
asdffdsa #Fails
