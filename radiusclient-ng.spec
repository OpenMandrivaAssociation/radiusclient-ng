%define	major 2
%define libname %mklibname radiusclient-ng %{major}
%define develname %mklibname %{name} -d

Summary:	Radiusclient library and tools
Name:		radiusclient-ng
Version:	0.5.6
Release:	%mkrel 3
License:	BSD
Group:		System/Servers
URL:		http://developer.berlios.de/projects/radiusclient-ng/
Source0:	http://download.berlios.de/radiusclient-ng/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%package -n	%{develname}
Summary:	Header files and development documentation for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel
Obsoletes:	%mklibname %{name} 2 -d

%description -n	%{develname}
Header files and development documentation for %{name}.

%prep

%setup -q

%build
%configure2_5x \
    --enable-shadow \
    --enable-scp

%make

%install
rm -rf %{buildroot}

%makeinstall_std

# rename these to prevent file clashes with the old package
cd %{buildroot}%{_sbindir}
for i in *; do mv ${i} ${i}-ng; done
cd -

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

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

%files -n %{develname}
%defattr(-,root,root)
%attr(0755,root,root) %{_libdir}/lib*.so
%attr(0644,root,root) %{_libdir}/lib*.la
%attr(0644,root,root) %{_libdir}/lib*.a
%{_includedir}/*
