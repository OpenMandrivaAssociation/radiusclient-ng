%define	major 2
%define libname %mklibname radiusclient-ng %{major}
#%%define oldlibname %mklibname radius 0

Summary:	Radiusclient library and tools
Name:		radiusclient-ng
Version:	0.5.2
Release:	%mkrel 4
License:	BSD
Group:		System/Servers
URL:		http://developer.berlios.de/projects/radiusclient-ng/
Source0:	http://download.berlios.de/radiusclient-ng/%{name}-%{version}.tar.bz2
Patch0:		radiusclient-ng-0.5.2-DESTDIR.diff
#Obsoletes:	radiusclient-utils
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
Radiusclient is a /bin/login replacement which gets called by a getty
to log in a user and to setup the user's login environment. Normal
login programs just check the login name and password which the user
entered against the local password file (/etc/passwd, /etc/shadow). In
contrast to that Radiusclient also uses the RADIUS protocol to
authenticate the user.

%package	conf
Summary:	Radiusclient configuration files
Group:		System/Libraries

%description 	conf
Configuration files required for Radiusclient

%package -n	%{libname}
Summary:	Radiusclient library
Group:          System/Libraries
Requires:	%{name}-conf = %{version}
#Obsoletes:	%{oldlibname}

%description -n	%{libname}
Libraries required for Radiusclient

%package -n	%{libname}-devel
Summary:	Header files and development documentation for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel lib%{name}-devel
#Obsoletes:	libradius-devel %{oldlibname}-devel

%description -n	%{libname}-devel
Header files and development documentation for %{name}.

%prep

%setup -q
%patch0 -p0

%build
autoreconf

%configure2_5x \
	--enable-shadow \
	--enable-scp

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

# rename these to prevent file clashes with the old package
cd %{buildroot}%{_sbindir}
for i in *; do mv ${i} ${i}-ng; done
cd -

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc BUGS CHANGES README* doc/*.html
%attr(0755,root,root) %{_sbindir}/*

%files conf
%dir %{_sysconfdir}/%{name}
%attr(0644,root,root) %config(missingok,noreplace) %verify(not md5 size mtime) %{_sysconfdir}/%{name}/*

%files -n %{libname}
%defattr(-,root,root)
%attr(0755,root,root) %{_libdir}/lib*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%attr(0755,root,root) %{_libdir}/lib*.so
%attr(0644,root,root) %{_libdir}/lib*.la
%attr(0644,root,root) %{_libdir}/lib*.a
%{_includedir}/*


