%define use_enable_final 1
%{?_no_enable_final: %{expand: %%global use_enable_final 0}}

%define compile_apidox 0
%{?_no_apidox: %{expand: %%global compile_apidox 0}}

%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

%define use_enable_pie 1
%{?_no_enable_pie: %{expand: %%global use_enable_pie 0}}

%if %unstable
%define dont_strip 1
%define use_enable_final 0
%endif

%define branch 1
%{?_branch: %{expand: %%global branch 1}}
%define revision 682345

Name: kdelibs4
Summary: K Desktop Environment - Libraries
Version: 3.91
Release: %mkrel 0.%revision.1
Group: Graphical desktop/KDE
License: ARTISTIC BSD GPL_V2 LGPL_V2 QPL_V1.0
BuildRoot: %_tmppath/%name-%version-%release-root
URL: http://www.kde.org
%if %branch
Source0: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdelibs-%version.%revision.tar.bz2
%else
Source0: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdelibs-%version.tar.bz2
%endif
Patch0: kdelibs4-homedir.patch
BuildRequires: kde4-macros
BuildRequires: cmake >= 2.4.5
BuildRequires: qt4-devel >= 4.3.0
BuildRequires: aspell-devel
BuildRequires: hspell-devel
BuildRequires: avahi-compat-libdns_sd-devel 
BuildRequires: avahi-client-devel
BuildRequires: enchant-devel
BuildRequires: libxslt-proc
BuildRequires: libxslt-devel
BuildRequires: libxml2 >= 2.4.11
BuildRequires: openssl-devel
BuildRequires: cups-devel >= 1.2
BuildRequires: pcre-devel
BuildRequires: fam-devel
BuildRequires: bzip2-devel
BuildRequires: libart_lgpl-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libsasl-devel
BuildRequires: libtiff-devel
BuildRequires: libvorbis-devel
BuildRequires: pam-devel
BuildRequires: X11-devel
BuildRequires: libalsa-devel
BuildRequires: libmad-devel
BuildRequires: gdbm-devel
BuildRequires: jasper-devel
BuildRequires:	OpenEXR-devel
BuildRequires: libacl-devel
BuildRequires: krb5-devel
BuildRequires: ungif-devel
BuildRequires: strigi-devel >=  0.5.1
BuildRequires: shared-mime-info
BuildRequires: soprano-devel

%description 
Libraries for the K Desktop Environment.

#------------------------------------------------	

%define libkaudiodevicelist %mklibname kaudiodevicelist 5

%package -n %libkaudiodevicelist
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: 30000000:%{_lib}kdecore5

%description -n %libkaudiodevicelist
KDE 4 core library.

%post -n %libkaudiodevicelist -p /sbin/ldconfig
%postun -n %libkaudiodevicelist -p /sbin/ldconfig

%files -n %libkaudiodevicelist
%defattr(-,root,root)
%_kde_libdir/libkaudiodevicelist.so.*

#------------------------------------------------	

%define libkde3support %mklibname kde3support 5

%package -n %libkde3support
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: 30000000:%{_lib}kdecore5

%description -n %libkde3support
KDE 4 core library.

%post -n %libkde3support -p /sbin/ldconfig
%postun -n %libkde3support -p /sbin/ldconfig

%files -n %libkde3support
%defattr(-,root,root)
%_kde_libdir/libkde3support.so.*

#------------------------------------------------	

%define libkdecore %mklibname kdecore 5

%package -n %libkdecore
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: 30000000:%{_lib}kdecore5

%description -n %libkdecore
KDE 4 core library.

%post -n %libkdecore -p /sbin/ldconfig
%postun -n %libkdecore -p /sbin/ldconfig

%files -n %libkdecore
%defattr(-,root,root)
%_kde_libdir/libkdecore.so.*

#------------------------------------------------	

%define libkdefakes %mklibname kdefakes 5

