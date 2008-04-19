%define compile_apidox 0
%{?_with_apidox: %{expand: %%global compile_apidox 1}}

Name: kdelibs4
Summary: K Desktop Environment - Libraries
Version: 4.0.70
Group: Graphical desktop/KDE
License: ARTISTIC BSD GPL_V2 LGPL_V2 QPL_V1.0
BuildRoot: %_tmppath/%name-%version-%release-root
URL: http://www.kde.org
Release: %mkrel 2
Source:        ftp://ftp.kde.org/pub/kde/stable/%version/src/kdelibs-%version.tar.bz2
Source1: kde.pam
Patch0: kdelibs4-homedir.patch
BuildRequires: kde4-macros
BuildRequires: cmake >= 2.4.5
BuildRequires: qt4-devel >= 4.4.0
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
BuildRequires: soprano-devel >= 2.0.98

Requires:      kde4-l10n

%description 
Libraries for the K Desktop Environment.

#------------------------------------------------	

%define kaudiodevicelist_major 4
%define libkaudiodevicelist %mklibname kaudiodevicelist %kaudiodevicelist_major

%package -n %libkaudiodevicelist
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}kaudiodevicelist5 < 3.93.0-0.714006.1
Obsoletes: %{_lib}cupsdconf4 < 3.93.0-0.728415.2
Obsoletes: %{_lib}kdefx5 < 3.93.0-0.728415.2
Obsoletes: %{_lib}kdeprint_management4 < 3.93.0-0.728415.2
Obsoletes: %{_lib}kdeprint5 < 3.93.0-0.728415.2

%description -n %libkaudiodevicelist
KDE 4 core library.

%post -n %libkaudiodevicelist -p /sbin/ldconfig
%postun -n %libkaudiodevicelist -p /sbin/ldconfig

%files -n %libkaudiodevicelist
%defattr(-,root,root)
%_kde_libdir/libkaudiodevicelist.so.%{kaudiodevicelist_major}*

#------------------------------------------------	

%define kde3support_major 4
%define libkde3support %mklibname kde3support %kde3support_major

%package -n %libkde3support
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}kde3support5 < 3.93.0-0.714006.1
 

%description -n %libkde3support
KDE 4 core library.

%post -n %libkde3support -p /sbin/ldconfig
%postun -n %libkde3support -p /sbin/ldconfig

%files -n %libkde3support
%defattr(-,root,root)
%_kde_libdir/libkde3support.so.%{kde3support_major}*

#------------------------------------------------	

%define kdecore_major 5
%define libkdecore %mklibname kdecore %kdecore_major

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
%_kde_libdir/libkdecore.so.%{kdecore_major}*

#------------------------------------------------	

%define kdefakes_major 5
%define libkdefakes %mklibname kdefakes %kdefakes_major

%package -n %libkdefakes
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= 30000000:3.80.3
 

%description -n %libkdefakes
KDE 4 core library.

%post -n %libkdefakes -p /sbin/ldconfig
%postun -n %libkdefakes -p /sbin/ldconfig

%files -n %libkdefakes
%defattr(-,root,root)
%_kde_libdir/libkdefakes.so.%{kdefakes_major}*

#------------------------------------------------	

%define kdesu_major 5
%define libkdesu %mklibname kdesu %kdesu_major

%package -n %libkdesu
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= 30000000:3.80.3
 

%description -n %libkdesu
KDE 4 core library.

%post -n %libkdesu -p /sbin/ldconfig
%postun -n %libkdesu -p /sbin/ldconfig

%files -n %libkdesu
%defattr(-,root,root)
%_kde_libdir/libkdesu.so.%{kdesu_major}*

#------------------------------------------------	

%define kdeui_major 5
%define libkdeui %mklibname kdeui %kdeui_major

%package -n %libkdeui
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= 30000000:3.80.3
 

%description -n %libkdeui
KDE 4 core library.

%post -n %libkdeui -p /sbin/ldconfig
%postun -n %libkdeui -p /sbin/ldconfig

%files -n %libkdeui
%defattr(-,root,root)
%_kde_libdir/libkdeui.so.%{kdeui_major}*

#------------------------------------------------	

