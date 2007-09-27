%define compile_apidox 0
%{?_no_apidox: %{expand: %%global compile_apidox 0}}

%define branch 1
%{?_branch: %{expand: %%global branch 1}}

%define revision 714006

Name: kdelibs4
Summary: K Desktop Environment - Libraries
Version: 3.93.0
Release: %mkrel 0.%revision.2
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
BuildRequires: OpenEXR-devel
BuildRequires: libacl-devel
BuildRequires: krb5-devel
BuildRequires: ungif-devel
BuildRequires: strigi-devel >=  0.5.1
BuildRequires: shared-mime-info
BuildRequires: soprano-devel

%description 
Libraries for the K Desktop Environment.

#------------------------------------------------	

%define libkaudiodevicelist %mklibname kaudiodevicelist 4

%package -n %libkaudiodevicelist
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}kaudiodevicelist5 < 3.93.0-0.714006.1

%description -n %libkaudiodevicelist
KDE 4 core library.

%post -n %libkaudiodevicelist -p /sbin/ldconfig
%postun -n %libkaudiodevicelist -p /sbin/ldconfig

%files -n %libkaudiodevicelist
%defattr(-,root,root)
%_kde_libdir/libkaudiodevicelist.so.*

#------------------------------------------------	

%define libkde3support %mklibname kde3support 4

%package -n %libkde3support
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}kde3support5 < 3.93.0-0.714006.1

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
Obsoletes: %{_lib}kdecore5 >= 30000000:3.80.3

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
Obsoletes: %{_lib}kdecore5 >= 30000000:3.80.3

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
Obsoletes: %{_lib}kdecore5 >= 30000000:3.80.3

%description -n %libkdefx
KDE 4 core library.

%post -n %libkdefx -p /sbin/ldconfig
%postun -n %libkdefx -p /sbin/ldconfig

%files -n %libkdefx
%defattr(-,root,root)
%_kde_libdir/libkdefx.so.*

#------------------------------------------------	

%define libkdeprint_management %mklibname kdeprint_management 4

%package -n %libkdeprint_management
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}kdeprint_management5 < 3.93.0-0.714006.1

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
Obsoletes: %{_lib}kdecore5 >= 30000000:3.80.3

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
Obsoletes: %{_lib}kdecore5 >= 30000000:3.80.3

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
Obsoletes: %{_lib}kdecore5 >= 30000000:3.80.3

%description -n %libkdeui
KDE 4 core library.

%post -n %libkdeui -p /sbin/ldconfig
%postun -n %libkdeui -p /sbin/ldconfig

%files -n %libkdeui
%defattr(-,root,root)
%_kde_libdir/libkdeui.so.*

#------------------------------------------------	

%define libkdnssd %mklibname kdnssd 4

%package -n %libkdnssd
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}kdnssd5 < 3.93.0-0.714006.1

%description -n %libkdnssd
KDE 4 core library.

%post -n %libkdnssd -p /sbin/ldconfig
%postun -n %libkdnssd -p /sbin/ldconfig

%files -n %libkdnssd
%defattr(-,root,root)
%_kde_libdir/libkdnssd.so.*

#------------------------------------------------	

%define libkfile %mklibname kfile 4

%package -n %libkfile
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}kfile5 < 3.93.0-0.714006.1

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
Obsoletes: %{_lib}kdecore5 >= 30000000:3.80.3

%description -n %libkhtml
KDE 4 core library.

%post -n %libkhtml -p /sbin/ldconfig
%postun -n %libkhtml -p /sbin/ldconfig

%files -n %libkhtml
%defattr(-,root,root)
%_kde_libdir/libkhtml.so.*

#------------------------------------------------	

%define libkimproxy %mklibname kimproxy 4

%package -n %libkimproxy
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}kimproxy5 < 3.93.0-0.714006.1

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
Obsoletes: %{_lib}kdecore5 >= 30000000:3.80.3

%description -n %libkio
KDE 4 core library.

%post -n %libkio -p /sbin/ldconfig
%postun -n %libkio -p /sbin/ldconfig

%files -n %libkio
%defattr(-,root,root)
%_kde_libdir/libkio.so.*

#------------------------------------------------	

%define libkjsembed %mklibname kjsembed 4