%package -n %libkdefakes
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: 30000000:%{_lib}kdecore5

%description -n %libkdefakes
KDE 4 core library.

%post -n %libkdefakes -p /sbin/ldconfig
%postun -n %libkdefakes -p /sbin/ldconfig

%files -n %libkdefakes
%defattr(-,root,root)
%_kde_libdir/libkdefakes.so.*

#------------------------------------------------	

%define libkdefx %mklibname kdefx 5

%package -n %libkdefx
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: 30000000:%{_lib}kdecore5

%description -n %libkdefx
KDE 4 core library.

%post -n %libkdefx -p /sbin/ldconfig
%postun -n %libkdefx -p /sbin/ldconfig

%files -n %libkdefx
%defattr(-,root,root)
%_kde_libdir/libkdefx.so.*

#------------------------------------------------	

%define libkdeprint_management %mklibname kdeprint_management 5

%package -n %libkdeprint_management
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: 30000000:%{_lib}kdecore5

%description -n %libkdeprint_management
KDE 4 core library.

%post -n %libkdeprint_management -p /sbin/ldconfig
%postun -n %libkdeprint_management -p /sbin/ldconfig

%files -n %libkdeprint_management
%defattr(-,root,root)
%_kde_libdir/libkdeprint_management.so.*

#------------------------------------------------	

%define libkdeprint %mklibname kdeprint 5

%package -n %libkdeprint
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: 30000000:%{_lib}kdecore5

%description -n %libkdeprint
KDE 4 core library.

%post -n %libkdeprint -p /sbin/ldconfig
%postun -n %libkdeprint -p /sbin/ldconfig

%files -n %libkdeprint
%defattr(-,root,root)
%_kde_libdir/libkdeprint.so.*

#------------------------------------------------	

%define libkdesu %mklibname kdesu 5

%package -n %libkdesu
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: 30000000:%{_lib}kdecore5

%description -n %libkdesu
KDE 4 core library.

%post -n %libkdesu -p /sbin/ldconfig
%postun -n %libkdesu -p /sbin/ldconfig

%files -n %libkdesu
%defattr(-,root,root)
%_kde_libdir/libkdesu.so.*

#------------------------------------------------	

%define libkdeui %mklibname kdeui 5

%package -n %libkdeui
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: 30000000:%{_lib}kdecore5

%description -n %libkdeui
KDE 4 core library.

%post -n %libkdeui -p /sbin/ldconfig
%postun -n %libkdeui -p /sbin/ldconfig

%files -n %libkdeui
%defattr(-,root,root)
%_kde_libdir/libkdeui.so.*

#------------------------------------------------	

%define libkdnssd %mklibname kdnssd 5

%package -n %libkdnssd
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: 30000000:%{_lib}kdecore5

%description -n %libkdnssd
KDE 4 core library.

%post -n %libkdnssd -p /sbin/ldconfig
%postun -n %libkdnssd -p /sbin/ldconfig

%files -n %libkdnssd
%defattr(-,root,root)
%_kde_libdir/libkdnssd.so.*

#------------------------------------------------	

%define libkfile %mklibname kfile 5

%package -n %libkfile
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: 30000000:%{_lib}kdecore5

%description -n %libkfile
KDE 4 core library.

%post -n %libkfile -p /sbin/ldconfig
%postun -n %libkfile -p /sbin/ldconfig

%files -n %libkfile
%defattr(-,root,root)
%_kde_libdir/libkfile.so.*

#------------------------------------------------	

%define libkhtml %mklibname khtml 5

%package -n %libkhtml
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: 30000000:%{_lib}kdecore5

%description -n %libkhtml
KDE 4 core library.

%post -n %libkhtml -p /sbin/ldconfig
%postun -n %libkhtml -p /sbin/ldconfig

%files -n %libkhtml
%defattr(-,root,root)
%_kde_libdir/libkhtml.so.*

#------------------------------------------------	

