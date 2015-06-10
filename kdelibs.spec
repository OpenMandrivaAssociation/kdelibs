%define bootstrap 1
%{?_branch: %{expand: %%global bootstrap 1}}

%define compile_apidox 0
%{?_with_apidox: %{expand: %%global compile_apidox 1}}

%define with_drkonqi 0
%{?_with_drkonqi: %{expand: %%global with_drkonqi 1}}

%define udisk_backend 1

# exclude libkactivities or not
%define no_libkactivities 1

%define build_nepomuk 0
%define major_ver 15.04.2

Summary:	K Desktop Environment - Libraries
Name:		kdelibs
Version:	4.14.9
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
Requires:	kde4-config-file
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

%build
%ifarch %{i586}
# Use linker flags to reduce memory consumption (bfd only)
%global CFLAGS %cflags -Werror
%global CXXFLAGS %cxxflags -Werror
%global LDFLAGS %{ldflags} -Wl,--no-keep-memory -Wl,--reduce-memory-overheads
# Workaround for abf builds running out of memory
export CFLAGS="$CFLAGS -g0 -Werror"
export CXXFLAGS="$CXXFLAGS -g0 -Werror"
%endif

%cmake_kde4 -DKDE_DISTRIBUTION_TEXT="%{distribution} %{distepoch}" -DKAUTH_BACKEND:STRING="PolkitQt-1" %{?udisk_backend:-DWITH_SOLID_UDISKS2:BOOL=ON} %{?no_libkactivities:-DBUILD_libkactivities:BOOL=OFF} %{?build_nepomuk:-DKIO_NO_SOPRANO:BOOL=ON}

%make

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

%changelog
* Tue Dec 02 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 5:4.14.3-2
- Use docbook-dtd45-xml instead of docbook-dtd42-xml
- Minor cleanups

* Tue Nov 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 5:4.14.3-1
- New version 4.14.3

* Wed Oct 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 5:4.14.2-1
- New version 4.14.2

* Mon Sep 29 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 5:4.14.1-1
- New version 4.14.1
- Drop merged qfile-header patch

* Tue Jul 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 5:4.13.3-1
- New version 4.13.3
- Drop no longer needed giflib5.1 patch

* Wed Jun 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 5:4.13.2-1
- New version 4.13.2
- Drop kfilemodule-l10n upstream patch
- Update giflib5.1 patch
- Update files, man for kdecmake is obsolete

* Wed May 28 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 5:4.12.4-4
- Add giflib5.1 patch to fix build with giflib 5.1

* Fri Apr 18 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 5:4.12.4-3
- Add qfile-header patch to fix the way QFile is included in kio/global.h

* Sun Apr 13 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 5:4.12.4-2
- Add kfilemodule-l10n patch from upstream to fix localization in kfile dialogs

* Wed Apr 02 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 5:4.12.4-1
- New version 4.12.4
- Re-diff improve-mimetype-detection-for-webdav patch

* Tue Mar 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 5:4.12.3-1
- New version 4.12.3
- Add armlinking patch to fix build for arm
- Add cmake2.8.12.2 patch to fix build with cmake newer than 2.8.12

* Tue Feb 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 5:4.12.2-1
- New version 4.12.2

* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 5:4.12.1-1
- New version 4.12.1

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 5:4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 5:4.11.3-1
- New version 4.11.3

* Tue Oct 22 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 5:4.11.2-3
- Add delayed icons patch to fix issue with incorrect icons on desktop
- Add containment config patch to fix issue with empty dialog when adding panel

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 5:4.11.2-1
- New version 4.11.2
- Drop find-samba patch because samba4 detection was fixed in upstream

* Sun Sep 15 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 5:4.11.1-2
- Add phonepower patch to support battery reporting in KDE Connect

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 5:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 5:4.11.0-1
- New version 4.11.0
- Drop kauthhelper patch (merged in upstream)

* Wed Jul 17 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 5:4.10.5-4
- Drop most of devel package Requires

* Wed Jul 17 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 5:4.10.5-3
- Sort and fix BuildRequires and devel package Requires
- Remove some no longer needed Conflicts

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 5:4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 5:4.10.4-1
- New version 4.10.4

* Thu May 23 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 5:4.10.3-2
- Add patch to avoid creation of .config etc folders in filesystem root

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 5:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 5:4.10.2-1
- New version 4.10.2
- Drop giflib5 patch (merged in upstream)
- Change libsasl-devel to sasl-devel in BuildRequires and Requires

* Sun Mar 10 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 5:4.10.1-2
- Add patch for giflib5 support

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 5:4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 5:4.10.0-1
- New version 4.10.0

* Thu Jan 31 2013 Per Øyvind Karlsen <peroyvind@mandriva.org> 4.9.98-2
- rebuild

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 5:4.9.4-1
- New version 4.9.4

* Thu Nov 29 2012 Sergey Borovkov <sergey.borovkov@osinit.ru> 5:4.9.3-2
- Added patch for webdav mimetypes detection

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 5:4.9.3-1
- New version 4.9.3

* Fri Nov 04 2012 Sergey Borovkov <sergey.borovkov@osinit.ru> 5:4.9.2-2
- Updated klook patch

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 5:4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 5:4.9.1-2
- New version 4.9.1
- Add patch for items preview with klook in standard open/save dialog

* Fri Aug 03 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 5:4.9.0-1
- New version 4.9.0

* Thu Jul 12 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 5:4.8.97-1
- New version 4.8.97

* Mon Jul 09 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 5:4.8.95-4
- Update fileplaces patch (adds Documents to default bookmarks)

* Sun Jul 08 2012 Bernhard Rosenkraenzer <bero@bero.eu> 5:4.8.95-3
+ Revision: 808509
- Rebuild for libudev.so.1
- Fix rpmlint problems

* Mon Jul 02 2012 Andrey Bondrov <abondrov@mandriva.org> 5:4.8.95-2
+ Revision: 807874
- Rebuild for new attica

* Sun Jul 01 2012 Andrey Bondrov <abondrov@mandriva.org> 5:4.8.95-1
+ Revision: 807688
- Adjust BuildRequires a bit
- Convert more stuff to pkgconfig style
- Convert BuildRequires to pkgconfig style again
- Update to 4.8.95, sync with Rosa

* Fri Jun 08 2012 Crispin Boylan <crisb@mandriva.org> 5:4.8.4-1
+ Revision: 803578
- New release

* Fri May 04 2012 Crispin Boylan <crisb@mandriva.org> 5:4.8.3-1
+ Revision: 795964
- New release

* Wed Apr 18 2012 Crispin Boylan <crisb@mandriva.org> 5:4.8.2-1
+ Revision: 791676
- New release

* Thu Mar 29 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 5:4.8.1-2
+ Revision: 788192
- rebuild with fixed dependency generator

* Tue Mar 13 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 5:4.8.1-1
+ Revision: 784597
- Fix file list
- New upstream tarball

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - use pkgconfig() deps for buildrequires

* Sun Feb 12 2012 Oden Eriksson <oeriksson@mandriva.com> 5:4.8.0-5
+ Revision: 773525
- rebuild
- rebuilt because of missing lib[64]kjsapi4

* Wed Feb 08 2012 Matthew Dawkins <mattydaw@mandriva.org> 5:4.8.0-3
+ Revision: 772226
- added missing BR libxi-devel

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt for new pcre

* Sat Jan 28 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 5:4.8.0-2
+ Revision: 769544
- Add P100: Fix loading profiles

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 5:4.8.0-1
+ Revision: 762515
- New upstream tarball
- Add Requires: dbus-x11 ( from mageia )

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 5:4.7.97-1
+ Revision: 758100
- New upstream tarball

* Sat Dec 31 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 5:4.7.95-1
+ Revision: 748541
- New version

* Thu Dec 29 2011 Zé <ze@mandriva.org> 5:4.7.90-2
+ Revision: 748187
- rebuild against new attica

* Fri Dec 09 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 5:4.7.90-1
+ Revision: 739370
- New upstream tarball

  + Zé <ze@mandriva.org>
    - fix path fir dbus files
    - seams neoclust dont cares about fixing things, kde-l10n-en_US needs to be removed else is NOT possible to upgrade to kde from cooker
    - clean requires that already exist by default in devel package

* Fri Nov 25 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 5:4.7.80-6
+ Revision: 733369
- remove overlapping dependencies for -devel package triggering rpm bug

* Fri Nov 25 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 5:4.7.80-5
+ Revision: 733316
- Fix requires in the devel package

* Fri Nov 25 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 5:4.7.80-4
+ Revision: 733301
- Add back mattydaw buildrequire fix
- Enhance self requires
- Add grantlee-devel as buildrequires
  Do not provide plasma-devel anymore
