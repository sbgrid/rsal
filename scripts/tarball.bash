#!/usr/bin/env bash

# create tarball for building staging/prod rpm
if [ -z ${RSAL_VERSION} ]; then
	v=0.1
else
	v=${RSAL_VERSION}
fi

if [ ! -d dist/ ]; then
	mkdir dist
fi

tar zcf dist/rsal-${v}.tar.gz api/*py scn/pub.sh scn/requirements.txt doc/config/* 