%define libkimproxy %mklibname kimproxy 5

%package -n %libkimproxy
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: 30000000:%{_lib}kdecore5

%description -n %libkimproxy
KDE 4 core library.

%post -n %libkimproxy -p /sbin/ldconfig
%postun -n %libkimproxy -p /sbin/ldconfig

%files -n %libkimproxy
%defattr(-,root,root)
%_kde_libdir/libkimproxy.so.*

#------------------------------------------------	

%define libkio %mklibname kio 5

%package -n %libkio
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: 30000000:%{_lib}kdecore5

%description -n %libkio
KDE 4 core library.

%post -n %libkio -p /sbin/ldconfig
%postun -n %libkio -p /sbin/ldconfig

%files -n %libkio
%defattr(-,root,root)
%_kde_libdir/libkio.so.*

#------------------------------------------------	

%define libkjsembed %mklibname kjsembed 5

%package -n %libkjsembed
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: 30000000:%{_lib}kdecore5

%description -n %libkjsembed
KDE 4 core library.

%post -n %libkjsembed -p /sbin/ldconfig
%postun -n %libkjsembed -p /sbin/ldconfig

%files -n %libkjsembed
%defattr(-,root,root)
%_kde_libdir/libkjsembed.so.*

#------------------------------------------------	

%define libkjs %mklibname kjs 5

%package -n %libkjs
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: 30000000:%{_lib}kdecore5

%description -n %libkjs
KDE 4 core library.

%post -n %libkjs -p /sbin/ldconfig
%postun -n %libkjs -p /sbin/ldconfig

%files -n %libkjs
%defattr(-,root,root)
%_kde_libdir/libkjs.so.*

#------------------------------------------------	

%define libkmediaplayer %mklibname kmediaplayer 5

%package -n %libkmediaplayer
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: 30000000:%{_lib}kdecore5

%description -n %libkmediaplayer
KDE 4 core library.

%post -n %libkmediaplayer -p /sbin/ldconfig
%postun -n %libkmediaplayer -p /sbin/ldconfig

%files -n %libkmediaplayer
%defattr(-,root,root)
%_kde_libdir/libkmediaplayer.so.*

#------------------------------------------------	

%define libnepomukmiddleware %mklibname nepomuk-middleware 5

%package -n %libnepomukmiddleware
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: 30000000:%{_lib}kdecore5

%description -n %libnepomukmiddleware
KDE 4 core library.

%post -n %libnepomukmiddleware -p /sbin/ldconfig
%postun -n %libnepomukmiddleware -p /sbin/ldconfig

%files -n %libnepomukmiddleware
%defattr(-,root,root)
%_kde_libdir/libnepomuk-middleware.so.*

#------------------------------------------------	

%define libnepomuk %mklibname nepomuk 5

%package -n %libnepomuk
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: 30000000:%{_lib}kdecore5
Obsoletes: %{_lib}knepomuk5
Obsoletes: %{_lib}kmetadata5
Obsoletes: %{_lib}konto5

%description -n %libnepomuk
KDE 4 core library.

%post -n %libnepomuk -p /sbin/ldconfig
%postun -n %libnepomuk -p /sbin/ldconfig

%files -n %libnepomuk
%defattr(-,root,root)
%_kde_libdir/libnepomuk.so.*

#------------------------------------------------	

%define libknewstuff2 %mklibname knewstuff2 5

%package -n %libknewstuff2
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: 30000000:%{_lib}kdecore5

%description -n %libknewstuff2
KDE 4 core library.

%post -n %libknewstuff2 -p /sbin/ldconfig
%postun -n %libknewstuff2 -p /sbin/ldconfig

%files -n %libknewstuff2
%defattr(-,root,root)
%_kde_libdir/libknewstuff2.so.*

#------------------------------------------------	

%define libknotifyconfig %mklibname knotifyconfig 5

%package -n %libknotifyconfig
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: 30000000:%{_lib}kdecore5

