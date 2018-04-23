%global debug_package %{nil}
%global __strip /bin/true

Name:	    wuzei
Version:	%{ver}
Release:	%{rel}%{?dist}
Summary:	HTTP server for ceph

Group:		System Environment/Base
License:	Apache-2.0
URL:		https://github.com/journeymidnight/radoshttpd
Source0:	 %{name}-%{version}-%{rel}.tar.gz
Source1:        wuzei.json
Source2:        whitelist
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	ceph-devel
Requires:	libradosstriper1

%description
A lightweight HTTP server to obtain ceph's striped object. Only
support download. 


%prep
%setup -q -n %{name}-%{version}-%{rel}


%build
make %{?_smp_mflags}



%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

install -d -m 755 %{buildroot}%{_sysconfdir}/wuzei
install -p -D -m 640 %{SOURCE1} %{buildroot}%{_sysconfdir}/wuzei/wuzei.json
install -p -D -m 640 %{SOURCE2} %{buildroot}%{_sysconfdir}/wuzei/whitelist

%clean
rm -rf %{buildroot}

%post
/sbin/chkconfig --add wuzei

%files
%defattr(-,root,root,-)
%{_bindir}/wuzei
%config(noreplace) /etc/wuzei/wuzei.json
%config(noreplace) /etc/wuzei/whitelist
/etc/init.d/wuzei
/etc/logrotate.d/wuzei
%dir /var/run/wuzei/
%dir /var/log/wuzei/
%doc



%changelog

