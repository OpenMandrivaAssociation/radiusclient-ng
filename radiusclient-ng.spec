%define	major 2
%define libname %mklibname radiusclient-ng %{major}
%define develname %mklibname %{name} -d

Summary:	Radiusclient library and tools
Name:		radiusclient-ng
Version:	0.5.6
Release:	5
License:	BSD
Group:		System/Servers
URL:		http://developer.berlios.de/projects/radiusclient-ng/
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
%defattr(-,root,root)
%attr(0755,root,root) %{_libdir}/lib*.so.*

%files -n %{develname}
%attr(0755,root,root) %{_libdir}/lib*.so
%attr(0644,root,root) %{_libdir}/lib*.a
%{_includedir}/*


%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.5.6-3mdv2010.0
+ Revision: 433050
- rebuild

* Wed Jul 09 2008 Oden Eriksson <oeriksson@mandriva.com> 0.5.6-2mdv2009.0
+ Revision: 233095
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu Jan 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.6-1mdv2008.1
+ Revision: 160785
- new version
  new devel policy

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Jan 12 2007 Andreas Hasenack <andreas@mandriva.com> 0.5.2-4mdv2007.0
+ Revision: 108007
- rebuild

* Sun Oct 15 2006 Stefan van der Eijk <stefan@mandriva.org> 0.5.2-3mdv2007.1
+ Revision: 65185
- mkrel 3

* Sun Oct 15 2006 Stefan van der Eijk <stefan@mandriva.org> 0.5.2-2mdv2007.1
+ Revision: 64849
- remove redundant deps
- fix deps
- import + make seperate conf package
- Import radiusclient-ng

* Tue Jun 27 2006 Oden Eriksson <oeriksson@mandriva.com> 0.5.2-1mdv2007.0
- 0.5.2
- rediffed P0

* Mon Apr 25 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 0.5.0-1mdk
- initial Mandriva package

* Sat Oct 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.3.2-5mdk
- fix deps

* Sat Oct 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.3.2-4mdk
- rebuild
- misc spec file fixes

