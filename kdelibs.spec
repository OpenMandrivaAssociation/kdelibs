%define bootstrap 0
%{?_branch: %{expand: %%global bootstrap 1}}

%define compile_apidox 0
%{?_with_apidox: %{expand: %%global compile_apidox 1}}

%define with_drkonqi 0
%{?_with_drkonqi: %{expand: %%global with_drkonqi 1}}

%define udisk_backend 1

# exclude libkactivities or not
%define no_libkactivities 1

%define build_nepomuk 0
%define major_ver 16.08.3

Summary:	K Desktop Environment - Libraries
Name:		kdelibs
Version:	4.14.28
Release:	1
Epoch:		5
Group:		Graphical desktop/KDE
License:	ARTISTIC BSD GPLv2+ LGPLv2+ QPLv1.0
Url:		http://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/stable/applications/%{major_ver}/src/%{name}-%{version}.tar.xz
Source100:	%{name}.rpmlintrc
Patch1:		kdelibs-4.1.85-add-kde-menu.patch
Patch2:		kdelibs-4.5.80-usr-abrt-instead-of-drkonqi.patch
Patch3:		kdelibs-4.7.1-fix-cmakelist-to-use-pthread.patch
Patch4:		kdelibs-4.14.26-openssl-1.1.patch
Patch5:		kdelibs-4.14.26-compile.patch
# Battery reporting support for KDE Connect from
# http://albertvaka.wordpress.com/2013/08/05/introducing-kde-connect/
Patch10:	kdelibs-4.11.1-phonepower.patch
# Revert upsteam commit because it leads to incorrect icons on desktop
# For example, application shortcuts are displayed with x-desktop mimetype icon
Patch11:	kdelibs-4.11.2-delayed-icons.patch
# Revert upstream commit because it leads to ugly empty dialog popup when
# adding new empty panel or RocketBar
Patch12:	kdelibs-4.11.2-containment-config.patch
Patch13:	kdelibs-4.14.3-docbook-dtd45.patch
Patch100:	kdelibs-4.8.0-plasma.patch
Patch200:	kdelibs-4.8.1-add-extra-catalogs.patch
Patch203:	kdelibs-4.8.95-fileplaces.patch
Patch204:	kdelibs-4.8.1-kfile-knewfilemenu-removed-LinkToDevice.patch
Patch206:	kdelibs-4.8.3-kfile-klook.patch
Patch207:	kdelibs4-4.9.3-iconwidget-revert-commit-c6160d14.patch
Patch208:	kdelibs-4.9.3-kio-ftp.patch
# Don't use HEAD to get mimetype. Sometimes servers don't return mimetype
# with it for webdav. It's also wrong for directories - HEAD will return
# text/xml (since it's actually file listing in XML)
Patch209:	kdelibs-4.12.4-improve-mimetype-detection-for-webdav.patch
Patch210:	kdelibs-4.12.2-armlinking.patch
Patch211:	kdelibs-4.13.2-kdecmake.patch
### FIXME workaround for what seems to be a clang bug
Patch220:	kdelibs-4.14.11-no-lto-for-khtml.patch
BuildRequires:	automoc
BuildRequires:	bison
BuildRequires:	docbook-dtd45-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	flex
BuildRequires:	kde4-macros >= 4.1.71
BuildRequires:	libxml2-utils
BuildRequires:	rootcerts
BuildRequires:	shared-mime-info
BuildRequires:	xsltproc
BuildRequires:	acl-devel
BuildRequires:	aspell-devel
BuildRequires:	bzip2-devel
BuildRequires:	cups-devel >= 1.2
BuildRequires:	gdbm-devel
BuildRequires:	grantlee-devel
BuildRequires:	hspell-devel
BuildRequires:	krb5-devel
BuildRequires:	utempter-devel
BuildRequires:	pam-devel
BuildRequires:	pcre-devel
BuildRequires:	polkit-qt-1-devel >= 0.98.1
BuildRequires:	sasl-devel
BuildRequires:	tiff-devel
BuildRequires:	ungif-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(avahi-compat-libdns_sd)
BuildRequires:	pkgconfig(avahi-client)
BuildRequires:	pkgconfig(dbusmenu-qt)
BuildRequires:	pkgconfig(enchant)
BuildRequires:	pkgconfig(gamin)
BuildRequires:	pkgconfig(jasper)
BuildRequires:	pkgconfig(libart-2.0)
BuildRequires:	pkgconfig(libattica)
BuildRequires:	pkgconfig(liblzma)
BuildRequires:	pkgconfig(libstreams) >= 0.6.3
BuildRequires:	pkgconfig(libxml-2.0) >= 2.4.11
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(mad)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(OpenEXR)
BuildRequires:	pkgconfig(icu-i18n)
%if %{build_nepomuk}
BuildRequires:	pkgconfig(soprano) > 2.7.57
%else
BuildConflicts:	pkgconfig(soprano)
%endif
BuildRequires:	pkgconfig(phonon)
BuildRequires:	pkgconfig(qca2)
BuildRequires:	pkgconfig(shared-desktop-ontologies)
BuildRequires:	pkgconfig(QtCore)
BuildRequires:	pkgconfig(QtDBus)
BuildRequires:	pkgconfig(QtWebKit)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(xft)
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xscrnsaver)
BuildRequires:	pkgconfig(xpm)
%if %{udisk_backend}
BuildRequires:	pkgconfig(udev)
%endif
#Optional, but let's build support for what we can
BuildRequires:	hupnp-devel
BuildRequires:	media-player-info