- Add SUID on kpac_dhcp_helper ( from fedora )
- Move makekdewidgets in devel ( from fedora )
- Revert previous commit ( some changes will be cherrypicked if useful)
- Fix icons listing  ( Patch from Mikala )
- Do not own icons dir
- Revert the 3 previous commits because they were wrong:

  + Zé <ze@mandriva.org>
    - once again you revert things that fix errors, mainproc its just needed to develop as discussed with major kde velopment person
    - theres:
      o %%{_kde_libdir}/kde4/plugins/script/libkrossqtsplugin.so.4
      o %%{_kde_libdir}/kde4/plugins/script/libkrossqtsplugin.so.4.7.0
      that arent devel files, and exist in core, thats why %%{_kde_libdir}/kde4/plugins/script/libkrossqtsplugin.so is moved to devel package being a devel file
    - you should be consistent to what you say and use the same macros the files that exist in /etc
    - the the file list was to fix the file listed twice since you had a simple * and in the next line you was listing again a file from the same path
    - the file %%{_kde_libdir}/kde4/libexec/kauth-policy-gen needs to be setuid as indicated in kio/misc/kpac/README.wpad (this was also indicated in the spec.
    - its neeed to have a conflict for kde-l10n-en_US, since kde-l10n-en_US < 2:4.6.4-1 isnt conflicting with the official one since their version is 4.6.4-2, therefore the existant conflict was useless and was preventing an upgrade.
    - please try to not revert fixes that are fixing errors just because you dont like me and for the sake of kde

* Fri Nov 25 2011 Matthew Dawkins <mattydaw@mandriva.org> 5:4.7.80-3
+ Revision: 733275
- fixed BR this time
- corrected BR name

  + Zé <ze@mandriva.org>
    - put back binaries that are only used for development into devel package:
        o %%{_kde_bindir}/makekdewidgets
        o %%{_kde_bindir}/meinproc4
        o %%{_kde_bindir}/meinproc4_simple
      and there manuals:
        o %%{_kde_mandir}/man1/kdecmake.1*
        o %%{_kde_mandir}/man1/makekdewidgets.1*
        o %%{_kde_mandir}/man8/meinproc4.8*
    - set suid kauth-policy-gen due to security issues
    - conflict kde-l10n-en_US to allow upgrades (for example upgrading to cooker)
    - fix file list to avoid files in severall packages (duplicates)
    - move %%{_kde_libdir}/kde4/plugins/script/libkrossqtsplugin.so into devel package
    - add back grantlee support for generating compilable code by the ModelEventLogger
    - do not own directory /usr/share/icons
    - fix an entry from %%_kde_sysconfdir to %%{_sysconfdir},but in fact we could even use the prefix in all entries if kde4-macros would be correctly done,and the files would continue being installed in /etc even if using the macro %%{_kde_sysconfdir}
    - rename %%_docdir into %%{_kde_docdir} to avoid installing diferente kde versions documentation in the same directory, therefore causing conflicts

* Tue Nov 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 5:4.7.80-2
+ Revision: 732447
- Try to workaround a nasty rpm5 bug by changing a space by a tab
  in kdelibs4-devel Requires

* Sat Nov 19 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 5:4.7.80-1
+ Revision: 731719
- New version 4.7.80
- Add back libkactivities-devel requires now it is fixed

* Fri Nov 18 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 5:4.7.41-10
+ Revision: 731558
- Do not requires libkactivities-devel

* Fri Nov 18 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 5:4.7.41-9
+ Revision: 731534
- Fix requires when building W/o bundled libkactivities

* Fri Nov 18 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 5:4.7.41-8
+ Revision: 731516
- Fix file list when building w/o bundled libkactivities
- Do not build bundled libkactivities

* Tue Nov 01 2011 Oden Eriksson <oeriksson@mandriva.com> 5:4.7.41-6
+ Revision: 709282
- sync with MDVSA-2011:162

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Revert previous commits:
      	- Do not move files in devel packages w/o good reasons: .so files in kde in %%libdir/kde4/ are not devel files and this add no devel requires
      	- Do not use kde macros for files not owned by kde packages
      	- Do not move to many files in the devel package
    - Revert because previous commit has not been reviewed by Mandriva kde team, this is a MUST HAVE

  + Zé <ze@mandriva.org>
    - use kde4 macros
    - add conflict for kde-l10n-en_US to avoid break upgrade into version 4.7.41
    - fix provides
    - move strict development apps into devel package
    - move devel file to correct package to avoid having kdelibs4-devel installed by default
    - enable grantlee support needed by ProxyModel test suite
    - add missing major4 variable
    - > - add optional support for grantlee
      > - mode strict devel apps into devel package
      > - fix kde-l10n-en_US conflict
      > - use kde macros
      > - fix install section (clean buildroot before install)
      > - arrange spec
    - do not own icons directory
    - move %%libdir/kde4/plugins/script/libkrossqtsplugin.so into devel package,this was causing th at devel package was being installed wrongly required
    - change to conflict since obsolete will erase kde-l10n-EN_USfrom BS

* Thu Sep 29 2011 Zé <ze@mandriva.org> 5:4.7.41-4
+ Revision: 701887
- we need to obsolete kde-l10n-en_US to avoid break upgrade into cooker
- add missing conflict for kde-l10n-en_US

* Mon Sep 19 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 5:4.7.41-3
+ Revision: 700277
- Workaround libpng new API
- Fix kdelibs build

* Mon Aug 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 5:4.7.41-1
+ Revision: 696064
- New version 4.7.41

* Wed Jul 27 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 5:4.7.40-1
+ Revision: 691997
- Remove wrong requires
- Finally fix file list
- Fix file list
- Fix file list
- Fix file list
- Fix file list
- Fix file list
- Fix file list
- Add new libs packages
- Update to kde 4.7.40
  Comment all file list to be able to see the whole list

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - make %%branch conditional inline in just one release tag definition to avoid
      confusion about which to update
    - fix file conflict during upgrade due to /usr/share/locale/en_US/entry.desktop
      being moved to kdelibs4-core from kdebase4-runtime
    - fix upgrade of %%{_lib}knewstuff34 to renamed %%{_lib}knewstuff3_4

* Mon Jul 11 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.6.95-1
+ Revision: 689599
- New version 4.7 Rc2

* Fri Jul 08 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.6.90-2
+ Revision: 689331
- Fix requires in the devel package

* Fri Jul 08 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.6.90-1
+ Revision: 689295
- Fix file list
- Update to kde 4.7 rc1

* Thu Jun 16 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.6.4-6
+ Revision: 685494
- Rebuild without bootstraping

* Wed Jun 15 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.6.4-5
+ Revision: 685455
- Enable bootstrap
- Change kde-l10n as suggests the time it is in contrib

* Wed Jun 15 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.6.4-4
+ Revision: 685222
- Remove kde-l10n-en_US package
  Change kde4-l10n requires into kde-l10n

* Tue Jun 14 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.6.4-3
+ Revision: 684994
- Fix patch name
- Update nepomuk patch
- New version 4.6.4

* Mon Jun 06 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.6.3-3
+ Revision: 682950
- Add NetworkShare for solid from trunk

* Mon Jun 06 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.6.3-2
+ Revision: 682893
- Sync nepomuk with trunk
- Remove old and unneeded obsoletes/conflicts
  Adapt spec file for rpm5

* Thu May 12 2011 Funda Wang <fwang@mandriva.org> 2:4.6.3-1
+ Revision: 673924
- New version 4.6.3
  hunspell patch merged

* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 2:4.6.2-2
+ Revision: 655818
- add upstream patch to find hunspell 1.3

* Wed Apr 06 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.6.2-1
+ Revision: 650960
- Remove merged patch
- Remove mkrel
- New version 4.6.2

* Mon Mar 28 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.6.1-6
+ Revision: 648669
- Add P100 to fix CVE-2011-1168

* Mon Mar 21 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.6.1-5
+ Revision: 647286
- Enable udisk backend
- Better fix for buildrequires

* Mon Mar 21 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.6.1-4
+ Revision: 647284
- FIx builrequires

* Tue Mar 08 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.6.1-3
+ Revision: 642841
- Add back patch use mdv translations in menu + dolphin

* Mon Feb 28 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.6.1-2
+ Revision: 640728
- New version 4.6.1

* Fri Feb 18 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.6.0-2
+ Revision: 638474
- Do not use ia ora anymore

* Wed Jan 26 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.6.0-1
+ Revision: 632980
- Remove merged patch
- New version KDE 4.6 Final

* Fri Jan 21 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.5.95-6
+ Revision: 632066
- Fix patch name

  + John Balcaen <mikala@mandriva.org>
    - Add patch100 from upstream to fix kde #251356 (fix a crash in solid udev backend)

* Thu Jan 06 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.5.95-5mdv2011.0
+ Revision: 629122
- New version KDE 4.6 RC2

* Thu Dec 23 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.5.90-5mdv2011.0
+ Revision: 624065
- New upstream tarball

* Tue Dec 14 2010 Funda Wang <fwang@mandriva.org> 2:4.5.85-5mdv2011.0
+ Revision: 621657
- really rebuild for new polkit-qt

* Fri Dec 10 2010 Funda Wang <fwang@mandriva.org> 2:4.5.85-4mdv2011.0
+ Revision: 620271
- rebuild for new polit-qt-1

* Wed Dec 08 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.5.85-3mdv2011.0
+ Revision: 616345
- New upstream tarball

* Wed Dec 01 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.5.80-3mdv2011.0
+ Revision: 604215
- Fix requires

* Mon Nov 29 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.5.80-2mdv2011.0
+ Revision: 603087
- Use ABRT instead of DrKonqi

* Fri Nov 26 2010 Funda Wang <fwang@mandriva.org> 2:4.5.80-1mdv2011.0
+ Revision: 601419
- new version 4.5.80 (aka 4.6 beta1)

* Sat Nov 20 2010 Funda Wang <fwang@mandriva.org> 2:4.5.77-0.svn1198704.1mdv2011.0
+ Revision: 599088
- new snapshot 4.5.77

* Thu Nov 18 2010 Funda Wang <fwang@mandriva.org> 2:4.5.76-0.svn1197335.3mdv2011.0
+ Revision: 598545
- requires docbook-style for transforming

* Mon Nov 15 2010 Funda Wang <fwang@mandriva.org> 2:4.5.76-0.svn1197335.2mdv2011.0
+ Revision: 597694
- new snapshot

* Sat Nov 13 2010 Funda Wang <fwang@mandriva.org> 2:4.5.76-0.svn1195844.2mdv2011.0
+ Revision: 597066
- add conflicts to ease upgrade

* Fri Nov 12 2010 Funda Wang <fwang@mandriva.org> 2:4.5.76-0.svn1195844.1mdv2011.0
+ Revision: 596454
- split out en_US
- new snapshot 4.5.76

* Thu Oct 28 2010 Funda Wang <fwang@mandriva.org> 2:4.5.74-0.svn1190490.1mdv2011.0
+ Revision: 589655
- upstream tarball

* Wed Oct 27 2010 Funda Wang <fwang@mandriva.org> 2:4.5.73-0.svn1190377.1mdv2011.0
+ Revision: 589594
- New snapshot
- new snapshot to fix bug#61416

* Thu Oct 07 2010 Funda Wang <fwang@mandriva.org> 2:4.5.71-0.svn1183355.1mdv2011.0
+ Revision: 583975
- update file list
- new snapshot 4.5.71
- modify libpackage name according to our lib policy

* Tue Sep 14 2010 Funda Wang <fwang@mandriva.org> 2:4.5.68-1mdv2011.0
+ Revision: 578129
- clean extra spaces
- New snapshot 4.5.68
- Patch10 merged upstream

* Thu Sep 02 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.5.67-2mdv2011.0
+ Revision: 575366
- Fix groups
- Fix file list
- Fix file list
- Fix groups
- New version 4.5.67
- Rebuild

  + Funda Wang <fwang@mandriva.org>
    - bump requires on soprano

* Mon Aug 30 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.5.65-2mdv2011.0
+ Revision: 574551
- Rebuild

* Mon Aug 30 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.5.65-1mdv2011.0
+ Revision: 574457
- Use kde snapshots

* Wed Aug 18 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.5.0-4mdv2011.0
+ Revision: 571147
- Rediff default places patch
  Merge timeline patch inside the default places one

* Tue Aug 10 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.5.0-2mdv2011.0
+ Revision: 568346
- Fix build release
- New upstream tarball

* Wed Aug 04 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.5.0-1mdv2011.0
+ Revision: 565757
- Update to version 4.5.0

* Tue Jul 27 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.95-1mdv2011.0
+ Revision: 562080
- kde 4.4.95

* Fri Jul 23 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.92-1mdv2011.0
+ Revision: 557154
- Remove old sources/patches
- Update to kde 4.5 RC 2

* Wed Jun 23 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.3-16mdv2010.1
+ Revision: 548732
- Add missing header ( needed for nepomuk scribo)

* Sat Jun 19 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.3-15mdv2010.1
+ Revision: 548335
- Add new UDS Entry, needed for runtime

* Fri Jun 18 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.3-14mdv2010.1
+ Revision: 548296
- Fix file list
- Update nepomuk patch

* Thu Jun 10 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.3-13mdv2010.1
+ Revision: 547857
- Fix size of pushbuttons in notifications

* Wed Jun 02 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.3-12mdv2010.1
+ Revision: 546996
- Remove patch6, break command line encoding

* Wed May 26 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.3-11mdv2010.1
+ Revision: 546314
- Fix Timeline translation
- Add 2 nepomuk patches from trunk fixing crashes

* Mon May 24 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.3-9mdv2010.1
+ Revision: 545742
- Rebuild in release mode

* Mon May 17 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.3-8mdv2010.1
+ Revision: 544912
- Add patches to sync with branch

  + Ahmad Samir <ahmadsamir@mandriva.org>
    - proof-read the About KDE -> Mandriva KDE text

* Wed May 12 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.3-7mdv2010.1
+ Revision: 544573
- Fix FindFFmpeg.cmake, to be kdemultimedia friendly

* Wed May 12 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.3-6mdv2010.1
+ Revision: 544547
- New version of FindFFmpeg.cmake needed for fmpegthumbnailer for video previews
- Update nepomuk patch

* Sun May 09 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.3-5mdv2010.1
+ Revision: 544285
- Add Nepomuk/Query/OptionalTerm include ( needed for nepomuk-scribo )

* Sun May 09 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.3-4mdv2010.1
+ Revision: 544220
- New version of the nepomuk patch
- Add branch patches:
        - Allow empty passwords and logins on routers
        - Add a new french translator
- Update nepomuk patch
- add patch
- Add branch patches (P100 -> 103 )

* Tue May 04 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.3-1mdv2010.1
+ Revision: 542134
- Update to version 4.4.3

* Tue May 04 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.2-5mdv2010.1
+ Revision: 542024
- Sync nepomuk with trunk
- Apply patch13 conditionnaly
- Add a patch ( not applied yet ) disactivating DrKonqi )

