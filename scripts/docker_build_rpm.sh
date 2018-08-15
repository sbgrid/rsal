#!/bin/sh
if [ -z ${RSAL_VERSION} ]; then
	RSAL_VERSION=0.1
fi

docker run --rm -e RSAL_VERSION=${RSAL_VERSION} -v `pwd`:/build c7build /build/scripts/build_rpm.sh