%description
Libraries for the K Desktop Environment.

#--------------------------------------------------------------------

%define kde3support_major 4
%define libkde3support %mklibname kde3support %{kde3support_major}

%package -n %{libkde3support}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkde3support}
KDE 4 core library.

%files -n %{libkde3support}
%{_kde_libdir}/libkde3support.so.%{kde3support_major}*

#--------------------------------------------------------------------

%define kdecore_major 5
%define libkdecore %mklibname kdecore %{kdecore_major}

%package -n %{libkdecore}
Summary:	KDE 4 core library
Group:		System/Libraries
Requires:	phonon-backend >= 4.2.0
%if ! %{bootstrap}
Suggests:	kde-l10n
%endif
Requires:	kdelibs-core = %{EVRD}

%description -n %{libkdecore}
KDE 4 core library.

%files -n %{libkdecore}
%{_kde_libdir}/libkdecore.so.%{kdecore_major}*

#--------------------------------------------------------------------

%define kdefakes_major 5
%define libkdefakes %mklibname kdefakes %{kdefakes_major}

%package -n %{libkdefakes}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkdefakes}
KDE 4 core library.

%files -n %{libkdefakes}
%{_kde_libdir}/libkdefakes.so.%{kdefakes_major}*

#--------------------------------------------------------------------

%define kdesu_major 5
%define libkdesu %mklibname kdesu %{kdesu_major}

%package -n %{libkdesu}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkdesu}
KDE 4 core library.

%files -n %{libkdesu}
%{_kde_libdir}/libkdesu.so.%{kdesu_major}*

#--------------------------------------------------------------------

%define kdeui_major 5
%define libkdeui %mklibname kdeui %{kdeui_major}

%package -n %{libkdeui}
Summary:	KDE 4 core library
Group:		System/Libraries
Requires:	dbus-x11

%description -n %{libkdeui}
KDE 4 core library.

%files -n %{libkdeui}
%{_kde_libdir}/libkdeui.so.%{kdeui_major}*

#--------------------------------------------------------------------

%define kdnssd_major 4
%define libkdnssd %mklibname kdnssd %{kdnssd_major}

%package -n %{libkdnssd}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkdnssd}
KDE 4 core library.

%files -n %{libkdnssd}
%{_kde_libdir}/libkdnssd.so.%{kdnssd_major}*

#--------------------------------------------------------------------

%define kfile_major 4
%define libkfile %mklibname kfile %{kfile_major}

%package -n %{libkfile}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkfile}
KDE 4 core library.

%files -n %{libkfile}
%{_kde_libdir}/libkfile.so.%{kfile_major}*

#--------------------------------------------------------------------

%define khtml_major 5
%define libkhtml %mklibname khtml %{khtml_major}

