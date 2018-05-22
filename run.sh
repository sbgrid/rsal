#!/bin/sh

docker run --rm -it -p 873:873 -p 8889:80 -v `pwd`:/mnt/ r7 bash 