%define kdnssd_major 4
%define libkdnssd %mklibname kdnssd %kdnssd_major

%package -n %libkdnssd
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}kdnssd5 < 3.93.0-0.714006.1
 

%description -n %libkdnssd
KDE 4 core library.

%post -n %libkdnssd -p /sbin/ldconfig
%postun -n %libkdnssd -p /sbin/ldconfig

%files -n %libkdnssd
%defattr(-,root,root)
%_kde_libdir/libkdnssd.so.%{kdnssd_major}*

#------------------------------------------------	

%define kfile_major 4
%define libkfile %mklibname kfile %kfile_major

%package -n %libkfile
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}kfile5 < 3.93.0-0.714006.1
 

%description -n %libkfile
KDE 4 core library.

%post -n %libkfile -p /sbin/ldconfig
%postun -n %libkfile -p /sbin/ldconfig

%files -n %libkfile
%defattr(-,root,root)
%_kde_libdir/libkfile.so.%{kfile_major}*

#------------------------------------------------	

%define khtml_major 5
%define libkhtml %mklibname khtml %khtml_major

%package -n %libkhtml
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= 30000000:3.80.3
 

%description -n %libkhtml
KDE 4 core library.

%post -n %libkhtml -p /sbin/ldconfig
%postun -n %libkhtml -p /sbin/ldconfig

%files -n %libkhtml
%defattr(-,root,root)
%_kde_libdir/libkhtml.so.%{khtml_major}*

#------------------------------------------------	

%define kimproxy_major 4
%define libkimproxy %mklibname kimproxy %kimproxy_major

%package -n %libkimproxy
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}kimproxy5 < 3.93.0-0.714006.1
 

%description -n %libkimproxy
KDE 4 core library.

%post -n %libkimproxy -p /sbin/ldconfig
%postun -n %libkimproxy -p /sbin/ldconfig

%files -n %libkimproxy
%defattr(-,root,root)
%_kde_libdir/libkimproxy.so.%{kimproxy_major}*

#------------------------------------------------	

%define kio_major 5
%define libkio %mklibname kio %kio_major

%package -n %libkio
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= 30000000:3.80.3
 

%description -n %libkio
KDE 4 core library.

%post -n %libkio -p /sbin/ldconfig
%postun -n %libkio -p /sbin/ldconfig

%files -n %libkio
%defattr(-,root,root)
%_kde_libdir/libkio.so.%{kio_major}*

#------------------------------------------------	

%define kjsembed_major 4
%define libkjsembed %mklibname kjsembed %kjsembed_major

%package -n %libkjsembed
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}kjsembed5 < 3.93.0-0.714006.1
 

%description -n %libkjsembed
KDE 4 core library.

%post -n %libkjsembed -p /sbin/ldconfig
%postun -n %libkjsembed -p /sbin/ldconfig

%files -n %libkjsembed
%defattr(-,root,root)
%_kde_libdir/libkjsembed.so.%{kjsembed_major}*

#------------------------------------------------	

%define kjs_major 4
%define libkjs %mklibname kjs %kjs_major

%package -n %libkjs
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}kjs5 < 3.93.0-0.714006.1
 

%description -n %libkjs
KDE 4 core library.

%post -n %libkjs -p /sbin/ldconfig
%postun -n %libkjs -p /sbin/ldconfig

%files -n %libkjs
%defattr(-,root,root)
%_kde_libdir/libkjs.so.%{kjs_major}*

#------------------------------------------------	

%define kmediaplayer_major 4
%define libkmediaplayer %mklibname kmediaplayer %kmediaplayer_major

%package -n %libkmediaplayer
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}kmediaplayer5 < 3.93.0-0.714006.1
 

%description -n %libkmediaplayer
KDE 4 core library.

%post -n %libkmediaplayer -p /sbin/ldconfig
%postun -n %libkmediaplayer -p /sbin/ldconfig

%files -n %libkmediaplayer
%defattr(-,root,root)
%_kde_libdir/libkmediaplayer.so.%{kmediaplayer_major}*

#------------------------------------------------	

%define nepomuk_major 4
%define libnepomuk %mklibname nepomuk %nepomuk_major

