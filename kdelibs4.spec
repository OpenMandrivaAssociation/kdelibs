%define branch 0
%{?_branch: %{expand: %%global branch 1}}

%define experimental 0
%{?_experimental: %{expand: %%global experimental 1}}

%define compile_apidox 0
%{?_with_apidox: %{expand: %%global compile_apidox 1}}

%define bootstrap 0
%{?_without_bootstrap: %global bootstrap 0}
%{?_with_bootstrap: %global bootstrap 1}

%define epoch_kdelibs3 30000000

%if %branch
%define kde_snapshot svn1053190
%endif

Name: kdelibs4
Summary: K Desktop Environment - Libraries
Version: 4.3.90
Release: %mkrel 1
Epoch:   2
Group: Graphical desktop/KDE
License: ARTISTIC BSD GPL_V2 LGPL_V2 QPL_V1.0
BuildRoot: %_tmppath/%name-%version-%release-root
URL:     http://www.kde.org
%if %branch
Source:  ftp://ftp.kde.org/pub/kde/stable/%version/src/kdelibs-%version%kde_snapshot.tar.bz2
%if %experimental
Source1: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdelibs-experimental-%version%kde_snapshot.tar.bz2
%endif
%else
Source:  ftp://ftp.kde.org/pub/kde/stable/%version/src/kdelibs-%version.tar.bz2
%if %experimental
Source1: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdelibs-experimental-%version.tar.bz2
%endif
%endif
Patch0: kdelibs-4.3.85-add-extra-catalogs.patch
Patch1: kdelibs-4.1.81-overrides-oxygen-iaora.patch
Patch2: kdelibs-4.1.85-add-kde-menu.patch 
Patch4: kdelibs-4.2.85-fix_konqueror_crash_on_big_tables.patch 
Patch5: kdelibs-4.3.75-mandriva-about.patch
Patch6: kdelibs-4.2.95-runtime-qt-locale-initialized.patch
Patch7: kdelibs-4.2.95-fix-kross-lib.patch
Patch8: kdelibs-4.3.85-use-timeline.patch
#official backports
#Testing
Patch301: kdelibs-testing-mdv47378.patch
BuildRequires: kde4-macros >= 4.1.71
BuildRequires: qt4-devel >= 4:4.6.0-0.beta1.1
BuildRequires: qt4-qtdbus
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
BuildRequires: strigi-devel >=  0.5.9
BuildRequires: shared-mime-info
BuildRequires: soprano-devel >= 2.0.98
BuildRequires: automoc
BuildRequires: phonon-devel >= 4.2
BuildRequires: xpm-devel
BuildRequires: xft2-devel
BuildRequires: libxml2-utils
BuildRequires: liblzma-devel
BuildRequires: libutempter-devel
BuildRequires: rootcerts
BuildRequires: flex
BuildRequires: bison
BuildRequires: qca2-devel
BuildRequires: polkit-qt-devel 
BuildRequires: shared-desktop-ontologies-devel
BuildRequires: attica-devel
BuildRequires: libxscrnsaver-devel

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
%defattr(-,root,root)
%_kde_libdir/libkde3support.so.%{kde3support_major}*

#------------------------------------------------	

%define kdecore_major 5
%define libkdecore %mklibname kdecore %kdecore_major

%package -n %libkdecore
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdecore5 >= %{epoch_kdelibs3}:3.80.3
Requires: phonon-backend >= 4.2.0
%if !%{bootstrap}
Requires: kde4-config-file 
Requires: kde4-l10n
Requires: qt4-style-iaora
Requires: kde4-style-iaora
%endif
Requires: kdelibs4-core = %epoch:%{version}

%description -n %libkdecore
KDE 4 core library.

%files -n %libkdecore
%defattr(-,root,root)
%_kde_libdir/libkdecore.so.%{kdecore_major}*

#------------------------------------------------	

%define kdefakes_major 5
%define libkdefakes %mklibname kdefakes %kdefakes_major

