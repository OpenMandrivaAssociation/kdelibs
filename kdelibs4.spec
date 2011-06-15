%define branch 0
%{?_branch: %{expand: %%global branch 1}}

%define experimental 0
%{?_experimental: %{expand: %%global experimental 1}}

%define compile_apidox 0
%{?_with_apidox: %{expand: %%global compile_apidox 1}}

%define with_drkonqi 0
%{?_with_drkonqi: %{expand: %%global with_drkonqi 1}}

%define epoch_kdelibs3 30000000

%if %branch
%define kde_snapshot svn1198704
%endif

%define udisk_backend 1

Name: kdelibs4
Summary: K Desktop Environment - Libraries
Version: 4.6.4
%if %branch
Release: 0.%kde_snapshot.1
%else
Release: 4
%endif
Epoch: 2
Group: Graphical desktop/KDE
License: ARTISTIC BSD GPL_V2 LGPL_V2 QPL_V1.0
BuildRoot: %_tmppath/%name-%version-%release-root
URL: http://www.kde.org
%if %branch
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdelibs-%version%kde_snapshot.tar.bz2
%if %experimental
Source1: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdelibs-experimental-%version%kde_snapshot.tar.bz2
%endif
%else
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdelibs-%version.tar.bz2
%if %experimental
Source1: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdelibs-experimental-%version.tar.bz2
%endif
%endif
Patch1: kdelibs-4.5.85-add-extra-catalogs.patch
Patch2: kdelibs-4.1.85-add-kde-menu.patch
Patch3: kdelibs-4.5.80-usr-abrt-instead-of-drkonqi.patch
Patch200: kdelibs-4.6.4-sync-nepomuk-with-trunk.patch
Patch201: kdelibs-4.6.3-add-NetworkShare-trunk.patch
Patch202: kdelibs-4.6.3-add-missing-include.patch
Patch203: kdelibs-4.6.4-add-missing-nepomuk-include.patch
BuildRequires: kde4-macros >= 4.1.71
BuildRequires: qt4-devel >= 4:4.7.0
BuildRequires: qt4-qtdbus
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
BuildRequires: libsasl-devel
BuildRequires: libtiff-devel
BuildRequires: libvorbis-devel
BuildRequires: pam-devel
BuildRequires: libalsa-devel
BuildRequires: libmad-devel
BuildRequires: gdbm-devel
BuildRequires: jasper-devel
BuildRequires: OpenEXR-devel
BuildRequires: libacl-devel
BuildRequires: krb5-devel
BuildRequires: ungif-devel
BuildRequires: strigi-devel >= 0.6.3
BuildRequires: shared-mime-info
BuildRequires: soprano-devel >= 4:2.5.60
BuildRequires: automoc
BuildRequires: phonon-devel >= 2:4.2
BuildRequires: xpm-devel
BuildRequires: xft2-devel
BuildRequires: libxml2-utils
BuildRequires: liblzma-devel
BuildRequires: libutempter-devel
BuildRequires: rootcerts
BuildRequires: flex
BuildRequires: bison
BuildRequires: qca2-devel
BuildRequires: polkit-qt-1-devel >= 0.98.1
BuildRequires: shared-desktop-ontologies-devel
BuildRequires: attica-devel
BuildRequires: libxscrnsaver-devel
BuildRequires: libdbusmenu-qt-devel 
BuildRequires: docbook-dtd42-xml
BuildRequires: docbook-style-xsl
BuildRequires: aspell-devel
BuildRequires: hspell-devel
%if %udisk_backend
Buildrequires: udev-devel
%endif

%description 
Libraries for the K Desktop Environment.

#------------------------------------------------	

%define kde3support_major 4
%define libkde3support %mklibname kde3support %kde3support_major

%package -n %libkde3support
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= %{epoch_kdelibs3}:3.80.3
Obsoletes: %{_lib}kde3support5 < 3.93.0-0.714006.1

%description -n %libkde3support
KDE 4 core library.