%package -n %libnepomuk
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}knepomuk5 < 3.93.0-0.714006.1
Obsoletes: %{_lib}nepomuk5 < 3.93.0-0.714006.1
Obsoletes: %{_lib}kmetadata5 < 3.93.0-0.714006.1
Obsoletes: %{_lib}konto5 < 3.93.0-0.714006.1
Obsoletes: %{_lib}nepomukmiddleware4 < 3.93.0-0.725600.1
 

%description -n %libnepomuk
KDE 4 core library.

%post -n %libnepomuk -p /sbin/ldconfig
%postun -n %libnepomuk -p /sbin/ldconfig

%files -n %libnepomuk
%defattr(-,root,root)
%_kde_libdir/libnepomuk.so.%{nepomuk_major}*

#------------------------------------------------	

%define knewstuff2_major 4
%define libknewstuff2 %mklibname knewstuff2 %knewstuff2_major

%package -n %libknewstuff2
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}knewstuff25 < 3.93.0-0.714006.1
 

%description -n %libknewstuff2
KDE 4 core library.

%post -n %libknewstuff2 -p /sbin/ldconfig
%postun -n %libknewstuff2 -p /sbin/ldconfig

%files -n %libknewstuff2
%defattr(-,root,root)
%_kde_libdir/libknewstuff2.so.%{knewstuff2_major}*

#------------------------------------------------	

%define knotifyconfig_major 4
%define libknotifyconfig %mklibname knotifyconfig %knotifyconfig_major

%package -n %libknotifyconfig
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}knotifyconfig5 < 3.93.0-0.714006.1
 

%description -n %libknotifyconfig
KDE 4 core library.

%post -n %libknotifyconfig -p /sbin/ldconfig
%postun -n %libknotifyconfig -p /sbin/ldconfig

%files -n %libknotifyconfig
%defattr(-,root,root)
%_kde_libdir/libknotifyconfig.so.%{knotifyconfig_major}*

#------------------------------------------------	

%define kntlm_major 4
%define libkntlm %mklibname kntlm %kntlm_major

%package -n %libkntlm
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}kntlm5 < 3.93.0-0.714006.1
 

%description -n %libkntlm
KDE 4 core library.

%post -n %libkntlm -p /sbin/ldconfig
%postun -n %libkntlm -p /sbin/ldconfig

%files -n %libkntlm
%defattr(-,root,root)
%_kde_libdir/libkntlm.so.%{kntlm_major}*

#------------------------------------------------	

%define kparts_major 4
%define libkparts %mklibname kparts %kparts_major

%package -n %libkparts
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}kparts5 < 3.93.0-0.714006.1
 

%description -n %libkparts
KDE 4 core library.

%post -n %libkparts -p /sbin/ldconfig
%postun -n %libkparts -p /sbin/ldconfig

%files -n %libkparts
%defattr(-,root,root)
%_kde_libdir/libkparts.so.%{kparts_major}*

#------------------------------------------------	

%define krosscore_major 4
%define libkrosscore %mklibname krosscore %krosscore_major

%package -n %libkrosscore
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}krosscore5 < 3.93.0-0.714006.1
 

%description -n %libkrosscore
KDE 4 core library.

%post -n %libkrosscore -p /sbin/ldconfig
%postun -n %libkrosscore -p /sbin/ldconfig

%files -n %libkrosscore
%defattr(-,root,root)
%_kde_libdir/libkrosscore.so.%{krosscore_major}*

#------------------------------------------------	

%define krossui_major 4
%define libkrossui %mklibname krossui %krossui_major

%package -n %libkrossui
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}krossui5 < 3.93.0-0.714006.1
 

%description -n %libkrossui
KDE 4 core library.

%post -n %libkrossui -p /sbin/ldconfig
%postun -n %libkrossui -p /sbin/ldconfig

%files -n %libkrossui
%defattr(-,root,root)
%_kde_libdir/libkrossui.so.%{krossui_major}*

#------------------------------------------------	

%define ktexteditor_major 4
%define libktexteditor %mklibname ktexteditor %ktexteditor_major

%package -n %libktexteditor
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}ktexteditor5 < 3.93.0-0.714006.1
 

%description -n %libktexteditor
KDE 4 core library.

