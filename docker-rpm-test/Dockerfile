FROM centos:6
MAINTAINER RPM Builder <eva.li@ehealth.com>

#RUN yum -y install rpm-build

COPY redis-3.2.11-1.el6.x86_64.rpm /root/

RUN rpm -Uvh /root/redis-3.2.11-1.el6.x86_64.rpm