%files -n %libkde3support
%_kde_libdir/libkde3support.so.%{kde3support_major}*

#------------------------------------------------	

%define kdecore_major 5
%define libkdecore %mklibname kdecore %kdecore_major

%package -n %libkdecore
Summary: KDE 4 core library
Group: System/Libraries
Requires: phonon-backend >= 4.2.0
Requires: kde4-config-file 
Requires: kde-l10n
Requires: kdelibs4-core = %epoch:%{version}

%description -n %libkdecore
KDE 4 core library.

%files -n %libkdecore
%_kde_libdir/libkdecore.so.%{kdecore_major}*

#------------------------------------------------	

%define kdefakes_major 5
%define libkdefakes %mklibname kdefakes %kdefakes_major

%package -n %libkdefakes
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libkdefakes
KDE 4 core library.

%files -n %libkdefakes
%_kde_libdir/libkdefakes.so.%{kdefakes_major}*

#------------------------------------------------	

%define kdesu_major 5
%define libkdesu %mklibname kdesu %kdesu_major

%package -n %libkdesu
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libkdesu
KDE 4 core library.

%files -n %libkdesu
%_kde_libdir/libkdesu.so.%{kdesu_major}*

#------------------------------------------------	

%define kdeui_major 5
%define libkdeui %mklibname kdeui %kdeui_major

%package -n %libkdeui
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libkdeui
KDE 4 core library.

%files -n %libkdeui
%_kde_libdir/libkdeui.so.%{kdeui_major}*

#------------------------------------------------	

%define kdnssd_major 4
%define libkdnssd %mklibname kdnssd %kdnssd_major

%package -n %libkdnssd
Summary: KDE 4 core library
Group: System/Libraries
 
%description -n %libkdnssd
KDE 4 core library.

%files -n %libkdnssd
%_kde_libdir/libkdnssd.so.%{kdnssd_major}*

#------------------------------------------------	

%define kfile_major 4
%define libkfile %mklibname kfile %kfile_major

%package -n %libkfile
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libkfile
KDE 4 core library.

%files -n %libkfile
%_kde_libdir/libkfile.so.%{kfile_major}*

#------------------------------------------------	

%define khtml_major 5
%define libkhtml %mklibname khtml %khtml_major

%package -n %libkhtml
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libkhtml
KDE 4 core library.

%files -n %libkhtml
%_kde_libdir/libkhtml.so.%{khtml_major}*

#------------------------------------------------	

%define kimproxy_major 4
%define libkimproxy %mklibname kimproxy %kimproxy_major

%package -n %libkimproxy
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libkimproxy
KDE 4 core library.

%files -n %libkimproxy
%_kde_libdir/libkimproxy.so.%{kimproxy_major}*

#------------------------------------------------	

%define kio_major 5
%define libkio %mklibname kio %kio_major

%package -n %libkio
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libkio
KDE 4 core library.

%files -n %libkio
%_kde_libdir/libkio.so.%{kio_major}*

#------------------------------------------------	

%define kjsembed_major 4
%define libkjsembed %mklibname kjsembed %kjsembed_major

%package -n %libkjsembed
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libkjsembed
KDE 4 core library.

%files -n %libkjsembed
%_kde_libdir/libkjsembed.so.%{kjsembed_major}*

#------------------------------------------------	

%define kjs_major 4
%define libkjs %mklibname kjs %kjs_major

%package -n %libkjs
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libkjs
KDE 4 core library.

%files -n %libkjs
%_kde_libdir/libkjs.so.%{kjs_major}*

#------------------------------------------------	

%define kmediaplayer_major 4
%define libkmediaplayer %mklibname kmediaplayer %kmediaplayer_major

%package -n %libkmediaplayer
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libkmediaplayer
KDE 4 core library.

%files -n %libkmediaplayer
%_kde_libdir/libkmediaplayer.so.%{kmediaplayer_major}*

#------------------------------------------------	

%define nepomuk_major 4
%define libnepomuk %mklibname nepomuk %nepomuk_major