%package -n %libkjsembed
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}kjsembed5 < 3.93.0-0.714006.1

%description -n %libkjsembed
KDE 4 core library.

%post -n %libkjsembed -p /sbin/ldconfig
%postun -n %libkjsembed -p /sbin/ldconfig

%files -n %libkjsembed
%defattr(-,root,root)
%_kde_libdir/libkjsembed.so.*

#------------------------------------------------	

%define libkjs %mklibname kjs 4

%package -n %libkjs
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}kjs5 < 3.93.0-0.714006.1

%description -n %libkjs
KDE 4 core library.

%post -n %libkjs -p /sbin/ldconfig
%postun -n %libkjs -p /sbin/ldconfig

%files -n %libkjs
%defattr(-,root,root)
%_kde_libdir/libkjs.so.*

#------------------------------------------------	

%define libkmediaplayer %mklibname kmediaplayer 4

%package -n %libkmediaplayer
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}kmediaplayer5 < 3.93.0-0.714006.1

%description -n %libkmediaplayer
KDE 4 core library.

%post -n %libkmediaplayer -p /sbin/ldconfig
%postun -n %libkmediaplayer -p /sbin/ldconfig

%files -n %libkmediaplayer
%defattr(-,root,root)
%_kde_libdir/libkmediaplayer.so.*

#------------------------------------------------	

%define libnepomukmiddleware %mklibname nepomuk-middleware 4

%package -n %libnepomukmiddleware
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}nepomuk-middleware5 < 3.93.0-0.714006.1

%description -n %libnepomukmiddleware
KDE 4 core library.

%post -n %libnepomukmiddleware -p /sbin/ldconfig
%postun -n %libnepomukmiddleware -p /sbin/ldconfig

%files -n %libnepomukmiddleware
%defattr(-,root,root)
%_kde_libdir/libnepomuk-middleware.so.*

#------------------------------------------------	

%define libnepomuk %mklibname nepomuk 4

%package -n %libnepomuk
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}knepomuk5 < 3.93.0-0.714006.1
Obsoletes: %{_lib}nepomuk5 < 3.93.0-0.714006.1
Obsoletes: %{_lib}kmetadata5 < 3.93.0-0.714006.1
Obsoletes: %{_lib}konto5 < 3.93.0-0.714006.1

%description -n %libnepomuk
KDE 4 core library.

%post -n %libnepomuk -p /sbin/ldconfig
%postun -n %libnepomuk -p /sbin/ldconfig

%files -n %libnepomuk
%defattr(-,root,root)
%_kde_libdir/libnepomuk.so.*

#------------------------------------------------	

%define libknewstuff2 %mklibname knewstuff2 4

%package -n %libknewstuff2
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}knewstuff25 < 3.93.0-0.714006.1

%description -n %libknewstuff2
KDE 4 core library.

%post -n %libknewstuff2 -p /sbin/ldconfig
%postun -n %libknewstuff2 -p /sbin/ldconfig

%files -n %libknewstuff2
%defattr(-,root,root)
%_kde_libdir/libknewstuff2.so.*

#------------------------------------------------	

%define libknotifyconfig %mklibname knotifyconfig 4

%package -n %libknotifyconfig
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}knotifyconfig5 < 3.93.0-0.714006.1

%description -n %libknotifyconfig
KDE 4 core library.

%post -n %libknotifyconfig -p /sbin/ldconfig
%postun -n %libknotifyconfig -p /sbin/ldconfig

%files -n %libknotifyconfig
%defattr(-,root,root)
%_kde_libdir/libknotifyconfig.so.*

#------------------------------------------------	

%define libkntlm %mklibname kntlm 4

%package -n %libkntlm
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}kntlm5 < 3.93.0-0.714006.1

%description -n %libkntlm
KDE 4 core library.

%post -n %libkntlm -p /sbin/ldconfig
%postun -n %libkntlm -p /sbin/ldconfig

%files -n %libkntlm
%defattr(-,root,root)
%_kde_libdir/libkntlm.so.*

#------------------------------------------------	

%define libkparts %mklibname kparts 4

%package -n %libkparts
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}kparts5 < 3.93.0-0.714006.1

%description -n %libkparts
KDE 4 core library.