%package -n %libkdefakes
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= %{epoch_kdelibs3}:3.80.3
 

%description -n %libkdefakes
KDE 4 core library.

%files -n %libkdefakes
%defattr(-,root,root)
%_kde_libdir/libkdefakes.so.%{kdefakes_major}*

#------------------------------------------------	

%define kdesu_major 5
%define libkdesu %mklibname kdesu %kdesu_major

%package -n %libkdesu
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= %{epoch_kdelibs3}:3.80.3 

%description -n %libkdesu
KDE 4 core library.

%files -n %libkdesu
%defattr(-,root,root)
%_kde_libdir/libkdesu.so.%{kdesu_major}*

#------------------------------------------------	

%define kdeui_major 5
%define libkdeui %mklibname kdeui %kdeui_major

%package -n %libkdeui
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= %{epoch_kdelibs3}:3.80.3
 

%description -n %libkdeui
KDE 4 core library.

%files -n %libkdeui
%defattr(-,root,root)
%_kde_libdir/libkdeui.so.%{kdeui_major}*

#------------------------------------------------	

%define kdnssd_major 4
%define libkdnssd %mklibname kdnssd %kdnssd_major

%package -n %libkdnssd
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= %{epoch_kdelibs3}:3.80.3
Obsoletes: %{_lib}kdnssd5 < 3.93.0-0.714006.1
 

%description -n %libkdnssd
KDE 4 core library.

%files -n %libkdnssd
%defattr(-,root,root)
%_kde_libdir/libkdnssd.so.%{kdnssd_major}*

#------------------------------------------------	

%define kfile_major 4
%define libkfile %mklibname kfile %kfile_major

%package -n %libkfile
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= %{epoch_kdelibs3}:3.80.3
Obsoletes: %{_lib}kfile5 < 3.93.0-0.714006.1
 

%description -n %libkfile
KDE 4 core library.

%files -n %libkfile
%defattr(-,root,root)
%_kde_libdir/libkfile.so.%{kfile_major}*

#------------------------------------------------	

%define khtml_major 5
%define libkhtml %mklibname khtml %khtml_major

%package -n %libkhtml
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= %{epoch_kdelibs3}:3.80.3
 

%description -n %libkhtml
KDE 4 core library.

%files -n %libkhtml
%defattr(-,root,root)
%_kde_libdir/libkhtml.so.%{khtml_major}*

#------------------------------------------------	

%define kimproxy_major 4
%define libkimproxy %mklibname kimproxy %kimproxy_major

%package -n %libkimproxy
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= %{epoch_kdelibs3}:3.80.3
Obsoletes: %{_lib}kimproxy5 < 3.93.0-0.714006.1
 

%description -n %libkimproxy
KDE 4 core library.

%files -n %libkimproxy
%defattr(-,root,root)
%_kde_libdir/libkimproxy.so.%{kimproxy_major}*

#------------------------------------------------	

%define kio_major 5
%define libkio %mklibname kio %kio_major

%package -n %libkio
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= %{epoch_kdelibs3}:3.80.3
 

%description -n %libkio
KDE 4 core library.

%files -n %libkio
%defattr(-,root,root)
%_kde_libdir/libkio.so.%{kio_major}*

#------------------------------------------------	

%define kjsembed_major 4
%define libkjsembed %mklibname kjsembed %kjsembed_major

%package -n %libkjsembed
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= %{epoch_kdelibs3}:3.80.3
Obsoletes: %{_lib}kjsembed5 < 3.93.0-0.714006.1
%if %mdkversion >= 201000
Obsoletes: kde3-kjsembed < 1:3.5.10-4
Obsoletes: kjsembed < 1:3.5.10-4
%endif
%description -n %libkjsembed
KDE 4 core library.

%files -n %libkjsembed
%defattr(-,root,root)
%_kde_libdir/libkjsembed.so.%{kjsembed_major}*

#------------------------------------------------	

%define kjs_major 4
%define libkjs %mklibname kjs %kjs_major