%package -n %libnepomuk
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libnepomuk
KDE 4 core library.

%files -n %libnepomuk
%_kde_libdir/libnepomuk.so.%{nepomuk_major}*

#------------------------------------------------	

%define knewstuff2_major 4
%define libknewstuff2 %mklibname knewstuff2_ %knewstuff2_major

%package -n %libknewstuff2
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libknewstuff2
KDE 4 core library.

%files -n %libknewstuff2
%_kde_libdir/libknewstuff2.so.%{knewstuff2_major}*

#------------------------------------------------	

%define knotifyconfig_major 4
%define libknotifyconfig %mklibname knotifyconfig %knotifyconfig_major

%package -n %libknotifyconfig
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libknotifyconfig
KDE 4 core library.

%files -n %libknotifyconfig
%_kde_libdir/libknotifyconfig.so.%{knotifyconfig_major}*

#------------------------------------------------	

%define kntlm_major 4
%define libkntlm %mklibname kntlm %kntlm_major

%package -n %libkntlm
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libkntlm
KDE 4 core library.

%files -n %libkntlm
%_kde_libdir/libkntlm.so.%{kntlm_major}*

#------------------------------------------------	

%define kparts_major 4
%define libkparts %mklibname kparts %kparts_major

%package -n %libkparts
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libkparts
KDE 4 core library.

%files -n %libkparts
%_kde_libdir/libkparts.so.%{kparts_major}*

#------------------------------------------------	

%define krosscore_major 4
%define libkrosscore %mklibname krosscore %krosscore_major

%package -n %libkrosscore
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libkrosscore
KDE 4 core library.

%files -n %libkrosscore
%_kde_libdir/libkrosscore.so.%{krosscore_major}*

#------------------------------------------------	

%define krossui_major 4
%define libkrossui %mklibname krossui %krossui_major

%package -n %libkrossui
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libkrossui
KDE 4 core library.

%files -n %libkrossui
%_kde_libdir/libkrossui.so.%{krossui_major}*

#------------------------------------------------	

%define ktexteditor_major 4
%define libktexteditor %mklibname ktexteditor %ktexteditor_major

%package -n %libktexteditor
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libktexteditor
KDE 4 core library.

%files -n %libktexteditor
%_kde_libdir/libktexteditor.so.%{ktexteditor_major}*

#------------------------------------------------	

%define kunittest_major 4
%define libkunittest %mklibname kunittest %kunittest_major

%package -n %libkunittest
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libkunittest
KDE 4 core library.

%files -n %libkunittest
%_kde_libdir/libkunittest.so.%{kunittest_major}*

#------------------------------------------------	

%define kutils_major 4
%define libkutils %mklibname kutils %kutils_major

%package -n %libkutils
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libkutils
KDE 4 core library.

%files -n %libkutils
%_kde_libdir/libkutils.so.%{kutils_major}*

#------------------------------------------------	

%define solid_major 4
%define libsolid %mklibname solid %solid_major

%package -n %libsolid
Summary: KDE 4 core library
Group: System/Libraries
 
%description -n %libsolid
KDE 4 core library.

%files -n %libsolid
%_kde_libdir/libsolid.so.%{solid_major}*

#------------------------------------------------

%define threadweaver_major 4
%define libthreadweaver %mklibname threadweaver %threadweaver_major

%package -n %libthreadweaver
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libthreadweaver
KDE 4 core library.

%files -n %libthreadweaver
%_kde_libdir/libthreadweaver.so.%{threadweaver_major}*

#------------------------------------------------

%define kpty_major 4
%define libkpty %mklibname kpty %kpty_major

%package -n %libkpty
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libkpty
KDE 4 core library.

%files -n %libkpty
%_kde_libdir/libkpty.so.%{kpty_major}*

#------------------------------------------------

%define kjsapi_major 4
%define libkjsapi %mklibname kjsapi %kjsapi_major

%package -n %libkjsapi
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libkjsapi
KDE 4 core library.

