# This is a spec file for redis 
 
%define _topdir     /root/rpmbuild 
%define name        redis
%define release     1.el6
%define version     3.2.11 
%define buildroot   %{_topdir}/%{name}-%{version}
 
BuildRoot:  	%{buildroot}
Summary:        A persistent key-value database 
License:       	BSD 
Name:           %{name}
Version:        %{version}
Release:        %{release}
Source:         %{name}-%{version}.tar.gz
Prefix:         /usr
Group:          Application/Databases
 
%description
Redis is a key-value database. It is similar to memcached but the dataset is not volatile, and values can be strings, exactly like in memcached, but also
lists and sets with atomic operations to push/pop elements.

In order to be very fast but at the same time persistent the whole dataset is taken in memory and from time to time and/or when a number of changes to the
dataset are performed it is written asynchronously on disk. You may lose the last few queries that is acceptable in many applications but it is as fast
as an in memory DB (beta 6 of Redis includes initial support for master-slave replication in order to solve this problem by redundancy).

Compression and other interesting features are a work in progress. Redis is written in ANSI C and works in most POSIX systems like Linux, *BSD, Mac OS X,
and so on. Redis is free software released under the very liberal BSD license.

%prep
%setup -q -n %{name}-%{version}
 
%build
make MALLOC=libc

%install
mkdir -p $RPM_BUILD_ROOT/usr/local/bin/
cp src/redis-server $RPM_BUILD_ROOT/usr/local/bin/
cp src/redis-cli $RPM_BUILD_ROOT/usr/local/bin/
cp src/redis-trib.rb $RPM_BUILD_ROOT/usr/local/bin/

%post

%clean
 
%files
/usr/local/bin

%defattr(-,root,root)
 