%package -n %{libkhtml}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkhtml}
KDE 4 core library.

%files -n %{libkhtml}
%{_kde_libdir}/libkhtml.so.%{khtml_major}*

#--------------------------------------------------------------------

%define kimproxy_major 4
%define libkimproxy %mklibname kimproxy %{kimproxy_major}

%package -n %{libkimproxy}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkimproxy}
KDE 4 core library.

%files -n %{libkimproxy}
%{_kde_libdir}/libkimproxy.so.%{kimproxy_major}*

#--------------------------------------------------------------------

%define kio_major 5
%define libkio %mklibname kio %{kio_major}

%package -n %{libkio}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkio}
KDE 4 core library.

%files -n %{libkio}
%{_kde_libdir}/libkio.so.%{kio_major}*

#--------------------------------------------------------------------

%define kjsembed_major 4
%define libkjsembed %mklibname kjsembed %{kjsembed_major}

%package -n %{libkjsembed}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkjsembed}
KDE 4 core library.

%files -n %{libkjsembed}
%{_kde_libdir}/libkjsembed.so.%{kjsembed_major}*

#--------------------------------------------------------------------

%define kjs_major 4
%define libkjs %mklibname kjs %{kjs_major}

%package -n %{libkjs}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkjs}
KDE 4 core library.

%files -n %{libkjs}
%{_kde_libdir}/libkjs.so.%{kjs_major}*

#--------------------------------------------------------------------

%define kmediaplayer_major 4
%define libkmediaplayer %mklibname kmediaplayer %{kmediaplayer_major}

%package -n %{libkmediaplayer}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkmediaplayer}
KDE 4 core library.

%files -n %{libkmediaplayer}
%{_kde_libdir}/libkmediaplayer.so.%{kmediaplayer_major}*

#--------------------------------------------------------------------

%define knewstuff2_major 4
%define libknewstuff2 %mklibname knewstuff2_ %{knewstuff2_major}

%package -n %{libknewstuff2}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libknewstuff2}
KDE 4 core library.

%files -n %{libknewstuff2}
%{_kde_libdir}/libknewstuff2.so.%{knewstuff2_major}*

#--------------------------------------------------------------------

%define knotifyconfig_major 4
%define libknotifyconfig %mklibname knotifyconfig %{knotifyconfig_major}

%package -n %{libknotifyconfig}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libknotifyconfig}
KDE 4 core library.

%files -n %{libknotifyconfig}
%{_kde_libdir}/libknotifyconfig.so.%{knotifyconfig_major}*

#--------------------------------------------------------------------

%define kntlm_major 4
%define libkntlm %mklibname kntlm %{kntlm_major}

%package -n %{libkntlm}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkntlm}
KDE 4 core library.

%files -n %{libkntlm}
%{_kde_libdir}/libkntlm.so.%{kntlm_major}*

#--------------------------------------------------------------------

%define kparts_major 4
%define libkparts %mklibname kparts %{kparts_major}

%package -n %{libkparts}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkparts}
KDE 4 core library.

%files -n %{libkparts}
%{_kde_libdir}/libkparts.so.%{kparts_major}*

#--------------------------------------------------------------------

%define krosscore_major 4
%define libkrosscore %mklibname krosscore %{krosscore_major}

%package -n %{libkrosscore}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkrosscore}
KDE 4 core library.

%files -n %{libkrosscore}
%{_kde_libdir}/libkrosscore.so.%{krosscore_major}*

#--------------------------------------------------------------------

%define krossui_major 4
%define libkrossui %mklibname krossui %{krossui_major}

%package -n %{libkrossui}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkrossui}
KDE 4 core library.

%files -n %{libkrossui}
%{_kde_libdir}/libkrossui.so.%{krossui_major}*

#--------------------------------------------------------------------

%define ktexteditor_major 4
%define libktexteditor %mklibname ktexteditor %{ktexteditor_major}

%package -n %{libktexteditor}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libktexteditor}
KDE 4 core library.

%files -n %{libktexteditor}
%{_kde_libdir}/libktexteditor.so.%{ktexteditor_major}*

#--------------------------------------------------------------------