%package -n %libkjs
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= %{epoch_kdelibs3}:3.80.3
Obsoletes: %{_lib}kjs5 < 3.93.0-0.714006.1
 

%description -n %libkjs
KDE 4 core library.

%files -n %libkjs
%defattr(-,root,root)
%_kde_libdir/libkjs.so.%{kjs_major}*

#------------------------------------------------	

%define kmediaplayer_major 4
%define libkmediaplayer %mklibname kmediaplayer %kmediaplayer_major

%package -n %libkmediaplayer
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= %{epoch_kdelibs3}:3.80.3
Obsoletes: %{_lib}kmediaplayer5 < 3.93.0-0.714006.1
 

%description -n %libkmediaplayer
KDE 4 core library.

%files -n %libkmediaplayer
%defattr(-,root,root)
%_kde_libdir/libkmediaplayer.so.%{kmediaplayer_major}*

#------------------------------------------------	

%define nepomuk_major 4
%define libnepomuk %mklibname nepomuk %nepomuk_major

%package -n %libnepomuk
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= %{epoch_kdelibs3}:3.80.3
Obsoletes: %{_lib}knepomuk5 < 3.93.0-0.714006.1
Obsoletes: %{_lib}nepomuk5 < 3.93.0-0.714006.1
Obsoletes: %{_lib}kmetadata5 < 3.93.0-0.714006.1
Obsoletes: %{_lib}konto5 < 3.93.0-0.714006.1
Obsoletes: %{_lib}nepomukmiddleware4 < 3.93.0-0.725600.1 
Obsoletes: %{_lib}nepomuk-middleware4 < 3.93.0-0.725600.1

%description -n %libnepomuk
KDE 4 core library.

%files -n %libnepomuk
%defattr(-,root,root)
%_kde_libdir/libnepomuk.so.%{nepomuk_major}*

#------------------------------------------------	

%define knewstuff2_major 4
%define libknewstuff2 %mklibname knewstuff2_ %knewstuff2_major

%package -n %libknewstuff2
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= %{epoch_kdelibs3}:3.80.3
Obsoletes: %{_lib}knewstuff25
Obsoletes: %{_lib}knewstuff24 

%description -n %libknewstuff2
KDE 4 core library.

%files -n %libknewstuff2
%defattr(-,root,root)
%_kde_libdir/libknewstuff2.so.%{knewstuff2_major}*

#------------------------------------------------	

%define knotifyconfig_major 4
%define libknotifyconfig %mklibname knotifyconfig %knotifyconfig_major

%package -n %libknotifyconfig
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= %{epoch_kdelibs3}:3.80.3
Obsoletes: %{_lib}knotifyconfig5 < 3.93.0-0.714006.1
 

%description -n %libknotifyconfig
KDE 4 core library.

%files -n %libknotifyconfig
%defattr(-,root,root)
%_kde_libdir/libknotifyconfig.so.%{knotifyconfig_major}*

#------------------------------------------------	

%define kntlm_major 4
%define libkntlm %mklibname kntlm %kntlm_major

%package -n %libkntlm
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= %{epoch_kdelibs3}:3.80.3
Obsoletes: %{_lib}kntlm5 < 3.93.0-0.714006.1
 

%description -n %libkntlm
KDE 4 core library.

%files -n %libkntlm
%defattr(-,root,root)
%_kde_libdir/libkntlm.so.%{kntlm_major}*

#------------------------------------------------	

%define kparts_major 4
%define libkparts %mklibname kparts %kparts_major

%package -n %libkparts
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= %{epoch_kdelibs3}:3.80.3
Obsoletes: %{_lib}kparts5 < 3.93.0-0.714006.1
 

%description -n %libkparts
KDE 4 core library.

%files -n %libkparts
%defattr(-,root,root)
%_kde_libdir/libkparts.so.%{kparts_major}*

#------------------------------------------------	