%post -n %libkparts -p /sbin/ldconfig
%postun -n %libkparts -p /sbin/ldconfig

%files -n %libkparts
%defattr(-,root,root)
%_kde_libdir/libkparts.so.*

#------------------------------------------------	

%define libkrosscore %mklibname krosscore 4

%package -n %libkrosscore
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}krosscore5 < 3.93.0-0.714006.1

%description -n %libkrosscore
KDE 4 core library.

%post -n %libkrosscore -p /sbin/ldconfig
%postun -n %libkrosscore -p /sbin/ldconfig

%files -n %libkrosscore
%defattr(-,root,root)
%_kde_libdir/libkrosscore.so.*

#------------------------------------------------	

%define libkrossui %mklibname krossui 4

%package -n %libkrossui
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}krossui5 < 3.93.0-0.714006.1

%description -n %libkrossui
KDE 4 core library.

%post -n %libkrossui -p /sbin/ldconfig
%postun -n %libkrossui -p /sbin/ldconfig

%files -n %libkrossui
%defattr(-,root,root)
%_kde_libdir/libkrossui.so.*

#------------------------------------------------	

%define libktexteditor %mklibname ktexteditor 4

%package -n %libktexteditor
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}ktexteditor5 < 3.93.0-0.714006.1

%description -n %libktexteditor
KDE 4 core library.

%post -n %libktexteditor -p /sbin/ldconfig
%postun -n %libktexteditor -p /sbin/ldconfig

%files -n %libktexteditor
%defattr(-,root,root)
%_kde_libdir/libktexteditor.so.*

#------------------------------------------------	

%define libkunittest %mklibname kunittest 4

%package -n %libkunittest
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}kunittest5 < 3.93.0-0.714006.1

%description -n %libkunittest
KDE 4 core library.

%post -n %libkunittest -p /sbin/ldconfig
%postun -n %libkunittest -p /sbin/ldconfig

%files -n %libkunittest
%defattr(-,root,root)
%_kde_libdir/libkunittest.so.*

#------------------------------------------------

%define libcupsdconf %mklibname cupsdconf 4

%package -n %libcupsdconf
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}cupsdconf5 < 3.93.0-0.714006.1

%description -n %libcupsdconf
KDE 4 core library.

%post -n %libcupsdconf -p /sbin/ldconfig
%postun -n %libcupsdconf -p /sbin/ldconfig

%files -n %libcupsdconf
%defattr(-,root,root)
%_kde_libdir/libcupsdconf.so.*

#------------------------------------------------	

%define libkutils %mklibname kutils 4

%package -n %libkutils
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}kutils5 < 3.93.0-0.714006.1

%description -n %libkutils
KDE 4 core library.

%post -n %libkutils -p /sbin/ldconfig
%postun -n %libkutils -p /sbin/ldconfig

%files -n %libkutils
%defattr(-,root,root)
%_kde_libdir/libkutils.so.*

#------------------------------------------------	

%define libkwalletbackend %mklibname kwalletbackend 4

%package -n %libkwalletbackend
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}kwalletbackend5 < 3.93.0-0.714006.1

%description -n %libkwalletbackend
KDE 4 core library.

%post -n %libkwalletbackend -p /sbin/ldconfig
%postun -n %libkwalletbackend -p /sbin/ldconfig

%files -n %libkwalletbackend
%defattr(-,root,root)
%_kde_libdir/libkwalletbackend.so.*

#------------------------------------------------	

%define libphononexperimental %mklibname phononexperimental 4

%package -n %libphononexperimental
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}phononexperimental5 < 3.93.0-0.714006.1

%description -n %libphononexperimental
KDE 4 core library.

%post -n %libphononexperimental -p /sbin/ldconfig
%postun -n %libphononexperimental -p /sbin/ldconfig

%files -n %libphononexperimental
%defattr(-,root,root)
%_kde_libdir/libphononexperimental.so.*

#------------------------------------------------	

%define libphonon %mklibname phonon 4

%package -n %libphonon
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}phonon5 < 3.93.0-0.714006.1

%description -n %libphonon
KDE 4 core library.

%post -n %libphonon -p /sbin/ldconfig
%postun -n %libphonon -p /sbin/ldconfig

%files -n %libphonon
%defattr(-,root,root)
%_kde_libdir/libphonon.so.*

