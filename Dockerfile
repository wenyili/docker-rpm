FROM centos:6
MAINTAINER RPM Builder <eva.li@ehealth.com>

RUN yum -y install rpm-build
RUN yum -y install make
RUN yum -y install gcc 

RUN mkdir -p /root/rpmbuild
COPY rpmbuild /root/rpmbuild

RUN rpmbuild -ba /root/rpmbuild/SPECS/redis.spec