%define krosscore_major 4
%define libkrosscore %mklibname krosscore %krosscore_major

%package -n %libkrosscore
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= %{epoch_kdelibs3}:3.80.3
Obsoletes: %{_lib}krosscore5 < 3.93.0-0.714006.1
 

%description -n %libkrosscore
KDE 4 core library.

%files -n %libkrosscore
%defattr(-,root,root)
%_kde_libdir/libkrosscore.so.%{krosscore_major}*

#------------------------------------------------	

%define krossui_major 4
%define libkrossui %mklibname krossui %krossui_major

%package -n %libkrossui
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= %{epoch_kdelibs3}:3.80.3
Obsoletes: %{_lib}krossui5 < 3.93.0-0.714006.1
 

%description -n %libkrossui
KDE 4 core library.

%files -n %libkrossui
%defattr(-,root,root)
%_kde_libdir/libkrossui.so.%{krossui_major}*

#------------------------------------------------	

%define ktexteditor_major 4
%define libktexteditor %mklibname ktexteditor %ktexteditor_major

%package -n %libktexteditor
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= %{epoch_kdelibs3}:3.80.3
Obsoletes: %{_lib}ktexteditor5 < 3.93.0-0.714006.1
 

%description -n %libktexteditor
KDE 4 core library.

%files -n %libktexteditor
%defattr(-,root,root)
%_kde_libdir/libktexteditor.so.%{ktexteditor_major}*

#------------------------------------------------	

%define kunittest_major 4
%define libkunittest %mklibname kunittest %kunittest_major

%package -n %libkunittest
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= %{epoch_kdelibs3}:3.80.3
Obsoletes: %{_lib}kunittest5 < 3.93.0-0.714006.1
 

%description -n %libkunittest
KDE 4 core library.

%files -n %libkunittest
%defattr(-,root,root)
%_kde_libdir/libkunittest.so.%{kunittest_major}*

#------------------------------------------------	

%define kutils_major 4
%define libkutils %mklibname kutils %kutils_major

%package -n %libkutils
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= %{epoch_kdelibs3}:3.80.3
Obsoletes: %{_lib}kutils5 < 3.93.0-0.714006.1
 

%description -n %libkutils
KDE 4 core library.

%files -n %libkutils
%defattr(-,root,root)
%_kde_libdir/libkutils.so.%{kutils_major}*

#------------------------------------------------	

%define solid_major 4
%define libsolid %mklibname solid %solid_major

%package -n %libsolid
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= %{epoch_kdelibs3}:3.80.3
Obsoletes: %{_lib}solid5 < 3.93.0-0.714006.1
 

%description -n %libsolid
KDE 4 core library.

%files -n %libsolid
%defattr(-,root,root)
%_kde_libdir/libsolid.so.%{solid_major}*

#------------------------------------------------

%define threadweaver_major 4
%define libthreadweaver %mklibname threadweaver %threadweaver_major

%package -n %libthreadweaver
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= %{epoch_kdelibs3}:3.80.3
Obsoletes: %{_lib}threadweaver5 < 3.93.0-0.714006.1
 

%description -n %libthreadweaver
KDE 4 core library.

%files -n %libthreadweaver
%defattr(-,root,root)
%_kde_libdir/libthreadweaver.so.%{threadweaver_major}*

#------------------------------------------------

%define  kpty_major 4
%define  libkpty %mklibname kpty %kpty_major

%package -n %libkpty
Summary: KDE 4 core library
Group: System/Libraries
 

%description -n %libkpty
KDE 4 core library.

%files -n %libkpty
%defattr(-,root,root)
%_kde_libdir/libkpty.so.%{kpty_major}*

#------------------------------------------------

%define  kjsapi_major 4
%define  libkjsapi %mklibname kjsapi %kjsapi_major

%package -n %libkjsapi
Summary: KDE 4 core library
Group: System/Libraries


%description -n %libkjsapi
KDE 4 core library.