%define kunittest_major 4
%define libkunittest %mklibname kunittest %{kunittest_major}

%package -n %{libkunittest}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkunittest}
KDE 4 core library.

%files -n %{libkunittest}
%{_kde_libdir}/libkunittest.so.%{kunittest_major}*

#--------------------------------------------------------------------

%define kutils_major 4
%define libkutils %mklibname kutils %{kutils_major}

%package -n %{libkutils}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkutils}
KDE 4 core library.

%files -n %{libkutils}
%{_kde_libdir}/libkutils.so.%{kutils_major}*

#--------------------------------------------------------------------

%define solid_major 4
%define libsolid %mklibname solid %{solid_major}

%package -n %{libsolid}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libsolid}
KDE 4 core library.

%files -n %{libsolid}
%{_kde_libdir}/libsolid.so.%{solid_major}*

#--------------------------------------------------------------------

%define threadweaver_major 4
%define libthreadweaver %mklibname threadweaver %{threadweaver_major}

%package -n %{libthreadweaver}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libthreadweaver}
KDE 4 core library.

%files -n %{libthreadweaver}
%{_kde_libdir}/libthreadweaver.so.%{threadweaver_major}*

#--------------------------------------------------------------------

%define kpty_major 4
%define libkpty %mklibname kpty %{kpty_major}

%package -n %{libkpty}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkpty}
KDE 4 core library.

%files -n %{libkpty}
%{_kde_libdir}/libkpty.so.%{kpty_major}*

#--------------------------------------------------------------------

%define kjsapi_major 4
%define libkjsapi %mklibname kjsapi %{kjsapi_major}

%package -n %{libkjsapi}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkjsapi}
KDE 4 core library.

%files -n %{libkjsapi}
%{_kde_libdir}/libkjsapi.so.%{kjsapi_major}*

#--------------------------------------------------------------------

%define libplasma_major 3
%define libplasma %mklibname plasma %{libplasma_major}

%package -n %{libplasma}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libplasma}
KDE 4 core library.

%files -n %{libplasma}
%{_kde_libdir}/libplasma.so.%{libplasma_major}*

#--------------------------------------------------------------------

%define libkunitconversion_major 4
%define libkunitconversion %mklibname kunitconversion %{libkunitconversion_major}

%package -n %{libkunitconversion}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkunitconversion}
KDE 4 core library.

%files -n %{libkunitconversion}
%{_kde_libdir}/libkunitconversion.so.%{libkunitconversion_major}*

#--------------------------------------------------------------------

%define libkdewebkit_major 5
%define libkdewebkit %mklibname kdewebkit %{libkdewebkit_major}

%package -n %{libkdewebkit}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkdewebkit}
KDE 4 library.

%files -n %{libkdewebkit}
%{_kde_libdir}/libkdewebkit.so.%{libkdewebkit_major}*

#----------------------------------------------------------------------------------------

%define libknewstuff3_major 4
%define libknewstuff3 %mklibname knewstuff3_ %{libknewstuff3_major}

%package -n %{libknewstuff3}
Summary:	KDE 4 library
Group:		System/Libraries
Obsoletes:	%{_lib}knewstuff34 < %{EVRD}

%description -n %{libknewstuff3}
KDE 4 library.

%files -n %{libknewstuff3}
%{_kde_libdir}/libknewstuff3.so.%{libknewstuff3_major}*

#--------------------------------------------------------------------

%define libkcmutils_major 4
%define libkcmutils %mklibname kcmutils %{libkcmutils_major}

%package -n %{libkcmutils}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkcmutils}
KDE 4 library.

%files -n %{libkcmutils}
%{_kde_libdir}/libkcmutils.so.%{libkcmutils_major}*

#--------------------------------------------------------------------

%define libkprintutils_major 4
%define libkprintutils %mklibname kprintutils %{libkprintutils_major}

%package -n %{libkprintutils}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkprintutils}
KDE 4 library.

%files -n %{libkprintutils}
%{_kde_libdir}/libkprintutils.so.%{libkprintutils_major}*

#--------------------------------------------------------------------

%define libkidletime_major 4
%define libkidletime %mklibname kidletime %{libkidletime_major}