%files -n %libkjsapi
%_kde_libdir/libkjsapi.so.%{kjsapi_major}*

#------------------------------------------------

%define libplasma_major 3
%define libplasma %mklibname plasma %{libplasma_major}

%package -n %libplasma
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libplasma
KDE 4 core library.

%files -n %libplasma
%_kde_libdir/libplasma.so.%{libplasma_major}*

#------------------------------------------------

%define libkunitconversion_major 4
%define libkunitconversion %mklibname kunitconversion %{libkunitconversion_major}

%package -n %libkunitconversion
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libkunitconversion
KDE 4 core library.

%files -n %libkunitconversion
%_kde_libdir/libkunitconversion.so.%{libkunitconversion_major}*

#------------------------------------------------

%define libnepomukquery_major 4
%define libnepomukquery %mklibname nepomukquery %{libnepomukquery_major}

%package -n %libnepomukquery
Summary: KDE 4 library
Group: System/Libraries

%description -n %libnepomukquery
KDE 4 library.

%files -n %libnepomukquery
%_kde_libdir/libnepomukquery.so.%{libnepomukquery_major}*

#------------------------------------------------

%define libkdewebkit_major 5
%define libkdewebkit %mklibname kdewebkit %{libkdewebkit_major}

%package -n %libkdewebkit
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkdewebkit
KDE 4 library.

%files -n %libkdewebkit
%_kde_libdir/libkdewebkit.so.%{libkdewebkit_major}*


#------------------------------------------------

%define libknewstuff3_major 4
%define libknewstuff3 %mklibname knewstuff3_ %{libknewstuff3_major}

%package -n %libknewstuff3
Summary: KDE 4 library
Group: System/Libraries

%description -n %libknewstuff3
KDE 4 library.

%files -n %libknewstuff3
%_kde_libdir/libknewstuff3.so.%{libknewstuff3_major}*

#------------------------------------------------

%define libkatepartinterfaces_major 4
%define libkatepartinterfaces %mklibname katepartinterfaces %{libkatepartinterfaces_major}

%package -n %libkatepartinterfaces
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkatepartinterfaces
KDE 4 library.

%files -n %libkatepartinterfaces
%_kde_libdir/libkatepartinterfaces.so.%{libkatepartinterfaces_major}*

#------------------------------------------------

%define libkcmutils_major 4
%define libkcmutils %mklibname kcmutils %{libkcmutils_major}

%package -n %libkcmutils
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkcmutils
KDE 4 library.

%files -n %libkcmutils
%_kde_libdir/libkcmutils.so.%{libkcmutils_major}*

#------------------------------------------------

%define libkprintutils_major 4
%define libkprintutils %mklibname kprintutils %{libkprintutils_major}

%package -n %libkprintutils
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkprintutils
KDE 4 library.

%files -n %libkprintutils
%_kde_libdir/libkprintutils.so.%{libkprintutils_major}*

#------------------------------------------------

%define libkidletime_major 4
%define libkidletime %mklibname kidletime %{libkidletime_major}

%package -n %libkidletime
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkidletime
KDE 4 library.

%files -n %libkidletime
%_kde_libdir/libkidletime.so.%{libkidletime_major}*


#------------------------------------------------

%define libkemoticons_major 4
%define libkemoticons %mklibname kemoticons %{libkemoticons_major}

%package -n %libkemoticons
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkemoticons
KDE 4 library.

%files -n %libkemoticons
%_kde_libdir/libkemoticons.so.%{libkemoticons_major}*

#------------------------------------------------

%define libnepomukutils_major 4
%define libnepomukutils %mklibname nepomukutils %{libnepomukutils_major}

%package -n %libnepomukutils
Summary: KDE 4 library
Group: System/Libraries

%description -n %libnepomukutils
KDE 4 library.

%files -n %libnepomukutils
%_kde_libdir/libnepomukutils.so.%{libnepomukutils_major}*

#------------------------------------------------

