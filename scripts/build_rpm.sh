#!/bin/sh

if [ -z ${RSAL_VERSION} ]; then
	v=0.1
else
	v=${RSAL_VERSION}
fi
echo "RSAL_VERSION=${RSAL_VERSION}"
cp /build/dist/rsal-${v}.tar.gz ~/rpmbuild/SOURCES/
cp /build/rpm/rsal.spec /tmp/
rpmbuild -ba --define "version ${v}" /tmp/rsal.spec
cp ~/rpmbuild/RPMS/noarch/rsal-${v}-0.noarch.rpm /build/dist/