%package -n %{libkidletime}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkidletime}
KDE 4 library.

%files -n %{libkidletime}
%{_kde_libdir}/libkidletime.so.%{libkidletime_major}*

#--------------------------------------------------------------------

%define libkemoticons_major 4
%define libkemoticons %mklibname kemoticons %{libkemoticons_major}

%package -n %{libkemoticons}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkemoticons}
KDE 4 library.

%files -n %{libkemoticons}
%{_kde_libdir}/libkemoticons.so.%{libkemoticons_major}*

#--------------------------------------------------------------------
%if %{build_nepomuk}
%define nepomuk_major 4
%define libnepomuk %mklibname nepomuk %{nepomuk_major}

%package -n %{libnepomuk}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libnepomuk}
KDE 4 core library.

%files -n %{libnepomuk}
%{_kde_libdir}/libnepomuk.so.%{nepomuk_major}*
%endif

#--------------------------------------------------------------------

%if %{build_nepomuk}
%define libnepomukquery_major 4
%define libnepomukquery %mklibname nepomukquery %{libnepomukquery_major}

%package -n %{libnepomukquery}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libnepomukquery}
KDE 4 library.

%files -n %{libnepomukquery}
%{_kde_libdir}/libnepomukquery.so.%{libnepomukquery_major}*
%endif

#--------------------------------------------------------------------

%if %{build_nepomuk}
%define libnepomukutils_major 4
%define libnepomukutils %mklibname nepomukutils %{libnepomukutils_major}

%package -n %{libnepomukutils}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libnepomukutils}
KDE 4 library.

%files -n %{libnepomukutils}
%{_kde_libdir}/libnepomukutils.so.%{libnepomukutils_major}*
%endif

#--------------------------------------------------------------------

%if ! %{no_libkactivities}
%define libkactivities_major 6
%define libkactivities %mklibname kactivities %{libkactivities_major}

%package -n %{libkactivities}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkactivities}
KDE 4 library.

%files -n %{libkactivities}
%{_kde_libdir}/libkactivities.so.%{libkactivities_major}*
%endif

#--------------------------------------------------------------------

%define libkdeclarative_major 5
%define libkdeclarative %mklibname kdeclarative %{libkdeclarative_major}

%package -n %{libkdeclarative}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkdeclarative}
KDE 4 library.

%files -n %{libkdeclarative}
%{_kde_libdir}/libkdeclarative.so.%{libkdeclarative_major}*

#--------------------------------------------------------------------

%package devel
Summary:	Header files and documentation for compiling KDE applications
Group:		Development/KDE and Qt
%rename		kdelibs4-devel
Requires:	automoc
Requires:	kde4-macros
Requires:	qt4-qtdbus
Requires:	shared-mime-info
Requires:	xsltproc
# add requires on libxml2-utils, as when building most kde applications,
# it will call xmllint to validate the docbook files:
Requires:	libxml2-utils
Requires:	kdelibs-core = %{EVRD}
Requires:	%{libkcmutils} = %{EVRD}
Requires:	%{libkde3support} = %{EVRD}
Requires:	%{libkdecore} = %{EVRD}
Requires:	%{libkdefakes} = %{EVRD}
Requires:	%{libkdesu} = %{EVRD}
Requires:	%{libkdeui} = %{EVRD}
Requires:	%{libkdewebkit} = %{EVRD}
Requires:	%{libkdnssd} = %{EVRD}
Requires:	%{libkemoticons} = %{EVRD}
Requires:	%{libkfile} = %{EVRD}
Requires:	%{libkhtml} = %{EVRD}
Requires:	%{libkidletime} = %{EVRD}
Requires:	%{libkimproxy} = %{EVRD}
Requires:	%{libkio} = %{EVRD}
Requires:	%{libkjsapi} = %{EVRD}
Requires:	%{libkjsembed} = %{EVRD}
Requires:	%{libkjs} = %{EVRD}
Requires:	%{libkmediaplayer} = %{EVRD}
Requires:	%{libknewstuff2} = %{EVRD}
Requires:	%{libknewstuff3} = %{EVRD}
Requires:	%{libknotifyconfig} = %{EVRD}
Requires:	%{libkntlm} = %{EVRD}
Requires:	%{libkparts} = %{EVRD}
Requires:	%{libkprintutils} = %{EVRD}
Requires:	%{libkpty} = %{EVRD}
Requires:	%{libkrosscore} = %{EVRD}
Requires:	%{libkrossui} = %{EVRD}
Requires:	%{libktexteditor} = %{EVRD}
Requires:	%{libkunitconversion} = %{EVRD}
Requires:	%{libkunittest} = %{EVRD}
Requires:	%{libkutils} = %{EVRD}
Requires:	%{libplasma} = %{EVRD}
Requires:	%{libsolid} = %{EVRD}
Requires:	%{libthreadweaver} = %{EVRD}
%if ! %{no_libkactivities}
Requires:	%{libkactivities} = %{EVRD}
%endif
Requires:	%{libkdeclarative} = %{EVRD}
%if %{build_nepomuk}
Requires:	%{libnepomuk} = %{EVRD}
Requires:	%{libnepomukquery} = %{EVRD}
Requires:	%{libnepomukutils} = %{EVRD}
%endif
Conflicts:	%{name}-core < 5:4.7.80-4