%package devel
Group: Development/KDE and Qt
Summary: Header files and documentation for compiling KDE applications
Requires: kde4-macros
Requires: automoc4
Requires: acl-devel
Requires: qt4-devel >= 4:4.7.0
Requires: qt4-qtdbus
Requires: kdelibs4-core = %epoch:%version
Requires: soprano-devel >= 4:2.5.60
Requires: strigi-devel
# add requires on libxml2-utils, as when building most kde applications,
# it will call xmllint to validate the docbook files:
Requires: libxml2-utils
Requires: avahi-compat-libdns_sd-devel 
Requires: avahi-client-devel
Requires: enchant-devel
Requires: libxslt-proc
Requires: libxslt-devel
Requires: openssl-devel
Requires: cups-devel >= 1.2
Requires: pcre-devel
Requires: fam-devel
Requires: bzip2-devel
Requires: libart_lgpl-devel
Requires: libjpeg-devel
Requires: libpng-devel
Requires: libsasl-devel
Requires: libtiff-devel
Requires: libvorbis-devel
Requires: pam-devel
Requires: libalsa-devel
Requires: libmad-devel
Requires: gdbm-devel
Requires: jasper-devel
Requires: OpenEXR-devel
Requires: libacl-devel
Requires: krb5-devel
Requires: ungif-devel
Requires: strigi-devel >= 0.6.3
Requires: shared-mime-info
Requires: soprano-devel >= 2.0.98
Requires: xpm-devel
Requires: xft2-devel
Requires: shared-desktop-ontologies-devel >= 0.5
Provides: plasma-devel = %epoch:%version
Requires: %libkatepartinterfaces = %epoch:%version
Requires: %libkcmutils = %epoch:%version
Requires: %libkde3support = %epoch:%version
Requires: %libkdecore = %epoch:%version
Requires: %libkdefakes = %epoch:%version
Requires: %libkdesu = %epoch:%version
Requires: %libkdeui = %epoch:%version
Requires: %libkdewebkit = %epoch:%version
Requires: %libkdnssd = %epoch:%version
Requires: %libkemoticons = %epoch:%version
Requires: %libkfile = %epoch:%version
Requires: %libkhtml = %epoch:%version
Requires: %libkidletime = %epoch:%version
Requires: %libkimproxy = %epoch:%version
Requires: %libkio = %epoch:%version
Requires: %libkjsapi = %epoch:%version
Requires: %libkjsembed = %epoch:%version
Requires: %libkjs = %epoch:%version
Requires: %libkmediaplayer = %epoch:%version
Requires: %libknewstuff2 = %epoch:%version
Requires: %libknewstuff3 = %epoch:%version
Requires: %libknotifyconfig = %epoch:%version
Requires: %libkntlm = %epoch:%version
Requires: %libkparts = %epoch:%version
Requires: %libkprintutils = %epoch:%version
Requires: %libkpty = %epoch:%version
Requires: %libkrosscore = %epoch:%version
Requires: %libkrossui = %epoch:%version
Requires: %libktexteditor = %epoch:%version
Requires: %libkunitconversion = %epoch:%version
Requires: %libkunittest = %epoch:%version
Requires: %libkutils = %epoch:%version
Requires: %libnepomuk = %epoch:%version
Requires: %libnepomukquery = %epoch:%version
Requires: %libnepomukutils = %epoch:%version
Requires: %libplasma = %epoch:%version
Requires: %libsolid = %epoch:%version
Requires: %libthreadweaver = %epoch:%version
Conflicts: koffice-devel < 11:1.9.95.9-2mdv
Conflicts: webkitkde-devel < 0.0-0.1050148.3
Conflicts: kdeplatform4-devel < 4:0.9.97-3

%description devel
This package includes the header files you will need to compile applications 
for KDE. Also included is the KDE API documentation in HTML format for easy 
browsing.