%post -n %libktexteditor -p /sbin/ldconfig
%postun -n %libktexteditor -p /sbin/ldconfig

%files -n %libktexteditor
%defattr(-,root,root)
%_kde_libdir/libktexteditor.so.%{ktexteditor_major}*

#------------------------------------------------	

%define kunittest_major 4
%define libkunittest %mklibname kunittest %kunittest_major

%package -n %libkunittest
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}kunittest5 < 3.93.0-0.714006.1
 

%description -n %libkunittest
KDE 4 core library.

%post -n %libkunittest -p /sbin/ldconfig
%postun -n %libkunittest -p /sbin/ldconfig

%files -n %libkunittest
%defattr(-,root,root)
%_kde_libdir/libkunittest.so.%{kunittest_major}*

#------------------------------------------------	

%define kutils_major 4
%define libkutils %mklibname kutils %kutils_major

%package -n %libkutils
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}kutils5 < 3.93.0-0.714006.1
 

%description -n %libkutils
KDE 4 core library.

%post -n %libkutils -p /sbin/ldconfig
%postun -n %libkutils -p /sbin/ldconfig

%files -n %libkutils
%defattr(-,root,root)
%_kde_libdir/libkutils.so.%{kutils_major}*

#------------------------------------------------	

%define kwalletbackend_major 4
%define libkwalletbackend %mklibname kwalletbackend %kwalletbackend_major

%package -n %libkwalletbackend
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}kwalletbackend5 < 3.93.0-0.714006.1
 

%description -n %libkwalletbackend
KDE 4 core library.

%post -n %libkwalletbackend -p /sbin/ldconfig
%postun -n %libkwalletbackend -p /sbin/ldconfig

%files -n %libkwalletbackend
%defattr(-,root,root)
%_kde_libdir/libkwalletbackend.so.%{kwalletbackend_major}*

#------------------------------------------------	

%define phononexperimental_major 4
%define libphononexperimental %mklibname phononexperimental %phononexperimental_major

%package -n %libphononexperimental
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}phononexperimental5 < 3.93.0-0.714006.1
 

%description -n %libphononexperimental
KDE 4 core library.

%post -n %libphononexperimental -p /sbin/ldconfig
%postun -n %libphononexperimental -p /sbin/ldconfig

%files -n %libphononexperimental
%defattr(-,root,root)
%_kde_libdir/libphononexperimental.so.%{phononexperimental_major}*

#------------------------------------------------	

%define phonon_major 4
%define libphonon %mklibname phonon %phonon_major

%package -n %libphonon
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}phonon5 < 3.93.0-0.714006.1
 

%description -n %libphonon
KDE 4 core library.

%post -n %libphonon -p /sbin/ldconfig
%postun -n %libphonon -p /sbin/ldconfig

%files -n %libphonon
%defattr(-,root,root)
%_kde_libdir/libphonon.so.%{phonon_major}*

#------------------------------------------------	

%define solid_major 4
%define libsolid %mklibname solid %solid_major

%package -n %libsolid
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}solid5 < 3.93.0-0.714006.1
 

%description -n %libsolid
KDE 4 core library.

%post -n %libsolid -p /sbin/ldconfig
%postun -n %libsolid -p /sbin/ldconfig

%files -n %libsolid
%defattr(-,root,root)
%_kde_libdir/libsolid.so.%{solid_major}*

#------------------------------------------------

%define threadweaver_major 4
%define libthreadweaver %mklibname threadweaver %threadweaver_major

%package -n %libthreadweaver
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}threadweaver5 < 3.93.0-0.714006.1
 

%description -n %libthreadweaver
KDE 4 core library.

%post -n %libthreadweaver -p /sbin/ldconfig
%postun -n %libthreadweaver -p /sbin/ldconfig

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

%post -n %libkpty -p /sbin/ldconfig
%postun -n %libkpty -p /sbin/ldconfig

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

%post -n %libkjsapi -p /sbin/ldconfig
%postun -n %libkjsapi -p /sbin/ldconfig

%files -n %libkjsapi
%defattr(-,root,root)
%_kde_libdir/libkjsapi.so.%{kjsapi_major}*