#------------------------------------------------	

%define libsolid %mklibname solid 4

%package -n %libsolid
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}solid5 < 3.93.0-0.714006.1

%description -n %libsolid
KDE 4 core library.

%post -n %libsolid -p /sbin/ldconfig
%postun -n %libsolid -p /sbin/ldconfig

%files -n %libsolid
%defattr(-,root,root)
%_kde_libdir/libsolid.so.*

#------------------------------------------------	

%define libthreadweaver %mklibname threadweaver 4

%package -n %libthreadweaver
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}threadweaver5 < 3.93.0-0.714006.1

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
Obsoletes: %{_lib}kdecore5-devel < 3.93.0-0.714006.1

%description devel
This package includes the header files you will need to compile applications 
for KDE. Also included is the KDE API documentation in HTML format for easy 
browsing.

%files devel
%defattr(-,root,root,-)
%_kde_prefix/include/*
%_kde_appsdir/cmake/modules/*
%_datadir/dbus-1/*/*
%_kde_libdir/*.so
%_kde_libdir/kde4/plugins/designer
%_kde_bindir/checkXML
%_kde_bindir/kconfig_compiler
%exclude %_kde_libdir/libkdeinit4_*

#--------------------------------------------------------------

%package core
Group: Graphical desktop/KDE
Summary: KDE 4 system core files
Requires: aspell
Obsoletes: kdelibs4-common < 3.93.0-0.714006.1
Conflicts: kdelibs4-devel < 3.90.2-0.678253 
Requires: shared-mime-info

%description core
KDE 4 system core files.

%files core
%defattr(-,root,root,-)
%_kde_prefix/README.urpmi
%attr(0755,root,root) %_sysconfdir/profile.d/*
%_kde_bindir/*
%_kde_libdir/kde4/*
%_kde_libdir/libkdeinit4_*
%_kde_appsdir/*/*
%_kde_datadir/config/*
%_kde_datadir/mime
%_kde_datadir/locale/all_languages
%_kde_datadir/kde4/services/*
%_kde_datadir/kde4/servicetypes/*
%_kde_docdir/HTML/en/sonnet
%_kde_configdir/xdg/menus/applications.menu
%_kde_docdir/HTML/en/common/*
%exclude %_kde_bindir/checkXML
%exclude %_kde_bindir/kconfig_compiler
%exclude %_kde_appsdir/cmake/modules/*
%exclude %_kde_libdir/kde4/plugins/designer
# exclude remaining icons. should not be here
%exclude %_kde_datadir/icons

%pre core
if [ -d %_kde_datadir/mime ]; then
	rm -rf %_kde_datadir/mime
fi

#--------------------------------------------------------------

%package apidoc
Group: Development/KDE and Qt
Summary: Development documentation for %name.
Requires: qt4-doc
Obsoletes: kdelibs4-apidoc < 3.93.0-0.714006.1

%description apidoc
This packages contains all development documentation for kdelibs

%files apidoc
%defattr(-,root,root,-)

#--------------------------------------------------------------

%prep
%setup -q -n kdelibs-%version
%patch0 -p1 -b .homedir

%build
%cmake_kde4 

%make


%if %{compile_apidox}
    cd ..
    doc/api/doxygen.sh --doxdatadir=${PWD}/doc/common .
%endif

%install
rm -fr %buildroot
cd build

make DESTDIR=%buildroot install

# Are libs really conflicting with kde3 libs ?  
#install -d %buildroot/etc/ld.so.conf.d

#cat > %buildroot/etc/ld.so.conf.d/kde4.conf <<EOF
#%_kde_libdir
#EOF

# Env entry for setup kde4  environment
install -d -m 0755 %buildroot/etc/profile.d
install -m 0755 %_sourcedir/kde4env.sh %buildroot/etc/profile.d/

# use shared-mime-info
rm -rf %buildroot%_kde_datadir/mime
ln -s %_datadir/mime %buildroot%_kde_datadir/mime

cat > %buildroot/%_kde_prefix/README.urpmi <<EOF
Mandriva RPM specific notes

WARNING
-------
These packages are not STABLE. Not to use them in production. 
Install theses packages just for testing (otherwise uninstall
them)

EOF


%clean
rm -fr %buildroot