%files devel
%_mandir/man1/kdecmake.1*
%_kde_includedir/*
%_kde_appsdir/cmake/modules/*
%_kde_datadir/dbus-1/*/*
%_kde_libdir/libkdefakes.so
%_kde_libdir/libkdesu.so
%_kde_libdir/libkdnssd.so
%_kde_libdir/libkhtml.so
%_kde_libdir/libkimproxy.so
%_kde_libdir/libkjs.so
%_kde_libdir/libkjsembed.so
%_kde_libdir/libkmediaplayer.so
%_kde_libdir/libknewstuff2.so
%_kde_libdir/libknotifyconfig.so
%_kde_libdir/libkntlm.so
%_kde_libdir/libkparts.so
%_kde_libdir/libkrossui.so
%_kde_libdir/libktexteditor.so
%_kde_libdir/libkunittest.so
%_kde_libdir/libkutils.so
%_kde_libdir/libnepomuk.so
%_kde_libdir/libkde3support.so
%_kde_libdir/libkpty.so
%_kde_libdir/libkfile.so
%_kde_libdir/libsolid.so
%_kde_libdir/libkrosscore.so
%_kde_libdir/libkdecore.so
%_kde_libdir/libkdeui.so
%_kde_libdir/libkio.so
%_kde_libdir/libthreadweaver.so
%_kde_libdir/libkjsapi.so
%_kde_libdir/libplasma.so
%_kde_libdir/libkunitconversion.so
%_kde_libdir/libnepomukquery.so
%_kde_libdir/libkdewebkit.so
%_kde_libdir/libknewstuff3.so
%_kde_libdir/libkprintutils.so
%_kde_libdir/libkidletime.so
%_kde_libdir/libkemoticons.so
%_kde_libdir/libkcmutils.so
%_kde_libdir/libkatepartinterfaces.so
%_kde_libdir/libnepomukutils.so
%_kde_libdir/kde4/plugins/designer
%_kde_bindir/checkXML
%_kde_mandir/man1/checkXML.1*
%_kde_bindir/kconfig_compiler

#--------------------------------------------------------------
%package core
Group: Graphical desktop/KDE
Summary: KDE 4 system core files
Suggests: enchant-dictionary
Suggests: xdg-utils
Requires: shared-mime-info
Requires: docbook-dtd42-xml
Requires: docbook-style-xsl
Conflicts: kdebase4-workspace < 2:4.1.73-1
Requires: rootcerts
Requires: shared-desktop-ontologies
Obsoletes: lilypond-kde4 < 0.2-3
Conflicts: kde-l10n-en_US < 2:4.6.4-1 
Requires:  abrt

%description core
KDE 4 system core files.

