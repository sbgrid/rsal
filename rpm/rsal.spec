Name: rsal
Version: %{version}
Release: 0
Summary: repository storage abstraction layer, rsync
Source: rsal-%{version}.tar.gz
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-${version}
License: proprietary
Requires: python34 python-virtualenv rsync lighttpd jq PyYAML python2-pip python34-pip
%description 
repository storage abstraction layer, rsync

%prep
%setup -c -n rsal

%build
# empty - no compile needed

%pre
# empty

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/opt/rsal/
mkdir -p %{buildroot}/etc/rsal

cp -r api %{buildroot}/opt/rsal
cp -r scn %{buildroot}/opt/rsal
mkdir -p %{buildroot}/public/requests
mkdir -p %{buildroot}/public/stage
mkdir -p %{buildroot}/hold/requests
mkdir -p %{buildroot}/hold/stage
cp doc/config/lighttpd.conf %{buildroot}/etc/rsal/lighttpd-conf-rsal
cp doc/config/lighttpd-modules.conf %{buildroot}/etc/rsal/lighttpd-modules-rsal
cp doc/config/rsyncd.conf %{buildroot}/etc/rsal/rsal-rsyncd.conf

%clean

rm -rf %{buildroot}

%files
/etc/rsal/lighttpd-conf-rsal
/etc/rsal/lighttpd-modules-rsal
/etc/rsal/rsal-rsyncd.conf
/opt/rsal/api/*
/opt/rsal/scn/*
/opt/rsal/scn/requirements.txt
%dir %attr(0744,lighttpd,lighttpd) /hold/requests
%dir %attr(0744,lighttpd,lighttpd) /hold/stage
%dir %attr(0744,lighttpd,lighttpd) /public/stage
%dir %attr(0744,root,root) /public/requests