* Thu Apr 15 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.2-4mdv2010.1
+ Revision: 535022
- Really remove solid patch for now

* Tue Apr 06 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.2-3mdv2010.1
+ Revision: 532383
- Rebuild

* Fri Apr 02 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.2-2mdv2010.1
+ Revision: 530785
- Add back nepomuk patch

* Tue Mar 30 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.2-1mdv2010.1
+ Revision: 528932
- Fix trash patch ( add a new config key)
- Disable the solid backport for the moment
- Update to version 4.4.2

* Sun Mar 28 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.1-5mdv2010.1
+ Revision: 528307
- Rebuild against new perl

* Fri Mar 26 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.1-4mdv2010.1
+ Revision: 527687
- Update solid patch

* Thu Mar 25 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.1-3mdv2010.1
+ Revision: 527506
- Add a confirmation window when empyting trash bin

* Wed Mar 10 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.1-2mdv2010.1
+ Revision: 517448
- Rebuild because of lost package

* Wed Mar 10 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.1-1mdv2010.1
+ Revision: 517370
- Sync solid with trunk that provide a kupnp backend.
- Remove patch4, this have been fixed upstream in commit 1094430
- Backport a trunk patch fixing kdialog buttons focus
- Remove merged patches
- Update to version 4.4.1

  + Christophe Fergeau <cfergeau@mandriva.com>
    - only build enchant spellchecker for more distro-wide consistency

* Wed Feb 24 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.0-17mdv2010.1
+ Revision: 510670
- Add branch patch fixing nepomuk bug
- Add a branch patch fixing a crash
- Fix kdelibs-4.4.0-fix-detect-shared-folder.patch
- Properly detect shared folders
- Use Downloads instead of Download

* Tue Feb 16 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.0-14mdv2010.1
+ Revision: 506561
- Backport commit 1090919 from branch

* Mon Feb 15 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.0-13mdv2010.1
+ Revision: 506139
- Fix typo in videos default place
- Add some new default places ( Music, download, pictures, videos)
  Rediff patch for default timeline place
  Add comment about patch10

* Tue Feb 09 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.0-11mdv2010.1
+ Revision: 503108
- Use new upstream tarball

* Tue Feb 09 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.0-10mdv2010.1
+ Revision: 502612
- Update to version 4.4.0

* Thu Feb 04 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.98-10mdv2010.1
+ Revision: 500744
- Disable patch10 for the moment

* Wed Feb 03 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.98-9mdv2010.1
+ Revision: 500310
- Fix kdelibs-4.3.98-fix-supportedprotocols.patch
- forward port 2010 patch to handle zip:/ kioslave for non kde apps

* Tue Feb 02 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.98-7mdv2010.1
+ Revision: 499816
- Do not hardcode default theme, use the one from aplasmarc instead

* Mon Feb 01 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.98-6mdv2010.1
+ Revision: 498987
- Fix file list to use polkit-1
- Fix file list
- Use PolkitQt-1 by default

* Mon Feb 01 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.98-5mdv2010.1
+ Revision: 498952
- Update to version 4.3.98 aka "kde 4.4 RC3"

* Sun Jan 31 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.95-5mdv2010.1
+ Revision: 498808
- Use mdv theme by default

* Fri Jan 29 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.95-4mdv2010.1
+ Revision: 498054
- Apply P9

* Fri Jan 29 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.95-3mdv2010.1
+ Revision: 498053
- Fix default wallpaper

* Wed Jan 27 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.95-2mdv2010.1
+ Revision: 496963
- Do not build with enable final, BKO: 220403

* Mon Jan 25 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.95-1mdv2010.1
+ Revision: 495628
- Use Polkit as backend for the moment
- Update to kde 4.4Rc2
- Enable polkit support

* Fri Jan 22 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.90-4mdv2010.1
+ Revision: 494905
- Fix plasma to use the WallpaperMode defined in the desktoptheme

* Sun Jan 17 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.90-3mdv2010.1
+ Revision: 492871
- Fix conflict with kdeplatform4-devel

* Mon Jan 11 2010 Funda Wang <fwang@mandriva.org> 2:4.3.90-2mdv2010.1
+ Revision: 489620
- rebuild for new libjpeg v8

* Fri Jan 08 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.90-1mdv2010.1
+ Revision: 487675
- Remove merged patch
- Update to 4.4 Rc1
- Remove those as they are already required by qt4-devel

* Sat Dec 26 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.85-6mdv2010.1
+ Revision: 482501
- Add libxscrnsaver-devel as buildrequires

* Sat Dec 26 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.85-5mdv2010.1
+ Revision: 482488
- Remove unneeded X11-Devel buildrequires

* Sat Dec 26 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.85-4mdv2010.1
+ Revision: 482333
- Bump release
- Build with enable final

* Wed Dec 23 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.85-3mdv2010.1
+ Revision: 481687
- Rebuild in debug mode

* Tue Dec 22 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.85-2mdv2010.1
+ Revision: 481287
- use patch from strueg to active the timeline:/ protocol

* Mon Dec 21 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.85-1mdv2010.1
+ Revision: 480514
- Update to kde 4.4 Beta2
- Obsolete lilypond-kde

* Tue Dec 15 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.80-5mdv2010.1
+ Revision: 479029
- Requires shared-desktop-ontologies on kdelibs4-common

* Fri Dec 04 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.80-4mdv2010.1
+ Revision: 473341
- Add shared-desktop-ontologies as requires on devel package

* Fri Dec 04 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.80-3mdv2010.1
+ Revision: 473191
- Use updated tarballs for beta1

* Thu Dec 03 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.80-2mdv2010.1
+ Revision: 472867
- Add attica-devel as BuildRequire

* Thu Dec 03 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.80-1mdv2010.1
+ Revision: 472794
- Update to kde 4.4 Beta1
  Remove merged patch
  Rediff patches

* Mon Nov 30 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.77-2mdv2010.1
+ Revision: 471753
- Fix crash in kbuildsycoca and add debugs to understand more why it crashed

  + Funda Wang <fwang@mandriva.org>
    - fix requires on qt4

* Thu Nov 26 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.77-1mdv2010.1
+ Revision: 470360
- Add libknewstuff3 package
- Remove unused test patch
- Update to kde 4.3.77
- Use kde macro for the included files
- conflicts with old webkitkde package

  + Funda Wang <fwang@mandriva.org>
    - add conflicts on webkitkde

* Mon Nov 16 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.75-3mdv2010.1
+ Revision: 466628
- Revert wrong commit

  + Funda Wang <fwang@mandriva.org>
    - obsoletes webkitkde also
    - increase conflicts on kdebase-workspace

