%define	major 2
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Radiusclient library and tools
Name:		radiusclient-ng
Version:	0.5.6
Release:	12
License:	BSD
Group:		System/Servers
Url:		http://developer.berlios.de/projects/radiusclient-ng/
Source0:	http://download.berlios.de/radiusclient-ng/%{name}-%{version}.tar.gz

%description
Radiusclient is a /bin/login replacement which gets called by a getty to log in
a user and to setup the user's login environment. Normal login programs just
check the login name and password which the user entered against the local
password file (/etc/passwd, /etc/shadow). In contrast to that Radiusclient also
uses the RADIUS protocol to authenticate the user.

%package	conf
Summary:	Radiusclient configuration files
Group:		System/Libraries

%description 	conf
Configuration files required for Radiusclient

%package -n	%{libname}
Summary:	Radiusclient library
Group:          System/Libraries
Requires:	%{name}-conf = %{version}

%description -n	%{libname}
Libraries required for Radiusclient

%package -n	%{devname}
Summary:	Header files and development documentation for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname %{name} 2 -d

%description -n	%{devname}
Header files and development documentation for %{name}.

%prep
%setup -q

%build
%configure2_5x \
	--enable-static \
	--enable-shadow \
	--enable-scp

%make

%install
%makeinstall_std

# rename these to prevent file clashes with the old package
cd %{buildroot}%{_sbindir}
for i in *; do mv ${i} ${i}-ng; done
cd -

%files
%doc BUGS CHANGES README* doc/*.html
%attr(0755,root,root) %{_sbindir}/*

%files conf
%dir %{_sysconfdir}/%{name}
%attr(0644,root,root) %config(missingok,noreplace) %verify(not md5 size mtime) %{_sysconfdir}/%{name}/*

%files -n %{libname}
%{_libdir}/libradiusclient-ng.so.%{major}*

%files -n %{devname}
%{_libdir}/libradiusclient-ng.so
%{_libdir}/libradiusclient-ng.a
%{_includedir}/*