%files -n %libkjsapi
%defattr(-,root,root)
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
%defattr(-,root,root)
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
%defattr(-,root,root)
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
%defattr(-,root,root)
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
%defattr(-,root,root)
%_kde_libdir/libkdewebkit.so.%{libkdewebkit_major}*


#------------------------------------------------

%define libknewstuff3_major 4
%define libknewstuff3 %mklibname knewstuff3 %{libknewstuff3_major}

%package -n %libknewstuff3
Summary: KDE 4 library
Group: System/Libraries

%description -n %libknewstuff3
KDE 4 library.

%files -n %libknewstuff3
%defattr(-,root,root)
%_kde_libdir/libknewstuff3.so.%{libknewstuff3_major}*

#------------------------------------------------

%package devel
Group: Development/KDE and Qt
Summary: Header files and documentation for compiling KDE applications
Requires: kde4-macros
Requires: automoc4
Requires: acl-devel
Requires: qt4-devel >= 4:4.6.0
Requires: qt4-qtdbus
Requires: kdelibs4-core = %epoch:%version
Requires: automoc
Requires: soprano-devel
Requires: strigi-devel
# add requires on libxml2-utils, as when building most kde applications,
# it will call xmllint to validate the docbook files:
Requires: libxml2-utils
Requires: aspell-devel
Requires: hspell-devel
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
Requires: strigi-devel >=  0.5.9
Requires: shared-mime-info
Requires: soprano-devel >= 2.0.98
Requires: automoc
Requires: xpm-devel
Requires: xft2-devel
Requires: shared-desktop-ontologies-devel
Provides: plasma-devel = %epoch:%version
Requires: %libkde3support = %epoch:%version
Requires: %libkdecore = %epoch:%version
Requires: %libkdefakes = %epoch:%version
Requires: %libkdesu = %epoch:%version
Requires: %libkdeui = %epoch:%version
Requires: %libkdnssd = %epoch:%version
Requires: %libkfile = %epoch:%version
Requires: %libkhtml = %epoch:%version
Requires: %libkimproxy = %epoch:%version
Requires: %libkio = %epoch:%version
Requires: %libkjsembed = %epoch:%version
Requires: %libkjs = %epoch:%version
Requires: %libkmediaplayer = %epoch:%version
Requires: %libnepomuk = %epoch:%version
Requires: %libknewstuff2 = %epoch:%version
Requires: %libknotifyconfig = %epoch:%version
Requires: %libkntlm = %epoch:%version
Requires: %libkparts = %epoch:%version
Requires: %libkrosscore = %epoch:%version
Requires: %libkrossui = %epoch:%version
Requires: %libktexteditor = %epoch:%version
Requires: %libkunittest = %epoch:%version
Requires: %libkutils = %epoch:%version
Requires: %libsolid = %epoch:%version
Requires: %libthreadweaver = %epoch:%version
Requires: %libkpty = %epoch:%version
Requires: %libkjsapi = %epoch:%version
Requires: %libplasma = %epoch:%version
Requires: %libkunitconversion = %epoch:%version
Requires: %libkdewebkit = %epoch:%version
Requires: %libnepomukquery = %epoch:%version
Requires: %libknewstuff3 = %epoch:%version
Obsoletes: %{_lib}kdecore5-devel < 3.93.0-0.714006.1
Obsoletes: kdelibs4-experimental-devel < 2:4.3.73-1 
Provides:  kdelibs4-experimental-devel = %epoch:%version
Conflicts: kdelibs4-core < 4.2.95-3
Conflicts: koffice-devel < 11:1.9.95.9-2mdv
Conflicts: kdebase4-workspace-devel < 2:4.3.75-1
Conflicts: kdebase4-runtime <= 1:4.2.4
Conflicts: webkitkde-devel < 0.0-0.1050148.3

%description devel
This package includes the header files you will need to compile applications 
for KDE. Also included is the KDE API documentation in HTML format for easy 
browsing.