%description devel
This package includes the header files you will need to compile applications 
for KDE. Also included is the KDE API documentation in HTML format for easy 
browsing.

%files devel
%{_datadir}/dbus-1/*/*
%{_kde_includedir}/*
%{_kde_appsdir}/cmake/modules/*
%{_kde_libdir}/libkdefakes.so
%{_kde_libdir}/libkdesu.so
%{_kde_libdir}/libkdnssd.so
%{_kde_libdir}/libkhtml.so
%{_kde_libdir}/libkimproxy.so
%{_kde_libdir}/libkjs.so
%{_kde_libdir}/libkjsembed.so
%{_kde_libdir}/libkmediaplayer.so
%{_kde_libdir}/libknewstuff2.so
%{_kde_libdir}/libknotifyconfig.so
%{_kde_libdir}/libkntlm.so
%{_kde_libdir}/libkparts.so
%{_kde_libdir}/libkrossui.so
%{_kde_libdir}/libktexteditor.so
%{_kde_libdir}/libkunittest.so
%{_kde_libdir}/libkutils.so
%{_kde_libdir}/libkde3support.so
%{_kde_libdir}/libkpty.so
%{_kde_libdir}/libkfile.so
%{_kde_libdir}/libsolid.so
%{_kde_libdir}/libkrosscore.so
%{_kde_libdir}/libkdecore.so
%{_kde_libdir}/libkdeui.so
%{_kde_libdir}/libkio.so
%{_kde_libdir}/libthreadweaver.so
%{_kde_libdir}/libkjsapi.so
%{_kde_libdir}/libplasma.so
%{_kde_libdir}/libkunitconversion.so
%{_kde_libdir}/libkdewebkit.so
%{_kde_libdir}/libknewstuff3.so
%{_kde_libdir}/libkprintutils.so
%{_kde_libdir}/libkidletime.so
%{_kde_libdir}/libkemoticons.so
%{_kde_libdir}/libkcmutils.so
%if ! %{no_libkactivities}
%{_kde_libdir}/libkactivities.so
%endif
%if %{build_nepomuk}
%{_kde_libdir}/libnepomuk.so
%{_kde_libdir}/libnepomukquery.so
%{_kde_libdir}/libnepomukutils.so
%endif
%{_kde_libdir}/libkdeclarative.so
%{_kde_libdir}/kde4/plugins/designer
%{_kde_bindir}/checkXML
%{_kde_mandir}/man1/checkXML.1*
%{_kde_mandir}/man1/makekdewidgets.1*
%{_kde_mandir}/man1/kconfig_compiler.1*
%{_kde_bindir}/kconfig_compiler
%{_kde_bindir}/makekdewidgets
%{_libdir}/cmake/KDeclarative/*.cmake

#----------------------------------------------------------------------------------

%package core
Summary:	KDE 4 system core files
Group:		Graphical desktop/KDE
Requires:	abrt
Requires:	docbook-dtd45-xml
Requires:	docbook-style-xsl
Requires:	rootcerts
Requires:	shared-desktop-ontologies
Requires:	shared-mime-info
Suggests:	enchant-dictionary
Suggests:	xdg-utils
%rename		kdelibs4-core

%description core
KDE 4 system core files.

%files core
%{_kde_bindir}/kbuildsycoca4
%{_kde_bindir}/kcookiejar4
%{_kde_bindir}/kde4-config
%{_kde_bindir}/kded4
%{_kde_bindir}/kdeinit4
%{_kde_bindir}/kdeinit4_shutdown
%{_kde_bindir}/kdeinit4_wrapper
%{_kde_bindir}/kjs
%{_kde_bindir}/kjscmd
%{_kde_bindir}/kmailservice
%{_kde_bindir}/ktelnetservice
%{_kde_bindir}/kross
%{_kde_bindir}/kshell4
%{_kde_bindir}/kunittestmodrunner
%{_kde_bindir}/kwrapper4
%{_kde_bindir}/meinproc4
%{_kde_bindir}/meinproc4_simple
%{_kde_bindir}/preparetips
%if %{build_nepomuk}
%{_kde_bindir}/nepomuk-rcgen
%{_kde_bindir}/kfilemetadatareader
%endif
%dir %{_kde_libdir}/kde4
%{_kde_libdir}/kde4/*.so
%dir %{_kde_libdir}/kde4/libexec
%{_kde_libdir}/kde4/libexec/filesharelist
%attr(4755,root,root) %{_kde_libdir}/kde4/libexec/fileshareset
%{_kde_libdir}/kde4/libexec/kauth-policy-gen
%{_kde_libdir}/kde4/libexec/kconf_update
%{_kde_libdir}/kde4/libexec/kdesu_stub
%{_kde_libdir}/kde4/libexec/kio_http_cache_cleaner
%{_kde_libdir}/kde4/libexec/kioslave
%{_kde_libdir}/kde4/libexec/klauncher
%attr(4755,root,root) %{_kde_libdir}/kde4/libexec/kpac_dhcp_helper
%{_kde_libdir}/kde4/libexec/ksendbugmail
%{_kde_libdir}/kde4/libexec/lnusertemp
%{_kde_libdir}/kde4/libexec/start_kdeinit
%{_kde_libdir}/kde4/libexec/start_kdeinit_wrapper
%dir %{_kde_libdir}/kde4/plugins
%{_kde_libdir}/kde4/plugins/imageformats
%{_kde_libdir}/kde4/plugins/kauth
%{_kde_libdir}/kde4/plugins/script
%{_kde_libdir}/libkdeinit4_*
%{_kde_datadir}/config
%{_kde_datadir}/mime/*
%{_kde_datadir}/kde4
%{_kde_applicationsdir}/kmailservice.desktop
%{_kde_applicationsdir}/ktelnetservice.desktop
%{_kde_appsdir}/proxyscout
%{_kde_appsdir}/LICENSES
%{_kde_appsdir}/kssl
%{_kde_appsdir}/ksgmltools2
%{_kde_appsdir}/knewstuff
%{_kde_appsdir}/kjava
%{_kde_appsdir}/khtml
%{_kde_appsdir}/kdewidgets
%{_kde_appsdir}/kdeui
%{_kde_appsdir}/kconf_update
%{_kde_appsdir}/kcm_componentchooser
%{_kde_appsdir}/kcharselect
%{_kde_docdir}/HTML/en/sonnet
%{_kde_docdir}/HTML/en/common/*
%{_kde_docdir}/HTML/en/kioslave/data
%{_kde_docdir}/HTML/en/kioslave/file
%{_kde_docdir}/HTML/en/kioslave/ftp
%{_kde_docdir}/HTML/en/kioslave/help
%{_kde_docdir}/HTML/en/kioslave/http
%{_kde_docdir}/HTML/en/kioslave/mailto
%{_kde_docdir}/HTML/en/kioslave/rlogin
%{_kde_docdir}/HTML/en/kioslave/telnet
%{_kde_docdir}/HTML/en/kioslave/webdav
%{_kde_mandir}/man1/kde4-config.1*
%{_kde_mandir}/man7/kdeoptions.7*
%{_kde_mandir}/man7/qtoptions.7*
%{_kde_mandir}/man8/kbuildsycoca4.8*
%{_kde_mandir}/man8/kcookiejar4.8*
%{_kde_mandir}/man8/kdeinit4.8*
%{_kde_mandir}/man8/meinproc4.8*
%{_kde_mandir}/man1/kjs.1.*
%{_kde_mandir}/man1/kjscmd.1.*
%{_kde_mandir}/man1/kross.1.*
%{_kde_mandir}/man1/preparetips.1.*
%{_kde_mandir}/man8/kded4.8.*
%{_kde_iconsdir}/hicolor/*/actions/presence_away.png
%{_kde_iconsdir}/hicolor/*/actions/presence_offline.png
%{_kde_iconsdir}/hicolor/*/actions/presence_online.png
%{_kde_iconsdir}/hicolor/*/actions/presence_unknown.png
%{_kde_datadir}/locale/all_languages
%{_sysconfdir}/dbus-1/system.d/org.kde.auth.conf
%{_kde_sysconfdir}/xdg/kde4/menus/applications.menu
%{_kde_appsdir}/kauth
%{_kde_appsdir}/plasma
%{_kde_datadir}/locale/en_US/entry.desktop

#----------------------------------------------------------------------------------

%if %{compile_apidox}
%package apidoc
Summary:	Development documentation for %{name}
Group:		Development/KDE and Qt
Requires:	qt4-doc

%description apidoc
This packages contains all development documentation for kdelibs

%files apidoc
%{_docdir}/kde4/api/*
%endif

#----------------------------------------------------------------------------------

%prep
%setup -q -n kdelibs-%{version}

%patch1 -p0
%if ! %{with_drkonqi}
%patch2 -p0
%endif
%patch3 -p1
%if %mdvver > 3000000
%patch4 -p1 -b .ossl11~
%endif
%patch5 -p1 -b .compile~
%patch10 -p1 -b .phonepower~
%patch11 -p1 -b .delayed~
%patch12 -p1 -R
%patch13 -p1 -b .dtd45~
%patch100 -p1
#patch200 -p1
#patch203 -p1
%patch204 -p1
%patch206 -p1
%patch207 -p1
%patch208 -p1
%patch209 -p1
%patch210 -p1
%patch211 -p1

%patch220 -p1 -b .p220~

%build
%ifarch %{ix86}
# Use linker flags to reduce memory consumption (bfd only)
#global CFLAGS %cflags -Werror
#global CXXFLAGS %cxxflags -Werror
%global LDFLAGS %{ldflags} -Wl,--no-keep-memory -Wl,--reduce-memory-overheads
# Workaround for abf builds running out of memory
export CFLAGS="$CFLAGS -g0 "
export CXXFLAGS="$CXXFLAGS -g0"
%endif

%cmake_kde4 -DCMAKE_BUILD_TYPE=debugfull -DKDE_DISTRIBUTION_TEXT="%{distribution} %{distepoch}" -DKAUTH_BACKEND:STRING="PolkitQt-1" %{?udisk_backend:-DWITH_SOLID_UDISKS2:BOOL=ON} %{?no_libkactivities:-DBUILD_libkactivities:BOOL=OFF} %{?build_nepomuk:-DKIO_NO_SOPRANO:BOOL=ON}

%make -j1 VERBOSE=1

%if %{compile_apidox}
  cd ..
  doc/api/doxygen.sh --doxdatadir=${PWD}/doc/common .
%endif

%install
make install/fast DESTDIR=%{buildroot} -C build

%if %{compile_apidox}
  mkdir -p %{buildroot}%{_docdir}/kde4/api
  cp -av kdelibs-%{version}-apidocs %{buildroot}%{_docdir}/kde4/api/kdelibs
%endif

rm -fr %{buildroot}%{_kde_appsdir}/kssl/ca-bundle.crt
ln -snf %{_sysconfdir}/pki/tls/certs/ca-bundle.crt %{buildroot}%{_kde_appsdir}/kssl/ca-bundle.crt