%description -n %libknotifyconfig
KDE 4 core library.

%post -n %libknotifyconfig -p /sbin/ldconfig
%postun -n %libknotifyconfig -p /sbin/ldconfig

%files -n %libknotifyconfig
%defattr(-,root,root)
%_kde_libdir/libknotifyconfig.so.*

#------------------------------------------------	

%define libkntlm %mklibname kntlm 5

%package -n %libkntlm
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: 30000000:%{_lib}kdecore5

%description -n %libkntlm
KDE 4 core library.

%post -n %libkntlm -p /sbin/ldconfig
%postun -n %libkntlm -p /sbin/ldconfig

%files -n %libkntlm
%defattr(-,root,root)
%_kde_libdir/libkntlm.so.*

#------------------------------------------------	

%define libkparts %mklibname kparts 5

%package -n %libkparts
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: 30000000:%{_lib}kdecore5

%description -n %libkparts
KDE 4 core library.

%post -n %libkparts -p /sbin/ldconfig
%postun -n %libkparts -p /sbin/ldconfig

%files -n %libkparts
%defattr(-,root,root)
%_kde_libdir/libkparts.so.*

#------------------------------------------------	

%define libkrosscore %mklibname krosscore 5

%package -n %libkrosscore
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: 30000000:%{_lib}kdecore5

%description -n %libkrosscore
KDE 4 core library.

%post -n %libkrosscore -p /sbin/ldconfig
%postun -n %libkrosscore -p /sbin/ldconfig

%files -n %libkrosscore
%defattr(-,root,root)
%_kde_libdir/libkrosscore.so.*

#------------------------------------------------	

%define libkrossui %mklibname krossui 5

%package -n %libkrossui
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: 30000000:%{_lib}kdecore5

%description -n %libkrossui
KDE 4 core library.

%post -n %libkrossui -p /sbin/ldconfig
%postun -n %libkrossui -p /sbin/ldconfig

%files -n %libkrossui
%defattr(-,root,root)
%_kde_libdir/libkrossui.so.*

#------------------------------------------------	

%define libktexteditor %mklibname ktexteditor 5

%package -n %libktexteditor
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: 30000000:%{_lib}kdecore5

%description -n %libktexteditor
KDE 4 core library.

%post -n %libktexteditor -p /sbin/ldconfig
%postun -n %libktexteditor -p /sbin/ldconfig

%files -n %libktexteditor
%defattr(-,root,root)
%_kde_libdir/libktexteditor.so.*

#------------------------------------------------	

%define libkunittest %mklibname kunittest 5

%package -n %libkunittest
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: 30000000:%{_lib}kdecore5

%description -n %libkunittest
KDE 4 core library.

%post -n %libkunittest -p /sbin/ldconfig
%postun -n %libkunittest -p /sbin/ldconfig

%files -n %libkunittest
%defattr(-,root,root)
%_kde_libdir/libkunittest.so.*

#------------------------------------------------

%define libcupsdconf %mklibname cupsdconf 5

%package -n %libcupsdconf
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: 30000000:%{_lib}kdecore5

%description -n %libcupsdconf
KDE 4 core library.

%post -n %libcupsdconf -p /sbin/ldconfig
%postun -n %libcupsdconf -p /sbin/ldconfig

%files -n %libcupsdconf
%defattr(-,root,root)
%_kde_libdir/libcupsdconf.so.*

#------------------------------------------------	

%define libkutils %mklibname kutils 5

%package -n %libkutils
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: 30000000:%{_lib}kdecore5

%description -n %libkutils
KDE 4 core library.

%post -n %libkutils -p /sbin/ldconfig
%postun -n %libkutils -p /sbin/ldconfig

%files -n %libkutils
%defattr(-,root,root)
%_kde_libdir/libkutils.so.*

#------------------------------------------------	

%define libkwalletbackend %mklibname kwalletbackend 5

