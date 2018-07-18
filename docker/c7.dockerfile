FROM centos:7
RUN yum update; yum install -y epel-release 
RUN yum install -y python36 python-virtualenv rsync lighttpd jq PyYAML
COPY docker/rsyncd.conf /etc/rsyncd.conf
COPY docker/entrypoint.sh /
COPY doc/config/lighttpd-modules.conf /etc/lighttpd/modules.conf
COPY doc//config/lighttpd.conf /etc/lighttpd/lighttpd.conf
RUN mkdir -p /public/FK2 /public/stage /public/requests ; echo "foo" > /public/FK2/foo.txt ; chown -R lighttpd:lighttpd /public/stage
RUN mkdir -p /opt/rsal/api /opt/rsal/scn
COPY api/* /opt/rsal/api/
COPY scn/* /opt/rsal/scn/
RUN mkdir /hold/
COPY testdata/ /hold/
ARG DV_HOST=http://dv_srv:8080
ARG DV_API_KEY=burrito
ENV DV_HOST ${DV_HOST}
ENV DV_API_KEY ${DV_API_KEY}
EXPOSE 873
EXPOSE 80
HEALTHCHECK CMD curl --fail http://localhost/hw.py || exit 1
CMD ["/entrypoint.sh"]