%files devel
%defattr(-,root,root,-)
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
%_kde_libdir/kde4/plugins/designer
%_kde_bindir/checkXML
%_kde_mandir/man1/checkXML.1*
%_kde_bindir/kconfig_compiler
%exclude %_kde_libdir/libkdeinit4_*

#--------------------------------------------------------------
%package    core
Group:      Graphical desktop/KDE
Summary:    KDE 4 system core files
Suggests:   enchant-dictionary
Suggests:   xdg-utils
Obsoletes:  kdelibs4-common < 3.93.0-0.714006.1
Conflicts:  kdelibs4-devel < 2:4.2.85-4
%if %mdkversion >= 200910
Obsoletes:  kdelibs-common < %{epoch_kdelibs3}:3.5.10-6
%endif
%if %mdkversion >= 201000
Obsoletes:  kdelibs3-common < %{epoch_kdelibs3}:3.5.10-12
%endif
Requires:   shared-mime-info
Conflicts:  kdebase4-workspace < 2:4.1.73-1
Requires:   rootcerts
Requires:   shared-desktop-ontologies
Obsoletes:  lilypond-kde4 < 0.2-3
%description core
KDE 4 system core files.

%files core
%defattr(-,root,root,-)
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
%_kde_bindir/nepomuk-rcgen
%_kde_bindir/preparetips
%dir %_kde_libdir/kde4
%_kde_libdir/kde4/*
%attr(4755,root,root) %_kde_libdir/kde4/libexec/fileshareset
%_kde_libdir/libkdeinit4_*
%_kde_datadir/config
%_kde_datadir/mime/*
%_kde_datadir/kde4
%_kde_appsdir/proxyscout
%_kde_appsdir/nepomuk
%_kde_appsdir/LICENSES
%_kde_appsdir/ktexteditor_kdatatool
%_kde_appsdir/ktexteditor_insertfile
%_kde_appsdir/ktexteditor_exporter
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
%_sysconfdir/dbus-1/system.d/org.kde.kcontrol.kcmremotewidgets.conf
%_kde_sysconfdir/xdg/kde4/menus/applications.menu
%_kde_datadir/PolicyKit/policy/org.kde.kcontrol.kcmremotewidgets.policy
%_kde_appsdir/kauth
%_kde_appsdir/plasma

# Devel stuff 0 included in kdelibs4-devel
%exclude %_kde_appsdir/cmake/modules/*
%exclude %_kde_libdir/kde4/plugins/designer

#--------------------------------------------------------------

%if %{compile_apidox}
%package apidoc
Group: Development/KDE and Qt
Summary: Development documentation for %name
Requires: qt4-doc
Obsoletes: kdelibs4-apidoc < 3.93.0-0.714006.1

%description apidoc
This packages contains all development documentation for kdelibs

%files apidoc
%defattr(-,root,root,-)
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

%patch0 -p0 -b .extra_catalogs
%patch1 -p0 -b .iaora
%patch2 -p0
%patch4 -p1 -b .konqueror_big_page
%patch5 -p0 -b .about
%patch6 -p0 -b .qt44_45
# Need to be added again ? ( need to be checked )
#%patch7 -p1
%patch8 -p0

%patch301 -p1

%build
%cmake_kde4 -DKDE4_ENABLE_FINAL=ON
%make

%if %{compile_apidox}
    cd ..
    doc/api/doxygen.sh --doxdatadir=${PWD}/doc/common .
%endif

%install
rm -fr %buildroot

make -C build DESTDIR=%buildroot install

%if %{compile_apidox}
   mkdir -p %buildroot/%_docdir/kde4/api
   cp -av kdelibs-%version-apidocs %buildroot/%_docdir/kde4/api/kdelibs
%endif 

%__rm -fr %buildroot%_kde_appsdir/kssl/ca-bundle.crt
ln -snf %_sysconfdir/pki/tls/certs/ca-bundle.crt %buildroot%_kde_appsdir/kssl/ca-bundle.crt

%clean
rm -fr %buildroot