%files core
%_kde_bindir/kbuildsycoca4
%_kde_bindir/kcookiejar4
%_kde_bindir/kde4-config
%_kde_bindir/kded4
%_kde_bindir/kdeinit4
%_kde_bindir/kdeinit4_shutdown
%_kde_bindir/kdeinit4_wrapper
%_kde_bindir/kjs
%_kde_bindir/kjscmd
%_kde_bindir/kross
%_kde_bindir/kshell4
%_kde_bindir/kunittestmodrunner
%_kde_bindir/kwrapper4
%_kde_bindir/makekdewidgets
%_kde_bindir/meinproc4
%_kde_bindir/meinproc4_simple
%_kde_bindir/nepomuk-rcgen
%_kde_bindir/preparetips
%dir %_kde_libdir/kde4
%_kde_libdir/kde4/*.so
%dir %_kde_libdir/kde4/libexec
%_kde_libdir/kde4/libexec/*
%attr(4755,root,root) %_kde_libdir/kde4/libexec/fileshareset
%dir  %_kde_libdir/kde4/plugins
%_kde_libdir/kde4/plugins/imageformats
%_kde_libdir/kde4/plugins/kauth
%_kde_libdir/kde4/plugins/script
%_kde_libdir/libkdeinit4_*
%_kde_datadir/config
%_kde_datadir/mime/*
%_kde_datadir/kde4
%_kde_applicationsdir/kmailservice.desktop
%_kde_applicationsdir/ktelnetservice.desktop
%_kde_appsdir/proxyscout
%_kde_appsdir/LICENSES
%_kde_appsdir/ktexteditor_kdatatool
%_kde_appsdir/ktexteditor_insertfile
%_kde_appsdir/ktexteditor_exporter
%_kde_appsdir/ktexteditor_iconinserter
%_kde_appsdir/ktexteditor_insanehtml_le
%_kde_appsdir/kssl
%_kde_appsdir/ksgmltools2
%_kde_appsdir/knewstuff
%_kde_appsdir/kjava
%_kde_appsdir/khtml 
%_kde_appsdir/kdewidgets
%_kde_appsdir/kdeui
%_kde_appsdir/kconf_update
%_kde_appsdir/kcm_componentchooser
%_kde_appsdir/katepart
%_kde_appsdir/kcharselect
%_kde_docdir/HTML/en/sonnet
%_kde_docdir/HTML/en/common/*
%_kde_docdir/HTML/en/kioslave/data
%_kde_docdir/HTML/en/kioslave/file
%_kde_docdir/HTML/en/kioslave/ftp
%_kde_docdir/HTML/en/kioslave/help
%_kde_docdir/HTML/en/kioslave/http
%_kde_docdir/HTML/en/kioslave/mailto
%_kde_docdir/HTML/en/kioslave/rlogin
%_kde_docdir/HTML/en/kioslave/telnet
%_kde_docdir/HTML/en/kioslave/webdav
%_kde_mandir/man1/kde4-config.1*
%_kde_mandir/man1/makekdewidgets.1*
%_kde_mandir/man7/kdeoptions.7*
%_kde_mandir/man7/qtoptions.7*
%_kde_mandir/man8/kbuildsycoca4.8*
%_kde_mandir/man8/kcookiejar4.8*
%_kde_mandir/man8/kdeinit4.8*
%_kde_mandir/man8/meinproc4.8*
%_kde_mandir/man1/kjs.1.*
%_kde_mandir/man1/kjscmd.1.*
%_kde_mandir/man1/kross.1.*
%_kde_mandir/man8/kded4.8.*
%_kde_datadir/icons
%_kde_datadir/locale/all_languages
%_sysconfdir/dbus-1/system.d/org.kde.auth.conf
%_kde_sysconfdir/xdg/kde4/menus/applications.menu
%_kde_appsdir/kauth
%_kde_appsdir/plasma
%_kde_datadir/locale/en_US/entry.desktop

#--------------------------------------------------------------

%if %{compile_apidox}
%package apidoc
Group: Development/KDE and Qt
Summary: Development documentation for %name
Requires: qt4-doc

%description apidoc
This packages contains all development documentation for kdelibs

%files apidoc
%_docdir/kde4/api/*
%endif

#--------------------------------------------------------------

%prep
%if %branch
%setup -q -n kdelibs-%version%kde_snapshot
%else
%setup -q -n kdelibs-%version
%endif

%if %experimental
tar xjvf %SOURCE1
%if %branch
  mv kdelibs-experimental-%version%kde_snapshot experimental
%else
  mv kdelibs-experimental-%version experimental
%endif
%endif
%patch1 -p0
%patch2 -p0
%if ! %with_drkonqi
%patch3 -p0
%endif
%patch200 -p1 -b .nepomuk_trunk
%patch201 -p1
%patch202 -p1
%patch203 -p1

%build
%cmake_kde4
%make

%if %{compile_apidox}
  cd ..
  doc/api/doxygen.sh --doxdatadir=${PWD}/doc/common .
%endif

%install
%makeinstall_std -C build

%if %{compile_apidox}
  mkdir -p %buildroot/%_docdir/kde4/api
  cp -av kdelibs-%version-apidocs %buildroot/%_docdir/kde4/api/kdelibs
%endif 

%__rm -fr %buildroot%_kde_appsdir/kssl/ca-bundle.crt
ln -snf %_sysconfdir/pki/tls/certs/ca-bundle.crt %buildroot%_kde_appsdir/kssl/ca-bundle.crt

