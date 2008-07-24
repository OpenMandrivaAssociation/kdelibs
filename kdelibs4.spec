%define compile_apidox 0
%{?_with_apidox: %{expand: %%global compile_apidox 1}}

Name: kdelibs4
Summary: K Desktop Environment - Libraries
Version: 4.1.0
Group: Graphical desktop/KDE
License: ARTISTIC BSD GPL_V2 LGPL_V2 QPL_V1.0
BuildRoot: %_tmppath/%name-%version-%release-root
URL: http://www.kde.org
Release: %mkrel 1
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdelibs-%version.tar.bz2
Patch0: kdelibs-4.0.81-add-extra-catalogs.patch
Patch1: kdelibs-post-4.0.98-translation-fix.patch
Patch2: kdelibs-post-4.0.98-findboost.patch
Patch3: kdelibs-4.0.98-liblzma.patch
BuildRequires: kde4-macros >= 4.1-8
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
BuildRequires: strigi-devel >=  0.5.9
BuildRequires: shared-mime-info
BuildRequires: soprano-devel >= 2.0.98
BuildRequires: automoc
BuildRequires: phonon-devel >= 4.2
BuildRequires: xpm-devel
BuildRequires: xft2-devel
BuildRequires: liblzma-devel >= 4.9

%description 
Libraries for the K Desktop Environment.

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

%if %mdkversion < 200900
%post -n %libkde3support -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkde3support -p /sbin/ldconfig
%endif

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
Requires: kde4-config-file 
Requires: kde4-l10n

%description -n %libkdecore
KDE 4 core library.

%if %mdkversion < 200900
%post -n %libkdecore -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkdecore -p /sbin/ldconfig
%endif

%files -n %libkdecore
%defattr(-,root,root)
%_kde_libdir/libkdecore.so.%{kdecore_major}*
%if %mdkversion <= 200810
%_sysconfdir/ld.so.conf.d/%{_lib}kde4.conf
%endif

#------------------------------------------------	

%define kdefakes_major 5
%define libkdefakes %mklibname kdefakes %kdefakes_major

%package -n %libkdefakes
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= 30000000:3.80.3
 

%description -n %libkdefakes
KDE 4 core library.

%if %mdkversion < 200900
%post -n %libkdefakes -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkdefakes -p /sbin/ldconfig
%endif

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

%if %mdkversion < 200900
%post -n %libkdesu -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkdesu -p /sbin/ldconfig
%endif

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

%if %mdkversion < 200900
%post -n %libkdeui -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkdeui -p /sbin/ldconfig
%endif

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

%if %mdkversion < 200900
%post -n %libkdnssd -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkdnssd -p /sbin/ldconfig
%endif

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

%if %mdkversion < 200900
%post -n %libkfile -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkfile -p /sbin/ldconfig
%endif

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

%if %mdkversion < 200900
%post -n %libkhtml -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkhtml -p /sbin/ldconfig
%endif

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

%if %mdkversion < 200900
%post -n %libkimproxy -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkimproxy -p /sbin/ldconfig
%endif

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

%if %mdkversion < 200900
%post -n %libkio -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkio -p /sbin/ldconfig
%endif

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

%if %mdkversion < 200900
%post -n %libkjsembed -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkjsembed -p /sbin/ldconfig
%endif

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

%if %mdkversion < 200900
%post -n %libkjs -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkjs -p /sbin/ldconfig
%endif

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

%if %mdkversion < 200900
%post -n %libkmediaplayer -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkmediaplayer -p /sbin/ldconfig
%endif

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
Obsoletes: %{_lib}nepomuk-middleware4 < 3.93.0-0.725600.1

%description -n %libnepomuk
KDE 4 core library.

%if %mdkversion < 200900
%post -n %libnepomuk -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libnepomuk -p /sbin/ldconfig
%endif

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

%if %mdkversion < 200900
%post -n %libknewstuff2 -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libknewstuff2 -p /sbin/ldconfig
%endif

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

%if %mdkversion < 200900
%post -n %libknotifyconfig -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libknotifyconfig -p /sbin/ldconfig
%endif

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

%if %mdkversion < 200900
%post -n %libkntlm -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkntlm -p /sbin/ldconfig
%endif

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

%if %mdkversion < 200900
%post -n %libkparts -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkparts -p /sbin/ldconfig
%endif

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

%if %mdkversion < 200900
%post -n %libkrosscore -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkrosscore -p /sbin/ldconfig
%endif

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

%if %mdkversion < 200900
%post -n %libkrossui -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkrossui -p /sbin/ldconfig
%endif

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

%if %mdkversion < 200900
%post -n %libktexteditor -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libktexteditor -p /sbin/ldconfig
%endif

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

%if %mdkversion < 200900
%post -n %libkunittest -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkunittest -p /sbin/ldconfig
%endif

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

%if %mdkversion < 200900
%post -n %libkutils -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkutils -p /sbin/ldconfig
%endif

%files -n %libkutils
%defattr(-,root,root)
%_kde_libdir/libkutils.so.%{kutils_major}*

#------------------------------------------------	

%package -n kwallet-daemon
Summary: Kwallet daemon
Group: Development/KDE and Qt

%description -n kwallet-daemon
Kwallet daemon.

