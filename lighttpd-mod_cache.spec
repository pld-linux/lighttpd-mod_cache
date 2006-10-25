Summary:	Cache (reverse-proxy) plugin for lighttpd
Name:		lighttpd-mod_cache
Version:	1.0
Release:	0.1
License:	BSD
Group:		Networking/Daemons
URL:		http://www.linux.com.cn/tag/mod-cache
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		%{_prefix}/%{_lib}/lighttpd
%define		_sysconfdir	/etc/lighttpd

%description
Mod-Cache is a cache(reverse-proxy) plugin for lighttpd, which works
like Squid with similar configuration. However mod_cache is faster and
more effective than Squid because it based on powerful Lighttpd.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)