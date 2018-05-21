FROM centos:7
RUN yum update; yum install -y epel-release
RUN yum install -y python36 python-virtualenv rsync
COPY rsyncd.conf /etc/rsyncd.conf
COPY entrypoint.sh /
RUN mkdir -p /public/data ; echo "foo" > /public/foo.txt
EXPOSE 873