%package -n %libkwalletbackend
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: 30000000:%{_lib}kdecore5

%description -n %libkwalletbackend
KDE 4 core library.

%post -n %libkwalletbackend -p /sbin/ldconfig
%postun -n %libkwalletbackend -p /sbin/ldconfig

%files -n %libkwalletbackend
%defattr(-,root,root)
%_kde_libdir/libkwalletbackend.so.*

#------------------------------------------------	

%define libphononexperimental %mklibname phononexperimental 5

%package -n %libphononexperimental
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: 30000000:%{_lib}kdecore5

%description -n %libphononexperimental
KDE 4 core library.

%post -n %libphononexperimental -p /sbin/ldconfig
%postun -n %libphononexperimental -p /sbin/ldconfig

%files -n %libphononexperimental
%defattr(-,root,root)
%_kde_libdir/libphononexperimental.so.*

#------------------------------------------------	

%define libphonon %mklibname phonon 5

%package -n %libphonon
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: 30000000:%{_lib}kdecore5

%description -n %libphonon
KDE 4 core library.

%post -n %libphonon -p /sbin/ldconfig
%postun -n %libphonon -p /sbin/ldconfig

%files -n %libphonon
%defattr(-,root,root)
%_kde_libdir/libphonon.so.*

#------------------------------------------------	

%define libsolid %mklibname solid 5

%package -n %libsolid
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: 30000000:%{_lib}kdecore5

%description -n %libsolid
KDE 4 core library.

%post -n %libsolid -p /sbin/ldconfig
%postun -n %libsolid -p /sbin/ldconfig

%files -n %libsolid
%defattr(-,root,root)
%_kde_libdir/libsolid.so.*

#------------------------------------------------	

%define libthreadweaver %mklibname threadweaver 5

%package -n %libthreadweaver
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: 30000000:%{_lib}kdecore5

%description -n %libthreadweaver
KDE 4 core library.

%post -n %libthreadweaver -p /sbin/ldconfig
%postun -n %libthreadweaver -p /sbin/ldconfig

%files -n %libthreadweaver
%defattr(-,root,root)
%_kde_libdir/libthreadweaver.so.*

#--------------------------------------------------------------

%package devel
Group: Development/KDE and Qt
Summary: Header files and documentation for compiling KDE applications
Conflicts: kdelibs4-core < 3.90.2-0.678253 
Requires: kde4-macros
Requires: acl-devel
Requires: qt4-devel >= 4.3.0
Requires: cmake
Requires: soprano-devel
Requires: strigi-devel
Requires: kdelibs4-core = %version
Requires: %libkaudiodevicelist = %version
Requires: %libkde3support = %version
Requires: %libkdecore = %version
Requires: %libkdefakes = %version
Requires: %libkdefx = %version
Requires: %libkdeprint_management = %version
Requires: %libkdeprint = %version
Requires: %libkdesu = %version
Requires: %libkdeui = %version
Requires: %libkdnssd = %version
Requires: %libkfile = %version
Requires: %libkhtml = %version
Requires: %libkimproxy = %version
Requires: %libkio = %version
Requires: %libkjsembed = %version
Requires: %libkjs = %version
Requires: %libkmediaplayer = %version
Requires: %libnepomuk = %version
Requires: %libnepomukmiddleware = %version
Requires: %libknewstuff2 = %version
Requires: %libknotifyconfig = %version
Requires: %libkntlm = %version
Requires: %libkparts = %version
Requires: %libkrosscore = %version
Requires: %libkrossui = %version
Requires: %libktexteditor = %version
Requires: %libkunittest = %version
Requires: %libkutils = %version
Requires: %libkwalletbackend = %version
Requires: %libphononexperimental = %version
Requires: %libphonon = %version
Requires: %libsolid = %version
Requires: %libthreadweaver = %version
Obsoletes: %{_lib}kdecore5-devel

