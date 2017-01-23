#!/bin/sh

# curl arguments for manual calls to `/release` endpoint

d=1
h=http://localhost:8080

curl -H "Content-type:application/json" -i -X POST -d "{\"datasetId\":$d}" $h/release

