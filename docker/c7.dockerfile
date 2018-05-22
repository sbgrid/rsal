FROM centos:7
RUN yum update; yum install -y epel-release 
RUN yum install -y python36 python-virtualenv rsync lighttpd jq PyYAML
COPY docker/rsyncd.conf /etc/rsyncd.conf
COPY docker/entrypoint.sh /
COPY doc/config/lighttpd-modules.conf /etc/lighttpd/modules.conf
COPY doc//config/lighttpd.conf /etc/lighttpd/lighttpd.conf
RUN mkdir -p /public/FK2 /public/stage ; echo "foo" > /public/FK2/foo.txt ; chown -R lighttpd:lighttpd /public/stage
RUN mkdir -p /opt/rsal/api
COPY api/* /opt/rsal/api/
RUN mkdir /hold/
COPY testdata/ /hold/
EXPOSE 873
EXPOSE 80