%description devel
This package includes the header files you will need to compile applications 
for KDE. Also included is the KDE API documentation in HTML format for easy 
browsing.

%files devel
%defattr(-,root,root,-)
%_kde_prefix/include/*
%_kde_appsdir/cmake/modules/*
%_kde_datadir/dbus-1/*/*
%_kde_libdir/*.so
#%_kde_libdir/*.a
%_kde_libdir/kde4/plugins/designer
%_kde_bindir/checkXML
%_kde_bindir/kconfig_compiler
%exclude %_kde_libdir/libkdeinit4_*

#--------------------------------------------------------------

%package -n oxygen-icon-theme
Group: Graphical desktop/KDE
Summary: Oxygen icon theme
Provides: kde4-icon-theme

%description -n oxygen-icon-theme
Oxygen KDE 4 icon theme. Complains with FreeDesktop.org naming schema

%files -n oxygen-icon-theme
%defattr(-,root,root,-)
%dir %_kde_iconsdir/oxygen
%_kde_iconsdir/*/index.theme
%_kde_iconsdir/*/*/*/*

#--------------------------------------------------------------

%package core
Group: Graphical desktop/KDE
Summary: KDE 4 system core files
Requires: aspell
Requires: kde4-icon-theme
Obsoletes: kdelibs4-common
Conflicts: kdelibs4-devel < 3.90.2-0.678253 

%description core
KDE 4 system core files.

%files core
%defattr(-,root,root,-)
%_kde_prefix/README.urpmi
%_kde_bindir/*
%_kde_libdir/kde4/*
%_kde_libdir/libkdeinit4_*
%_kde_appsdir/*/*
%_kde_datadir/emoticons/*
%_kde_datadir/config/*
%_kde_datadir/mime/packages/kde.xml
%_kde_datadir/locale/all_languages
%_kde_datadir/kde4/services/*
%_kde_datadir/kde4/servicetypes/*
%_kde_docdir/HTML/en/sonnet
%_kde_configdir/xdg/menus/applications.menu
%_sysconfdir/ld.so.conf.d/kde4.conf
%_kde_docdir/HTML/en/common/*
%exclude %_kde_bindir/checkXML
%exclude %_kde_bindir/kconfig_compiler
%exclude %_kde_appsdir/cmake/modules/*

#--------------------------------------------------------------

%package apidoc
Group: Development/KDE and Qt
Summary: Development documentation for %name.
Requires: qt4-doc
Obsoletes: kdelibs4-apidoc

%description apidoc
This packages contains all development documentation for kdelibs

%files apidoc
%defattr(-,root,root,-)

#--------------------------------------------------------------

%prep
%setup -q -n kdelibs
%patch0 -p1 -b .homedir

%build
%if %unstable
CFLAGS="-fPIC"
CXXFLAGS="-fPIC"
%endif

%cmake_kde4 \
%if %use_enable_final
    -DKDE4_ENABLE_FINAL=ON \
%endif
%if %use_enable_pie
    -DKDE4_ENABLE_FPIE=ON \
%endif
%if %unstable
    -DCMAKE_BUILD_TYPE=debug
%endif

%make


%if %{compile_apidox}
    cd ..
    doc/api/doxygen.sh --doxdatadir=${PWD}/doc/common .
%endif

%install
rm -fr %buildroot
cd build

make DESTDIR=%buildroot install

install -d %buildroot/etc/ld.so.conf.d

cat > %buildroot/etc/ld.so.conf.d/kde4.conf <<EOF
%_kde_libdir
EOF


cat > %buildroot/%_kde_prefix/README.urpmi <<EOF
Mandriva RPM specific notes

WARNING
-------
These packages are not STABLE. Not to use them in production. 
Install theses packages just for testing (otherwise uninstall
them)

We use for the moment KDE standard menu, Mandriva menu is not 
supported for the moment.
EOF


%clean
rm -fr %buildroot