#------------------------------------------------

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
# add requires on libxml2-utils, as when building most kde applications,
# it will call xmllint to validate the docbook files:
Requires: libxml2-utils
Requires: kdelibs4-core = %version
Requires: %libkaudiodevicelist = %version
Requires: %libkde3support = %version
Requires: %libkdecore = %version
Requires: %libkdefakes = %version
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
Requires: %libkpty = %version
Conflicts: libkdecore4-devel <= 30000000:3.5.9-10mdv
Conflicts: kdelibs-common <= 30000000:3.5.9-10mdv
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
%_kde_libdir/libkaudiodevicelist.so
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
%_kde_libdir/libkwalletbackend.so
%_kde_libdir/libnepomuk.so
%_kde_libdir/libphonon.so
%_kde_libdir/libphononexperimental.so
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
%_kde_libdir/kde4/plugins/designer
%_kde_bindir/checkXML
%_kde_mandir/man1/checkXML.1.*
%_kde_bindir/kconfig_compiler
%exclude %_kde_libdir/libkdeinit4_*

#--------------------------------------------------------------

%package core
Group: Graphical desktop/KDE
Summary: KDE 4 system core files
Suggests: enchant-dictionary
Obsoletes: kdelibs4-common < 3.93.0-0.714006.1
Conflicts: kdelibs4-devel < 4.0.0-5
Conflicts: kdelibs4-devel < 4.0.0-5
Conflicts: kdelibs-common <= 30000000:3.5.9-10mdv
Requires: shared-mime-info

%description core
KDE 4 system core files.

%files core
%defattr(-,root,root,-)
%attr(0755,root,root) %_sysconfdir/profile.d/*
%_sysconfdir/ld.so.conf.d/kde4.conf
%_sysconfdir/pam.d/kde
%dir %_kde_bindir
%_kde_bindir/*
%dir %_kde_libdir
%dir %_kde_libdir/kde4
%_kde_libdir/kde4/*
%_kde_libdir/libkdeinit4_*
%dir %_kde_appsdir
%_kde_appsdir/*/*
%dir %_kde_datadir
%_kde_datadir/config/*
%_kde_datadir/mime/*
%_kde_datadir/kde4/services/*
%_kde_datadir/kde4/servicetypes/*
%_kde_docdir/HTML/en/sonnet
%_kde_docdir/HTML/en/common/*
%_kde_mandir/man1/kde4-config.1.*
%_kde_mandir/man7/kdeoptions.7.*
%_kde_mandir/man7/qtoptions.7.*
%_kde_mandir/man8/kbuildsycoca4.8.*
%_kde_datadir/icons
%exclude %_kde_sysconfdir/xdg/menus/applications.menu
%exclude %_kde_bindir/checkXML
%exclude %_kde_bindir/kconfig_compiler
%exclude %_kde_appsdir/cmake/modules/*
%exclude %_kde_libdir/kde4/plugins/designer
%exclude %_kde_datadir/locale/all_languages

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

make -C build DESTDIR=%buildroot install

%if %{compile_apidox}
   mkdir -p %buildroot/%_docdir/kde4/api
   cp -av kdelibs-%version-apidocs %buildroot/%_docdir/kde4/api/kdelibs
%endif 

# Install kde pam configuration file
install -d -m 0755 %buildroot%_sysconfdir/pam.d/
install -m 0644 %SOURCE1 %buildroot%_sysconfdir/pam.d/kde

# Env entry for setup kde4  environment
install -d -m 0755 %buildroot/%_sysconfdir/profile.d
cat > %buildroot%_sysconfdir/profile.d/kde4env.sh << EOF
#!/bin/bash

if [ -z \$PKG_CONFIG_PATH ]; then
    PKG_CONFIG_PATH=%{_kde_libdir}/pkgconfig
else
    PKG_CONFIG_PATH=\$PKG_CONFIG_PATH:%{_kde_libdir}/pkgconfig
fi

export PKG_CONFIG_PATH

EOF

# Are libs really conflicting with kde3 libs ?
install -d %buildroot/%_sysconfdir/ld.so.conf.d
cat > %buildroot/%_sysconfdir/ld.so.conf.d/kde4.conf <<EOF
%_kde_libdir
EOF

%clean
rm -fr %buildroot