* Mon Nov 16 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.75-1mdv2010.1
+ Revision: 466494
- Update to kde 4.3.75
  Rediff patch 5
  Remove patch 8: merged upstream
  New packages:
              - libkdewebkit
              - libnepomukquery

* Wed Nov 11 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.73-5mdv2010.1
+ Revision: 464717
- sorry, those debug things should not have been commited
- Rebuild against new qt

* Sat Nov 07 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.73-3mdv2010.1
+ Revision: 462409
- Add kdelibs experimental back in kdelibs

* Fri Nov 06 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.73-2mdv2010.1
+ Revision: 461243
- Obsolete kdelibs4-experimental-devel for now ( the one from trunk is empty for the moment )

* Fri Nov 06 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.73-1mdv2010.1
+ Revision: 461099
- Fix buildrequires
- fix vars name
- Honor the Use of Hal-lock
- Fix Requires on qt4
- Update to kde 4.3.73
  Remove merged patches
  Fix File list
  Rediff some patches

* Wed Oct 28 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.2-11mdv2010.0
+ Revision: 459715
- Add patch 119 to fix a security issue ( http://www.ocert.org/advisories/ocert-2009-015.html )
- use a macro for kdelibs3 epoch

* Thu Oct 22 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.2-9mdv2010.0
+ Revision: 458649
- Use rootcerts instead of kde bundled certs

* Sun Oct 18 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.2-8mdv2010.0
+ Revision: 458085
- backport a nepomuk fix
- Add a suggests in xdg-utils, to allow to use kde4 apps outside of KDE
- Remove kdelibs-4.3.2-use-xdgopen-prefer-kfmclient.patch because this is useless as
  this patch will call, under KDE, kfmclient or kde-open and as if we are not under KDE,
  xdg-open will be called.
  The real fix have been done in mandriva-kde4-config

* Fri Oct 16 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.2-6mdv2010.0
+ Revision: 457962
- Fix login in anonymous ( patch from our great helio )

* Thu Oct 15 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.3.2-5mdv2010.0
+ Revision: 457702
- Restore desktop translation patch to use local mdv translations

* Wed Oct 14 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.2-4mdv2010.0
+ Revision: 457235
- Add wrongly removed patch

* Wed Oct 14 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.2-3mdv2010.0
+ Revision: 457234
- Backport the add of the activate method

  + Funda Wang <fwang@mandriva.org>
    - prefer xdg-open over kfmclient even in KDE session

* Wed Oct 07 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.3.2-2mdv2010.0
+ Revision: 455533
- Fix deadlock in a simultaneous usage of mutex bu klocale and klocalizedstring

* Sun Oct 04 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.3.2-1mdv2010.0
+ Revision: 453712
- New upstream release 4.3.2.

* Sun Sep 27 2009 Olivier Blin <blino@mandriva.org> 2:4.3.1-10mdv2010.0
+ Revision: 449821
- fix bootstrap definition
- add bootstrap flag (from Arnaud Patard)

* Thu Sep 24 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.3.1-9mdv2010.0
+ Revision: 448335
- Update nepomuk filemodule patch

* Wed Sep 23 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.3.1-8mdv2010.0
+ Revision: 447910
- Add nepomuk file dialog instance

* Sat Sep 19 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.1-7mdv2010.0
+ Revision: 444736
- Fix typo

* Sat Sep 19 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.1-6mdv2010.0
+ Revision: 444731
- Fix stupid typo

* Fri Sep 18 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.1-5mdv2010.0
+ Revision: 444250
- Rebuild
- Obsolete kde3 packages
- Add obsolete for kde3 upgrade

* Sun Sep 13 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.1-2mdv2010.0
+ Revision: 438589
- Bump for release
- Remove obsoletes on libs
- Obsolete kde3 packages

* Tue Sep 01 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.3.1-1mdv2010.0
+ Revision: 423267
- Put the proper release number until someone decide rebuild package

* Mon Aug 31 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.3.1-0.1mdv2010.0
+ Revision: 423094
- New upstream release 4.3.1.

* Sun Aug 30 2009 Raphaël Gertz <rapsys@mandriva.org> 2:4.3.0-7mdv2010.0
+ Revision: 422557
- Rebuild for libtiff

* Tue Aug 18 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.0-5mdv2010.0
+ Revision: 417528
- Rebuild

* Sat Aug 15 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.0-4mdv2010.0
+ Revision: 416602
- Rebuild for new libjpeg

* Wed Aug 12 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.0-3mdv2010.0
+ Revision: 415758
- Rebuild to fix some unknown symbols

* Mon Aug 10 2009 Funda Wang <fwang@mandriva.org> 2:4.3.0-2mdv2010.0
+ Revision: 414181
- add qt4-qtdbus as BR
- There is so many applications requires qdbuscpp2xml binary

* Mon Aug 03 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.3.0-1mdv2010.0
+ Revision: 408411
- New upstream release 4.3.0.
- Fix conflicts

* Wed Jul 22 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.2.98-1mdv2010.0
+ Revision: 398576
- Update to KDE 4.3 RC3
- Breaking kdelibs to spit kdelibs-experimental, following upstream.

* Fri Jul 10 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.96-1mdv2010.0
+ Revision: 394139
- Update to Rc2

* Fri Jun 26 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.95-6mdv2010.0
+ Revision: 389533
- Fix file list

* Fri Jun 26 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.95-5mdv2010.0
+ Revision: 389419
- Fix lib ( do not require devel)

* Thu Jun 25 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.95-4mdv2010.0
+ Revision: 389078
- Bump release for missing libsolid4 package

* Thu Jun 25 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.95-3mdv2010.0
+ Revision: 388908
- Fix file list
- Fix patch11
- Rediff patch11
- Update to 4.3 Rc1

* Thu Jun 04 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.90-1mdv2010.0
+ Revision: 382592
- Update to beta2

* Thu May 28 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.88-1mdv2010.0
+ Revision: 380598
- Remove merged patches
- Update to kde 4.2.88
- Use kde team policy naming for patch 101

* Tue May 26 2009 Funda Wang <fwang@mandriva.org> 2:4.2.87-2mdv2010.0
+ Revision: 379785
- add upstream r969968 to fix FindLibKonq.cmake

* Thu May 21 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.87-1mdv2010.0
+ Revision: 378184
- Remove unused patch
- Add kdelibs-experimental as tarball and not as a patch anymore
- FIx file list
- Add a switch to handle ftp snapshots
- Update to kde 4.2.87

* Tue May 12 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.85-5mdv2010.0
+ Revision: 374864
- Add testing patch to mount crypto_LUKS devices

* Sat May 09 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.85-4mdv2010.0
+ Revision: 373655
- move out libknotificationitem-1.so from the devel package

* Fri May 08 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.85-3mdv2010.0
+ Revision: 373463
- Package kdelibs-experimental inside kdelibs4

* Fri May 08 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.85-2mdv2010.0
+ Revision: 373438
- Increase release
- New tarball fixes kdegraphics4 build

* Thu May 07 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.85-1mdv2010.0
+ Revision: 372991
- Remove merged patch
- Update to kde 4.2.85

* Tue May 05 2009 Funda Wang <fwang@mandriva.org> 2:4.2.71-0.svn961800.2mdv2010.0
+ Revision: 372114
- fix xz (lzma) detection, from upstream rev981856

* Sun May 03 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.71-0.svn961800.1mdv2010.0
+ Revision: 371492
- Fix file list
- Update to kde 4.2.71

* Fri May 01 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.70-0.svn954171.2mdv2010.0
+ Revision: 369619
- Fix conflicts

* Wed Apr 29 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.70-0.svn954171.1mdv2010.0
+ Revision: 369152
- Update to kde 4.2.70
  Remove branch patches
  Rediff patches
- Activate patch 210, allow to move folders in the trash

* Thu Apr 23 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.2.2-26mdv2009.1
+ Revision: 368775
- Disable harmfull patches for now. Probable cause in https://qa.mandriva.com/show_bug.cgi?id=50204

* Wed Apr 22 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.2-25mdv2009.1
+ Revision: 368614
- Allow to drag file on a filemanager  opened as root
- [Trunk] Allow to move folder on the trash

* Mon Apr 20 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.2-23mdv2009.1
+ Revision: 368097
- Patch135: make kdeinit really not leak file descriptors to child processes
  Patch136: fix and simplify the child struct disposal the previous patch exposed this problem ...

* Sun Apr 19 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.2-22mdv2009.1
+ Revision: 368078
- Remove patch210 for now

* Sun Apr 19 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.2-21mdv2009.1
+ Revision: 368013
- Add patch210 to fix leaks in kinit

* Sat Apr 18 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.2-20mdv2009.1
+ Revision: 367985
- Fix crash in kdelibs with wrong javascripts

* Thu Apr 16 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.2-19mdv2009.1
+ Revision: 367797
- Add libutempter-devel as BuildRequires

* Sat Apr 11 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.2-18mdv2009.1
+ Revision: 366393
- Add patch133 from branch : Fix widget item delegates to respect the focused widget ( KDE bug #186142)

* Fri Apr 10 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.2-17mdv2009.1
+ Revision: 365558
- Add 2 upstream patches to fix leak and coverity

* Thu Apr 09 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.2-16mdv2009.1
+ Revision: 365460
- Add some upstream patches from branch
        - Patch127: Fixes kickoff closing
        - Patch128: Fixes infinite loop in bidiNext on some websites
        - Patch129: Set continuation to 0 when we actually removed it BKO: 189121
        - Patch130: Backport of revision 951352 from trunk (mostly sorting fixes)

* Wed Apr 08 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.2-15mdv2009.1
+ Revision: 365245
- Add some upstream patches from branch
        - Patch126: Fix the call to KJob::kill when the Cancel button is pressed

* Wed Apr 08 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.2-14mdv2009.1
+ Revision: 365224
- Add some upstream patches from branch
        - Patch124: Don't loop if we get no auth request (that we understand) together with a 401/407 status code.
        - Patch125: Backport commit 950846 with apidox clarifications for result and finished.
- Add some upstream patches from branch
        - Patch119: Add missing mapping for insert key
        - Patch120: Fix two porting bugs
        - Patch121: Fix updating of images from the airport-nuernberg webcam
        - Patch122: Remove some unneded files
        - Patch123: Fix Build with Qt4.4 again

* Mon Apr 06 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.2.2-12mdv2009.1
+ Revision: 364431
- Add safe trunk backport bugfix patches

* Mon Apr 06 2009 Gustavo Pichorim Boiko <boiko@mandriva.com> 2:4.2.2-10mdv2009.1
+ Revision: 364297
- Disable caching of kdeglobals paths. This was breaking the config reading
  from kde profile dirs. (Patch from fedora kdelibs)

* Sun Apr 05 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.2-9mdv2009.1
+ Revision: 364248
- Add upstream patch to fix hovering in folderview

* Sun Apr 05 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.2-8mdv2009.1
+ Revision: 364240
- Add upstream patches from 4.2 branch
    - Khtml fixes
    - emoticones fixes
- Renumber patches
- Really remove kdelibs-4.2.1-iconwidget-keepproportion.patch

* Sat Apr 04 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.2.2-7mdv2009.1
+ Revision: 364002
- Make applications built against qt 4.4 works in runtime against qt 4.5 no loosing internationalization properties

* Fri Apr 03 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.2.2-6mdv2009.1
+ Revision: 363822
- Another upgrade issue for old distros

* Thu Apr 02 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.2.2-5mdv2009.1
+ Revision: 363582
- Inverted test makes all distros below 2009.1 wrongly remove kdelibs-common

* Tue Mar 31 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.2.2-4mdv2009.1
+ Revision: 363099
- Another lzma patch fix
- Update with Try#3 kdelibs package with recent KFilterDev fixes

* Tue Mar 31 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.2.2-3mdv2009.1
+ Revision: 363018
- Small change to avoid headaches in upgrade

* Tue Mar 31 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.2.2-2mdv2009.1
+ Revision: 362786
- Update with Try#2 tarball

* Fri Mar 27 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.2.2-1mdv2009.1
+ Revision: 361594
- Upgrade to KDE 4.2.2 try#1 packages.

* Wed Mar 25 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.1-15mdv2009.1
+ Revision: 361161
- Fix previous commit
- Try to fix Bug 49069

* Tue Mar 17 2009 Arthur Renato Mello <arthur@mandriva.com> 2:4.2.1-13mdv2009.1
+ Revision: 356624
- Add patch for Plasma::Svg cache. This should fix the MDV menu button update after a svg change.
- Remove keepProportion patch since we do not use it on MDV button anymore.

* Tue Mar 17 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.1-12mdv2009.1
+ Revision: 356611
- More obsoletes to ease upgrade

* Mon Mar 16 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.1-11mdv2009.1
+ Revision: 355927
- Fix obsoletes in kdelibs-common

* Sun Mar 15 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.1-10mdv2009.1
+ Revision: 355560
- [Branch] Fix encoding pb ( regression from upstream r931769)
- Fix text
- Fix spelling

* Wed Mar 04 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.2.1-9mdv2009.1
+ Revision: 348293
- Backport utf8 dir work made upstream against qt 4.5 compilations

* Tue Mar 03 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.2.1-7mdv2009.1
+ Revision: 347968
- Added some nice about

* Tue Mar 03 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.2.1-6mdv2009.1
+ Revision: 347837
- Fix for bug https://qa.mandriva.com/show_bug.cgi?id=48348. Backport will be added in 4.2 branch too.

* Mon Mar 02 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.2.1-5mdv2009.1
+ Revision: 347537
- Backporting upstream commit spotted by Thiago, about duplication of mimetypes.
  This was the real cause of crashing on initial update, and Mandriva was suffering from
  dynamic inroduced system mimetypes protocols. This commit prevents this situations.

* Mon Mar 02 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.1-4mdv2009.1
+ Revision: 346863
- Use back keepproportion patch from 4.2.0

* Sat Feb 28 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.1-3mdv2009.1
+ Revision: 346137
- Revert commit 921138, should workaround the crash

* Fri Feb 27 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.2.1-2mdv2009.1
+ Revision: 345648
- Try#1 updated tarball

* Fri Feb 27 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.2.1-1mdv2009.1
+ Revision: 345541
- KDE 4.2.1 try#1 upstream release

* Wed Feb 25 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.2.0-15mdv2009.1
+ Revision: 344987
- Added knotify 4.2.1 backport patch to fix current qt 4.5 notofication issues

* Tue Feb 24 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.0-14mdv2009.1
+ Revision: 344338
- Fix typo
- [branch] Removed applets do not reappear at kde start
- Remove patch108 for now, will be rediff later
- Fix patch level
- Fix write of plasma conf files

* Tue Feb 17 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.0-12mdv2009.1
+ Revision: 341166
- Fix upstream bug176280 when resizing plasma bar

* Mon Feb 16 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.0-11mdv2009.1
+ Revision: 340854
- Rebuild against qt4.5

* Fri Feb 13 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.0-10mdv2009.1
+ Revision: 339966
- Fix patch 8
- Use patch from fedora to remove a workaround for a qt 4.4 bug

  + Gustavo Pichorim Boiko <boiko@mandriva.com>
    - Fix a crash in konqueror when opening big web pages (bug #47226)
      Patch from Daniel Pestana de Gouveia.

* Sat Jan 31 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.0-7mdv2009.1
+ Revision: 335749
- Add a  testing patch to fix khtml rendering of linuxtoday

* Sat Jan 31 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.0-6mdv2009.1
+ Revision: 335748
- Add some fixes from branch

* Fri Jan 30 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.0-5mdv2009.1
+ Revision: 335649
- Fix kded regression

* Fri Jan 30 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.0-4mdv2009.1
+ Revision: 335405
- Revert upstream commit 914158 ( to try to fix kded issues )

* Thu Jan 29 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.2.0-3mdv2009.1
+ Revision: 335309
- Update with current nepomuk trunk as requested by Nepomuk development team

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - if we're going to add a versioned build dependency on liblzma-devel, we might
      as well add more proper version requirement..

* Mon Jan 26 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.2.0-2mdv2009.1
+ Revision: 333866
- Update with 4.2.0 upstream final tarball

* Mon Jan 26 2009 Arthur Renato Mello <arthur@mandriva.com> 2:4.2.0-1mdv2009.1
+ Revision: 333775
- Add support to keep proportion in plasma icons
- Backport patch rev915328. Fix size info for svg

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Update cacert (Bug #47282)

  + Helio Chissini de Castro <helio@mandriva.com>
    - Added first try 4.2.0 final tarball

* Thu Jan 22 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.1.96-7mdv2009.1
+ Revision: 332507
- Added nepomuk backport, based on trunk, as requested for Nepomuk devels
- Cleanup spec for old distros

* Fri Jan 16 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.96-5mdv2009.1
+ Revision: 330052
- Not needed anymore with latest cmake

* Sun Jan 11 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.96-4mdv2009.1
+ Revision: 328423
- Fix a crash (appearing in KSMServer) which is partly a Qt bug and partly an odd SVG

* Fri Jan 09 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.96-3mdv2009.1
+ Revision: 327460
- Fix kdebase4-workspace detection

* Fri Jan 09 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.96-2mdv2009.1
+ Revision: 327325
- Fix kdepimlibs detection

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - update lzma filter patch with xz support, renaming it to kxzfilter..

* Thu Jan 08 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.96-1mdv2009.1
+ Revision: 327199
- Definitivly fix file list
- Remove last bit of kformula
- Remove %%lib require in the devel package
- Fix filelist
- Remove merged patches
  Rediff Patch5

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update with Release Candidate 1 - 4.1.96

* Sun Jan 04 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.85-8mdv2009.1
+ Revision: 324904
- More filesharing fixes
- Add patch from BKO160221 to not crash when hal is OFF

* Sun Jan 04 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.85-7mdv2009.1
+ Revision: 324718
- Hack to fix build
- fix debug
- More filesharing fixes
- Fix filesharing patch
- Allow to unshare a folder

* Tue Dec 23 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.85-5mdv2009.1
+ Revision: 317771
- Allow to share files again

* Mon Dec 22 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.85-4mdv2009.1
+ Revision: 317723
- Bump release
- Add patch to help upstream to debug some file association bugs

* Tue Dec 16 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.85-3mdv2009.1
+ Revision: 314997
- New kdelibs tarball fixing translation build error ( like es )

* Sun Dec 14 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.85-2mdv2009.1
+ Revision: 314074
- carefully save applets on creation, prevents losing new applets right after adding them

* Fri Dec 12 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.85-1mdv2009.1
+ Revision: 313748
- Fix kde menu patch

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update with Beta 1 - 4.1.85

* Wed Dec 10 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.82-1mdv2009.1
+ Revision: 312606
- Update to kde 4.1.82

* Sun Nov 30 2008 Funda Wang <fwang@mandriva.org> 2:4.1.81-1mdv2009.1
+ Revision: 308361
- New version 4.1.81
- rediff iaora patch
- drop upstream patch

* Tue Nov 25 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.80-10mdv2009.1
+ Revision: 306507
- Fix and Apply patch5

* Tue Nov 25 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.80-9mdv2009.1
+ Revision: 306491
- Do not apply patch5, need more work
- Remove merged patches
  Add patch103: initialize this value, that's why toolbox sometimes was going to left in an unpredictable way
- Add back menu-button-plasma-icon.patch

  + Helio Chissini de Castro <helio@mandriva.com>
    - Updated with fresh beta 1 official fixed tarball

  + Funda Wang <fwang@mandriva.org>
    - bring back kde4-style-iaora requires

* Sat Nov 22 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.80-7mdv2009.1
+ Revision: 305820
- backport patches from tags/4.1.80

  + Funda Wang <fwang@mandriva.org>
    - requires_exceptions is of no use here

* Sat Nov 22 2008 Funda Wang <fwang@mandriva.org> 2:4.1.80-6mdv2009.1
+ Revision: 305696
- disable provides for devel(libkephal), as it is not the cause of selecting
  kdebase4-workspace-devel
- disable requires on kde4-style-iaora, it is pulling libkdecoreations ->
  libkephal. Need to re-add after fixing kdebase-workspace.

* Sat Nov 22 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.80-5mdv2009.1
+ Revision: 305667
- Dirty hack to allow to install kdelibs4-devel
- Add libxml2-utils as BuildRequires

* Sat Nov 22 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.80-4mdv2009.1
+ Revision: 305624
- Try to remove wrong require on kdelibs4

* Fri Nov 21 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.80-3mdv2009.1
+ Revision: 305387
- Rebuild

* Thu Nov 20 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.80-2mdv2009.1
+ Revision: 305337
- Add missing patch
- Do not use translation patch for the moment ( seems broken)

* Wed Nov 19 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.80-1mdv2009.1
+ Revision: 304618
- Fix file list

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update with Beta 1 - 4.1.80

* Thu Nov 13 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.73-9mdv2009.1
+ Revision: 302680
- Add conflicts because of plasma move

* Thu Nov 13 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.73-8mdv2009.1
+ Revision: 302670
- Fix epoch in requires
  Add back plasma-devel provides ( was in kdebase4-workspace before )
- Remove cmake buildrequires ( already required by kde4-macros)
  Fix Versionnate on kde4-macros

* Thu Nov 13 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.73-7mdv2009.1
+ Revision: 302630
- Fix Requires on %%libkdeui
- Add epoch because of plasma move
- Update to kde 4.1.73
  Say hello to plasma in kdelibs
- Change libknewstuff2 name according to library policy
- Add back default kde menu ( step  1 )
- Fix conflict
- Fix File list

* Fri Oct 24 2008 Per Øyvind Karlsen <peroyvind@mandriva.org> 4.1.71-3mdv2009.1
+ Revision: 296991
- regenerate lzma patch:
  	o fix build with kdelibs 4.1.71
  	o fix build with liblzma 4.999.6
  	o improve lzma cmake file
- fix man page suffix stuff in %%files

* Fri Oct 24 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.1.71-2mdv2009.1
+ Revision: 296872
- Add conflicts

* Thu Oct 23 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.1.71-1mdv2009.1
+ Revision: 296836
- New version 4.1.71

* Wed Oct 22 2008 Gustavo Pichorim Boiko <boiko@mandriva.com> 4.1.70-2mdv2009.1
+ Revision: 296471
- Add some missing conflicts

* Sun Oct 19 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.1.70-1mdv2009.1
+ Revision: 295416
- Add back wrongly removed file
- Update to kde 4.1.70

* Thu Oct 02 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.1.2-5mdv2009.0
+ Revision: 290927
- Add upstream patch revision 867092 to fix dolphin crash when in zip files

* Mon Sep 29 2008 Helio Chissini de Castro <helio@mandriva.com> 4.1.2-4mdv2009.0
+ Revision: 289899
- Fortify translation patch to avoid empty strings

* Mon Sep 29 2008 Helio Chissini de Castro <helio@mandriva.com> 4.1.2-3mdv2009.0
+ Revision: 289776
- Add automatic translation for Name, GenericName and Description on desktop files

* Mon Sep 29 2008 Helio Chissini de Castro <helio@mandriva.com> 4.1.2-2mdv2009.0
+ Revision: 289369
- Add menu catalogs

* Thu Sep 25 2008 Helio Chissini de Castro <helio@mandriva.com> 4.1.2-1mdv2009.0
+ Revision: 288191
- KDE 4.1.2 arriving.

* Thu Sep 18 2008 Helio Chissini de Castro <helio@mandriva.com> 4.1.1-9mdv2009.0
+ Revision: 285657
- khtml post branch patch

* Tue Sep 16 2008 Helio Chissini de Castro <helio@mandriva.com> 4.1.1-8mdv2009.0
+ Revision: 285189
- file dialog fixes from post branch.

* Mon Sep 15 2008 Helio Chissini de Castro <helio@mandriva.com> 4.1.1-7mdv2009.0
+ Revision: 285065
- khtml nvidia artifacts post branch fix.

* Tue Sep 09 2008 Helio Chissini de Castro <helio@mandriva.com> 4.1.1-6mdv2009.0
+ Revision: 283261
- Fix for mimetype bug https://qa.mandriva.com/show_bug.cgi?id=43625 ( already upstream )
- Moved post 4.1.1 patches to over 100 numbering
- Renamed patch name to match other backports

* Tue Sep 09 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.1.1-5mdv2009.0
+ Revision: 282853
- Use vfat with correct codepages

* Thu Sep 04 2008 Helio Chissini de Castro <helio@mandriva.com> 4.1.1-4mdv2009.0
+ Revision: 280714
- Thanks to Mr. Ktuberling and bug https://qa.mandriva.com/show_bug.cgi?id=43502

* Mon Sep 01 2008 Götz Waschk <waschk@mandriva.org> 4.1.1-3mdv2009.0
+ Revision: 278412
- rebuild for new libdvdread

* Sat Aug 30 2008 Helio Chissini de Castro <helio@mandriva.com> 4.1.1-2mdv2009.0
+ Revision: 277606
- Update 4.1.1 tarballs. Reverted sonnet changes

* Thu Aug 28 2008 Helio Chissini de Castro <helio@mandriva.com> 4.1.1-1mdv2009.0
+ Revision: 277049
- Upgrade to forthcoming 4.1.1 packages

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Apply this patch after update to kde 4.1.1
    - Fix source highlighting refresh problems (Bug #42721)

* Tue Aug 19 2008 Helio Chissini de Castro <helio@mandriva.com> 4.1.0-15mdv2009.0
+ Revision: 274012
- Use iaora as default for now. Need be replaced with proper solution

* Mon Aug 18 2008 Helio Chissini de Castro <helio@mandriva.com> 4.1.0-13mdv2009.0
+ Revision: 273390
- Daily branch patch updates

* Sat Aug 16 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.1.0-12mdv2009.0
+ Revision: 272516
- Backport patch202 from trunk ( needed by nepomuk-kde)

* Tue Aug 12 2008 Helio Chissini de Castro <helio@mandriva.com> 4.1.0-11mdv2009.0
+ Revision: 271130
- Daily branch patch update

* Thu Aug 07 2008 Helio Chissini de Castro <helio@mandriva.com> 4.1.0-10mdv2009.0
+ Revision: 266729
- Update with latest backport from xdg-user-dirs now using qt standards
- Profile is only suitable for distro lower than 2009

* Wed Aug 06 2008 Helio Chissini de Castro <helio@mandriva.com> 4.1.0-7mdv2009.0
+ Revision: 264346
- Daily branch patch updates
- Added backport of xdg user dirs patch

* Mon Aug 04 2008 Helio Chissini de Castro <helio@mandriva.com> 4.1.0-6mdv2009.0
+ Revision: 263220
- More patch mess fixes

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Use better naming for backport patches from trunk

* Mon Aug 04 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.1.0-5mdv2009.0
+ Revision: 263014
- Add patch131 that add kdiskfreespaceinfo class needed for nepomuk backport

* Mon Aug 04 2008 Helio Chissini de Castro <helio@mandriva.com> 4.1.0-4mdv2009.0
+ Revision: 262838
- Update with current branch 4.1 patches

* Wed Jul 30 2008 Helio Chissini de Castro <helio@mandriva.com> 4.1.0-3mdv2009.0
+ Revision: 255166
- kdecore should requires phonon-backend >= 4.2

* Tue Jul 29 2008 Helio Chissini de Castro <helio@mandriva.com> 4.1.0-2mdv2009.0
+ Revision: 253814
- Start updates from post 4.1.0 branch on cooker only. All patches comes with full description inside.

* Thu Jul 24 2008 Helio Chissini de Castro <helio@mandriva.com> 4.1.0-1mdv2009.0
+ Revision: 247361
- Update with Release Candidate 1 - 4.1.0

* Tue Jul 22 2008 Per Øyvind Karlsen <peroyvind@mandriva.org> 4.0.98-6mdv2009.0
+ Revision: 240867
- bump release
- add lzma filter (P3)

* Tue Jul 15 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0.98-5mdv2009.0
+ Revision: 236218
- Fix to boost detection

* Tue Jul 15 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0.98-4mdv2009.0
+ Revision: 236040
- Latest fix for translations

* Mon Jul 14 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0.98-3mdv2009.0
+ Revision: 234668
- rc1 upstream tarball updated with l10n latest hour fixes

* Fri Jul 11 2008 Olivier Blin <blino@mandriva.org> 4.0.98-2mdv2009.0
+ Revision: 233707
- move kde pam files to kdm package (used by kdm only, and provided upstream in kdebase-workspace)

* Thu Jul 10 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0.98-1mdv2009.0
+ Revision: 233179
- Update with Release Candidate 1 - 4.0.98

* Wed Jul 09 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0.85-2mdv2009.0
+ Revision: 233030
- Added kde-np to allow autologin with clean password

* Sun Jul 06 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.0.85-1mdv2009.0
+ Revision: 232302
- Update to kde 4.0.85
- Add extra dir on $PATH for mdv <= 200810
  Add patch that add extra catalogs ( will be need for desktop file translations )

* Fri Jun 27 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0.84-1mdv2009.0
+ Revision: 229411
- Added kwallet daemon
- Update with new snapshot tarballs 4.0.84

* Fri Jun 20 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0.83-2mdv2009.0
+ Revision: 227358
- Add ld.so.conf for 2008.1

* Thu Jun 19 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0.83-1mdv2009.0
+ Revision: 226853
- Update with new snapshot tarballs 4.0.83

  + Anssi Hannula <anssi@mandriva.org>
    - add another conflict to ensure smooth upgrade

* Thu Jun 12 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0.82-5mdv2009.0
+ Revision: 218624
- Missing requires for lang and config files

* Thu Jun 12 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0.82-3mdv2009.0
+ Revision: 218533
- Let's specify all br as a requires for devel package, allow applications not miss new things like xpm and xft2 splitted

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix typo

* Wed Jun 11 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0.82-1mdv2009.0
+ Revision: 217964
- Update with new snapshot tarballs 4.0.82

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Jun 03 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0.81-5mdv2009.0
+ Revision: 214697
- Update with new snapshot tarballs 4.0.81
- Update with new snapshot tarballs %%{VERSION}
- Rebuild against new qca2

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Remove unneeded obsoletes %%libkaudiodevicelist have not been removed but it just moved to kdebase4-runtime
    - Add back removed obsoletes

* Thu May 29 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.0.81-1mdv2009.0
+ Revision: 213170
- KDE 4.0.8
- Fix File list for new snapshot ( phonon is gone away on its own package )

* Wed May 28 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0.80-4mdv2009.0
+ Revision: 212825
- Recompile against changes on qt libraries placement

* Mon May 26 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0.80-3mdv2009.0
+ Revision: 211430
- We don't need this anymore. Having /usr/lib on ld is useless since is the system path.

* Sun May 25 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.0.80-2mdv2009.0
+ Revision: 211067
- Fix Requires on devel package
- Add Automoc as Requires

* Sat May 24 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0.80-1mdv2009.0
+ Revision: 210806
- New upstream kde4 4.1 beta1
- New upstream kde4 4.1 beta1

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - More owned folders
    - Own %%_kde_appsdir/knewstuff
    - Own %%_kde_appsdir/ksgmltools2
    - Own %%_kde_appsdir/kssl
    - Own %%_kde_appsdir/ktexteditor_kdatatool %%_kde_appsdir/ktexteditor_insertfile and %%_kde_appsdir/ktexteditor_docwordcompletion
    - Own %%_kde_appsdir/libphonon
    - Own %%_kde_appsdir/LICENSES
    - Own %%_kde_appsdir/nepomuk
    - Own %%_kde_appsdir/phonon
    - Own %%_kde_appsdir/proxyscout
    - fix file list
    - Fix 'folder ownage
    - Fix obsoletes

* Mon May 19 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.0.74-3mdv2009.0
+ Revision: 209211
- Add an obsolete for libnepomuk-middleware4

* Fri May 16 2008 Funda Wang <fwang@mandriva.org> 4.0.74-2mdv2009.0
+ Revision: 208067
- Requires automoc (since most of kde4 packages BR automoc)

* Fri May 16 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.0.74-1mdv2009.0
+ Revision: 208017
- Fix BuildRequires
- Update to kde 4.0.74

* Tue May 13 2008 Anssi Hannula <anssi@mandriva.org> 4.0.73-4mdv2009.0
+ Revision: 206691
- Fix versioned conflicts on kjsembed

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix conflicts

* Sun May 11 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.0.73-3mdv2009.0
+ Revision: 205510
- Clean conflicts

* Thu May 08 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.0.73-2mdv2009.0
+ Revision: 204027
- Rebuild because of bs failure

* Wed May 07 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.0.73-1mdv2009.0
+ Revision: 203719
- a new week, a new snapshot => 4.0.73

* Thu May 01 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.0.72-1mdv2009.0
+ Revision: 199779
- Update to kde 4.0.72
- Fix versionate BR
- New week-end New snapshot 4.0.70
- New snapshot 4.0.69
- New snapshot  4.0.68
- Fix File list

  + Helio Chissini de Castro <helio@mandriva.com>
    - New upstream kde4 4.1 alpha 1
    - applictions.menu comes from mandriva specified
    - Starting to push new infrastructure for devel KDE 4.1. KDE 4 will be on / now. KDE is dead. Long live KDE vi kdenetwork4/SPECS/kdenetwork4.spec ;-)

* Fri Mar 28 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0.3-1mdv2008.1
+ Revision: 190965
- Update for last stable release 4.0.3
- Update for last stable release 4.0.3

* Sun Mar 09 2008 Anssi Hannula <anssi@mandriva.org> 4.0.2-7mdv2008.1
+ Revision: 182728
- replace requires on aspell with suggests on enchant-dictionary as
  kde4 uses libenchant that supports other backends as well

* Sat Mar 08 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.0.2-6mdv2008.1
+ Revision: 182096
- Rebuild against new qt4 changes

  + Helio Chissini de Castro <helio@mandriva.com>
    - New upstream bugfix release 4.0.2

* Sat Mar 01 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0.2-5mdv2008.1
+ Revision: 177247
- Update for upstream upcoming 4.0.2

* Wed Feb 20 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0.1-5mdv2008.1
+ Revision: 173196
- Update nepomuk with trunk modifications. Requested by nepomuk maintainer, Sebastian Trueg

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix patch0 to use more .kde4
      Add patch2 to see kde3 applications of the menu

* Tue Feb 12 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.0.1-3mdv2008.1
+ Revision: 165671
- Rebuild

* Fri Feb 08 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0.1-2mdv2008.1
+ Revision: 164253
- Rebuild against stable cmake

* Thu Feb 07 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0.1-1mdv2008.1
+ Revision: 163746
- Default apidocs generation is off. Resulting package is too big and not often required except for developers. Final install can reach 605 mb.
- Updating for stable KDE 4.0.1
- No more branches. From now, we will be using the monthly official KDE tarballs, as discussed by Mandriva KDE team

* Sun Jan 27 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.0.0-5.765596.2mdv2008.1
+ Revision: 158534
- Fix kde4env.sh and do not use it as source anymore ( because of wrong use of libs )
  (Regression introduced on revision 93342)
- Add back kde4.conf in ld.conf
- Reordering file list

* Thu Jan 24 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0.0-5.765596.1mdv2008.1
+ Revision: 157562
- Update for today branch adding nepomuk changes from trunk

* Wed Jan 23 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0.0-5.765238.1mdv2008.1
+ Revision: 157184
- Update from branch 4.0.1
- Added nepomuk kdelibs patch ( generated from trunk ( provided by Sebastian Tr?\195?\188eg )

* Tue Jan 22 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.0.0-5mdv2008.1
+ Revision: 156656
- Finally fix file list ( move back lib files in devel)
- Fix conflict
- Move files out of devel package

* Sat Jan 19 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.0.0-4mdv2008.1
+ Revision: 155103
- Fix File list
  Own some directories

  + Anssi Hannula <anssi@mandriva.org>
    - ensure major correctness

  + Helio Chissini de Castro <helio@mandriva.com>
    - fix pam for kde4 apps ( sorry neoclust, need to do it faster ) :-)

* Wed Jan 09 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.0.0-1mdv2008.1
+ Revision: 147401
- Fix release on stable

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update for official tarball

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sun Dec 23 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.97.1-0.751982.1mdv2008.1
+ Revision: 137310
- new snapshot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Dec 10 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.97.1-0.746866.1mdv2008.1
+ Revision: 117009
- New snapshot
  Fix BuildRequires on soprano

* Wed Dec 05 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.97.0-0.745252.1mdv2008.1
+ Revision: 115784
- KDE4 Rc2

* Thu Nov 29 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.96.1-0.742999.1mdv2008.1
+ Revision: 113940
- New snapshot

* Tue Nov 27 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.96.1-0.742334.1mdv2008.1
+ Revision: 113531
- New snapshot
  Remove Patch1 : Merged upstream

* Tue Nov 27 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.96.1-0.741480.2mdv2008.1
+ Revision: 113478
- Add patch  1 to fix bug 35603 ( empy page when logging in bugzilla)

  + Thierry Vignaud <tv@mandriva.org>
    - explain require on libxml2-utils

* Sun Nov 25 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.96.1-0.741480.1mdv2008.1
+ Revision: 111956
- New Snapshot
  Add back ld.so.conf.d/kde4.conf

  + Funda Wang <fwang@mandriva.org>
    - add requires on libxml2-utils, as when building most kde applications,
      it will call xmllint to validate the docbook files.

* Thu Nov 22 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.96.1-0.739810.1mdv2008.1
+ Revision: 111136
- New Snapshot

* Thu Nov 15 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.96.0-0.737190.1mdv2008.1
+ Revision: 108964
- Kde 4 RC1

* Sat Nov 10 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.95.2-0.734845.2mdv2008.1
+ Revision: 107454
- Remove Requires(pre)

* Sat Nov 10 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.95.2-0.734845.1mdv2008.1
+ Revision: 107419
+ rebuild (emptylog)

* Fri Nov 09 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.95.2-0.733956.1mdv2008.1
+ Revision: 107256
- New snapshot ( say hello back to nepomuk )

  + Funda Wang <fwang@mandriva.org>
    - Revert changes as there are already commented out ld.so.conf.d lines
    - add /opt/kde4/lib{,64} into ld.so.conf.d

* Thu Nov 01 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.95.1-0.731775.1mdv2008.1
+ Revision: 104752
- New snapshot post Rc1

* Tue Oct 30 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.94.1-0.730890.1mdv2008.1
+ Revision: 103685
- New snapshot

* Wed Oct 24 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.94.1-0.728975.1mdv2008.1
+ Revision: 101890
- New svn snapshot

* Tue Oct 23 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.94.1-0.728415.2mdv2008.1
+ Revision: 101503
- Fix file list
- Fix file list ( Kdeprint is dead too )
- Snapshot post BIC

* Tue Oct 23 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.94.1-0.728203.2mdv2008.1
+ Revision: 101369
- Upload because of missing package

* Mon Oct 22 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.94.1-0.728203.1mdv2008.1
+ Revision: 101289
- New snapshot after today BIC day ( and prepare for Kickoff )

* Mon Oct 22 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.94.1-0.727920.1mdv2008.1
+ Revision: 101067
- New svn snapshot

* Sun Oct 21 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.94.1-0.727754.1mdv2008.1
+ Revision: 101037
- Update svn tarball

* Sun Oct 21 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.94.0-0.727618.1mdv2008.1
+ Revision: 100825
- New svn snapshot
- Add requires for translations

* Fri Oct 19 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.94.0-0.726236.2mdv2008.1
+ Revision: 100502
- Fix update

* Wed Oct 17 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.94.0-0.726236.1mdv2008.1
+ Revision: 99598
- New beta 3.94.0

* Wed Oct 17 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.93.0-0.726000.1mdv2008.1
+ Revision: 99437
- New svn snapshot
- New svn snapshot

  + Thierry Vignaud <tv@mandriva.org>
    - fix summary-ended-with-dot

* Thu Sep 27 2007 Tiago Salem <salem@mandriva.com.br> 3.93.0-0.714006.2mdv2008.0
+ Revision: 93400
- Adding kde4env.sh file as Source1
- Bumping release and fixing mime directories
- Adding kde4env.sh as a SOURCE file.
- fixing XDG variables for kde4
- Removing mdv2008.0 from Obsoletes tags.

* Wed Sep 19 2007 Tiago Salem <salem@mandriva.com.br> 3.93.0-0.714006.1mdv2008.0
+ Revision: 91190
- Making Obsoletes tags versioned

* Fri Sep 14 2007 Helio Chissini de Castro <helio@mandriva.com> 3.93.0-0.712507.1mdv2008.0
+ Revision: 85720
- Update with revision 712507
- Wrong source

* Wed Sep 12 2007 Helio Chissini de Castro <helio@mandriva.com> 3.93.0-0.711712.1mdv2008.0
+ Revision: 84803
- Update with revision 711712
- Update with revision 711596

* Wed Sep 05 2007 Helio Chissini de Castro <helio@mandriva.com> 3.93.0-0.708831.1mdv2008.0
+ Revision: 80452
- Update with revision 708831

* Wed Sep 05 2007 Helio Chissini de Castro <helio@mandriva.com> 3.93.0-0.708644.1mdv2008.0
+ Revision: 80120
- Update with revision 708644

* Tue Sep 04 2007 Helio Chissini de Castro <helio@mandriva.com> 3.93.0-0.708165.1mdv2008.0
+ Revision: 78992
- Update with revision 708165

* Sat Sep 01 2007 Helio Chissini de Castro <helio@mandriva.com> 3.93.0-0.707068.1mdv2008.0
+ Revision: 77321
- Update with revision 707068

* Thu Aug 30 2007 Helio Chissini de Castro <helio@mandriva.com> 3.92.0-0.706494.1mdv2008.0
+ Revision: 75991
- Update with revision 706494

* Wed Aug 29 2007 Helio Chissini de Castro <helio@mandriva.com> 3.92.0-0.706278.1mdv2008.0
+ Revision: 75026
- Update with revision 706278

* Wed Aug 29 2007 Helio Chissini de Castro <helio@mandriva.com> 3.92.0-0.705911.1mdv2008.0
+ Revision: 73297
- Update with revision 705911

* Tue Aug 28 2007 Helio Chissini de Castro <helio@mandriva.com> 3.92.0-0.705398.1mdv2008.0
+ Revision: 72277
- Update with revision 705398

* Mon Aug 27 2007 Helio Chissini de Castro <helio@mandriva.com> 3.92.0-0.705301.1mdv2008.0
+ Revision: 72139
- Update with revision 705301

* Sat Aug 25 2007 Helio Chissini de Castro <helio@mandriva.com> 3.92.0-0.704641.1mdv2008.0
+ Revision: 71431
- Update with revision 704641

* Fri Aug 24 2007 Helio Chissini de Castro <helio@mandriva.com> 3.92.0-0.704401.1mdv2008.0
+ Revision: 71057
- Update with revision 704401

* Tue Aug 21 2007 Helio Chissini de Castro <helio@mandriva.com> 3.92.0-0.702914.1mdv2008.0
+ Revision: 68461
- Update with revision 702914

* Thu Aug 16 2007 Helio Chissini de Castro <helio@mandriva.com> 3.92.0-0.700801.1mdv2008.0
+ Revision: 64502
- Updated for revision 700801

* Mon Aug 13 2007 Helio Chissini de Castro <helio@mandriva.com> 3.92.0-0.699624.1mdv2008.0
+ Revision: 62812
- Update for revision 699624
- Oxygen theme moved for kdebase.

* Wed Aug 08 2007 Helio Chissini de Castro <helio@mandriva.com> 3.92.0-0.698012.1mdv2008.0
+ Revision: 60550
- Update for release 698012

* Wed Aug 01 2007 Helio Chissini de Castro <helio@mandriva.com> 3.92.0-0.695277.1mdv2008.0
+ Revision: 57810
- Update to revision 695277
- Update for revision 694683
- Updated to revision 694510

* Fri Jul 27 2007 Helio Chissini de Castro <helio@mandriva.com> 3.92-0.693023.1mdv2008.0
+ Revision: 56201
- Update for revision 693023

* Mon Jul 23 2007 Helio Chissini de Castro <helio@mandriva.com> 3.91-0.691408.1mdv2008.0
+ Revision: 54813
- Update from revision 691408
- Update to revision 690298

* Tue Jul 17 2007 Helio Chissini de Castro <helio@mandriva.com> 3.91-0.688867.1mdv2008.0
+ Revision: 52862
- Fix soname for many libraries. Back to 4
- Fix soname for solid

* Mon Jul 16 2007 Helio Chissini de Castro <helio@mandriva.com> 3.91-0.688734.1mdv2008.0
+ Revision: 52693
- Fix lnusertemp calls ( silly packager :-)
- Update to revision 688734

* Thu Jul 12 2007 Helio Chissini de Castro <helio@mandriva.com> 3.91-0.687061.1mdv2008.0
+ Revision: 51683
- Update for revision 687061
- Make kde4env available for system

* Wed Jul 11 2007 Helio Chissini de Castro <helio@mandriva.com> 3.91-0.686496.1mdv2008.0
+ Revision: 51377
- Removed duplicated sources
- Moved kde4env to kdelibs, and disabled ld.so.conf entry to avoid kde3 lib loading ( neoclust )
- Removed duplicate file list on designer plugins ( adamw )
- Updated for recent kdelibs revision

* Wed Jul 11 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.91-0.686439.1mdv2008.0
+ Revision: 51237
-New svn snapshot

* Mon Jul 09 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.91-0.685748.1mdv2008.0
+ Revision: 50714
- New svn snaphot

* Thu Jul 05 2007 Helio Chissini de Castro <helio@mandriva.com> 3.91-0.683569.1mdv2008.0
+ Revision: 48550
- Update at revision 683569

* Tue Jul 03 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.91-0.682628.1mdv2008.0
+ Revision: 47459
- New snaphot after BIC

* Mon Jul 02 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.91-0.682420.1mdv2008.0
+ Revision: 47241
- New snapshot
  Fix dbus path

* Mon Jul 02 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.91-0.682345.1mdv2008.0
+ Revision: 47171
- New snapshot

* Wed Jun 27 2007 Helio Chissini de Castro <helio@mandriva.com> 3.91-0.680966.1mdv2008.0
+ Revision: 45037
- And we're going to alpha2

* Wed Jun 27 2007 Helio Chissini de Castro <helio@mandriva.com> 3.90.2-0.680680mdv2008.0
+ Revision: 44824
- Update from svn

* Tue Jun 26 2007 Helio Chissini de Castro <helio@mandriva.com> 3.90.2-0.680441mdv2008.0
+ Revision: 44452
- Update for revision 680441. May conflicts with current kdebase4-devel package, but new upcoming version is arriving soon and we're still alpha..

* Tue Jun 26 2007 Helio Chissini de Castro <helio@mandriva.com> 3.90.2-0.680284mdv2008.0
+ Revision: 44220
- Update for post BIC monday revision 680284

* Mon Jun 25 2007 Helio Chissini de Castro <helio@mandriva.com> 3.90.2-0.679803mdv2008.0
+ Revision: 43987
- Updating for svn revision 679803
- Update from svn revision 679119

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Remove duplicate file
    - Really add kde4-config on the packages

* Thu Jun 21 2007 Helio Chissini de Castro <helio@mandriva.com> 3.90.2-0.678253mdv2008.0
+ Revision: 41961
- Update for current svn
- Fix bug http://qa.mandriva.com/show_bug.cgi?id=31504

* Tue Jun 19 2007 Helio Chissini de Castro <helio@mandriva.com> 3.90.2-0.677520mdv2008.0
+ Revision: 41464
- Another daily update. Now with automoc working.

* Mon Jun 18 2007 Helio Chissini de Castro <helio@mandriva.com> 3.90.2-0.677229mdv2008.0
+ Revision: 41111
- Update with current svn. Removing duplicates on file list

* Sun Jun 17 2007 Helio Chissini de Castro <helio@mandriva.com> 3.90.2-0.676703mdv2008.0
+ Revision: 40547
- Update for latest svn 676703.
- Oxygen set is available now

* Sat Jun 16 2007 Helio Chissini de Castro <helio@mandriva.com> 3.90.2-0.676122mdv2008.0
+ Revision: 40326
- Bring icons back to root /opt/kde3
- Oxygen style added

* Fri Jun 15 2007 Helio Chissini de Castro <helio@mandriva.com> 3.90.2-0.675929mdv2008.0
+ Revision: 40108
- Update for revision 675929
- Added hicolor and crystalsvg legacy icons under /opt/kde4/share/icons

* Thu Jun 14 2007 Helio Chissini de Castro <helio@mandriva.com> 3.90.2-0.675664mdv2008.0
+ Revision: 39786
- Update for latest svn checkout. Nepomuk change library name

* Sat Jun 09 2007 Helio Chissini de Castro <helio@mandriva.com> 3.90.2-0.673230mdv2008.0
+ Revision: 37717
- Updated for revision 673230
- Fixed devel file list
- Fixed requires for devel package

* Fri Jun 08 2007 Helio Chissini de Castro <helio@mandriva.com> 3.90.2-0.672878mdv2008.0
+ Revision: 37503
- New kdelibs 4 package layout and everything.
- We're trying to get rid of ugly epoch
- Splitted libraries ( yes folks, put everything in one basket never is a good idea, got it ? )
- Requires new kde macros package, to make stupid easily build kde4 packages
- Updated for recent svn code ( as requested by Sebastian Trueg )
- Moved icons to oxygen-icon-theme in /usr/share/icons as standard
- Make kde4 homedir as .kde4 ( borrow opensuse minor patch )
- Removed all old patches that still are commented in spec just to make us confuse :-)

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix File list
    - New Svn Snapshot

* Wed May 09 2007 Laurent Montel <lmontel@mandriva.org> 30000000:3.90.1-0.20070502.1mdv2008.0
+ Revision: 25429
- Fix release
- new snapshot

* Wed May 02 2007 Laurent Montel <lmontel@mandriva.org> 30000000:3.80.3-0.20070502.6mdv2008.0
+ Revision: 20473
- Fix buildrequires
- new snapshot
- new snapshot