%files -n kwallet-daemon
%defattr(-,root,root)
%_kde_bindir/kwalletd

#------------------------------------------------	

%define kwalletbackend_major 4
%define libkwalletbackend %mklibname kwalletbackend %kwalletbackend_major

%package -n %libkwalletbackend
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}kwalletbackend5 < 3.93.0-0.714006.1
Requires: kwallet-daemon 

%description -n %libkwalletbackend
KDE 4 core library.

%if %mdkversion < 200900
%post -n %libkwalletbackend -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkwalletbackend -p /sbin/ldconfig
%endif

%files -n %libkwalletbackend
%defattr(-,root,root)
%_kde_libdir/libkwalletbackend.so.%{kwalletbackend_major}*

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

%if %mdkversion < 200900
%post -n %libsolid -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libsolid -p /sbin/ldconfig
%endif

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

%if %mdkversion < 200900
%post -n %libthreadweaver -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libthreadweaver -p /sbin/ldconfig
%endif

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

%if %mdkversion < 200900
%post -n %libkpty -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkpty -p /sbin/ldconfig
%endif

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

%if %mdkversion < 200900
%post -n %libkjsapi -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkjsapi -p /sbin/ldconfig
%endif

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
Requires: qt4-devel >= 4.4.0
Requires: kdelibs4-core = %version
Requires: cmake
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
Requires: X11-devel
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
Requires: %libsolid = %version
Requires: %libthreadweaver = %version
Requires: %libkpty = %version
Requires: %libkjsapi = %version
Requires: automoc
Obsoletes: %{_lib}kdecore5-devel < 3.93.0-0.714006.1
%if %mdkversion > 200810
Conflicts: %{_lib}kdecore4-devel < 30000000:3.5.9-11
Conflicts: %{_lib}kjsembed1-devel < 1:3.5.9-2
Conflicts: kdelibs-common < 30000000:3.5.9-11
%endif

%description devel
This package includes the header files you will need to compile applications 
for KDE. Also included is the KDE API documentation in HTML format for easy 
browsing.

%files devel
%defattr(-,root,root,-)
%_mandir/man1/kdecmake.*
%_kde_prefix/include/*
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
%_kde_libdir/libkwalletbackend.so
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
%if %mdkversion > 200810
Conflicts: kdelibs-common < 30000000:3.5.9-11
Conflicts: kjsembed < 1:3.5.9-2
%endif
Requires: shared-mime-info

%description core
KDE 4 system core files.

%files core
%defattr(-,root,root,-)
%attr(0755,root,root) %_sysconfdir/profile.d/*
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
%_kde_libdir/libkdeinit4_*
%_kde_datadir/config
%_kde_datadir/mime/*
%_kde_datadir/kde4
%_kde_appsdir/proxyscout
%_kde_appsdir/nepomuk
%_kde_appsdir/LICENSES
%_kde_appsdir/ktexteditor_kdatatool
%_kde_appsdir/ktexteditor_insertfile
%_kde_appsdir/ktexteditor_docwordcompletion
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
%_kde_appsdir/kcertpart
%_kde_appsdir/kcharselect
%_kde_docdir/HTML/en/sonnet
%_kde_docdir/HTML/en/common/*
%_kde_mandir/man1/kde4-config.1.*
%_kde_mandir/man1/makekdewidgets.1.*
%_kde_mandir/man7/kdeoptions.7.*
%_kde_mandir/man7/qtoptions.7.*
%_kde_mandir/man8/kbuildsycoca4.8.*
%_kde_datadir/icons
#Do not include this file because provided by desktop-common-data
%exclude %_kde_sysconfdir/xdg/menus/applications.menu

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
%patch0 -p0
%patch1 -p0 -b .post4098
%patch2 -p0 -b .post49098
%patch3 -p1 -b .liblzma

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

# Libraries are in /opt
%if %mdkversion <= 200810
install -d -m 0755 %buildroot/%_sysconfdir/ld.so.conf.d
echo "%_kde_libdir" > %buildroot/%_sysconfdir/ld.so.conf.d/%{_lib}kde4.conf
%endif

# Env entry for setup kde4  environment
install -d -m 0755 %buildroot/%_sysconfdir/profile.d
cat > %buildroot%_sysconfdir/profile.d/kde4env.sh << EOF
#!/bin/bash

%if %mdkversion <= 200810

if [ -z \$PATH ]; then
    PATH=%{_bindir}:/bin:%{_kde_bindir}
else
    PATH=\$PATH:%{_bindir}:%{_kde_bindir}
fi

if [ -z \$XDG_DATA_DIRS ]; then
    XDG_DATA_DIRS=%{_datadir}:%{_kde_datadir}
else
    XDG_DATA_DIRS=\$XDG_DATA_DIRS:%{_datadir}:%{_kde_datadir}
fi

export XDG_DATA_DIRS PATH

%endif

if [ -z \$PKG_CONFIG_PATH ]; then
    PKG_CONFIG_PATH=%{_kde_libdir}/pkgconfig
else
    PKG_CONFIG_PATH=\$PKG_CONFIG_PATH:%{_kde_libdir}/pkgconfig
fi

export PKG_CONFIG_PATH XDG_DATA_DIRS PATH

EOF

%clean
rm -fr %buildroot

