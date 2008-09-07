Name:           goffice         
Version:        0.6.5
Release:        1%{?dist}
Summary:        Goffice support libraries
Group:          System Environment/Libraries
# bug filed upstream about this being GPL v2 only:
# http://bugzilla.gnome.org/show_bug.cgi?id=463248
License:        GPLv2
URL:            http://freshmeat.net/projects/goffice/
Source0:        ftp://ftp.gnome.org/pub/gnome/sources/%{name}/0.6/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  libgsf-gnome-devel     >= 1.13.3
BuildRequires:  libgnomeui-devel       >= 2.0.0
BuildRequires:  intltool gettext
# glib on fedora 8 is too old
%if 0%{?fedora} < 9
BuildRequires:  pcre-devel
%endif

%description
Support libraries for gnome office


%package devel
Summary:        Libraries and include files for goffice
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       libgsf-gnome-devel     >= 1.13.3
Requires:       libgnomeui-devel       >= 2.0.0
Requires:       pkgconfig

%description devel
Development libraries for goffice


%prep
%setup -q


%build
%configure --disable-dependency-tracking
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang goffice-%{version}
rm $RPM_BUILD_ROOT/%{_libdir}/*.la
rm $RPM_BUILD_ROOT/%{_libdir}/%{name}/%{version}/plugins/*/*.la


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%clean
rm -rf $RPM_BUILD_ROOT


%files -f goffice-%{version}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/*.so.*
%{_libdir}/goffice/
%{_datadir}/goffice/
%{_datadir}/pixmaps/goffice/

%files devel
%{_includedir}/libgoffice-0.6/
%{_libdir}/pkgconfig/libgoffice-0.6.pc
%{_libdir}/*.so
%{_datadir}/gtk-doc/html/goffice/


%changelog
* Sun Sep  7 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.6.5-1
- Updated to 0.6.5

* Wed Aug 27 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.6.4-1
- Updated to 0.6.4
- BuildRequires: pcre-devel only on Fedora < 9

* Sat Mar  8 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.6.2-1
- New upstream version 0.6.2

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.6.1-2
- Autorebuild for GCC 4.3

* Fri Jan 25 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.6.1-1
- Jump to upstream version 0.6.1 for new gnumeric
- Notice ABI and API changes!

* Fri Aug  3 2007 Bill Nottingham <notting@redhat.com>
- tweak license tag

* Thu Mar  1 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.2.2-1
- New upstream release 0.2.2
- Fix rpath usage on x86_64

* Mon Aug 28 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.2.1-2
- FE6 Rebuild

* Tue May  2 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.2.1-1
- new upstream version: 0.2.1

* Tue Mar 21 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.2.0-2
- rebuild for new libgsf

* Thu Feb 16 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.2.0-1
- New upstream version
- Remove .la files from plugin dirs
- Add BuildRequires: intltool gettext

* Mon Feb 13 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.1.2-4
- Bump release and rebuild for new gcc4.1 and glibc.
- add %%{?dist} for consistency with my other packages

* Thu Dec  8 2005 Hans de Goede <j.w.r.degoede@hhs.nl> 0.1.2-3
-Switch to core version of libgsf now Core has 1.13 instead of using special
 Extras libgsf113 version.

* Mon Nov 28 2005 Hans de Goede <j.w.r.degoede@hhs.nl> 0.1.2-2
-Make Source0 a full URL
-Better URL tag
-Fix not owning /usr/lib(64)/goffice and /usr/share/goffice

* Fri Nov 25 2005 Hans de Goede <j.w.r.degoede@hhs.nl> 0.1.2-1
-change name to goffice as that is the upstream tarbal name.
-bump to 0.1.2 this is the minimal version supported by gnumeric-1.6
-use extras libgsf113 package since core libgsf is to old
-use locale macros
-don't ship .la files
-remove some redundant (already included in other) (Build)Requires

* Sat Nov 05 2005 Michael Wise <micwise at gmail.com> - 0.0.4-1
- Initial spec file
