%define _requires_exceptions perl\(.*\)\\|devel\(linux-gate\)\\|devel\(libdns_sd\(.*\)\\|devel\(libdns_sd\)

# remove it when kde4 will be official kde package
%define _prefix /opt/kde4/
%define _libdir %_prefix/%_lib
%define _datadir %_prefix/share/
%define _bindir %_prefix/bin
%define _includedir %_prefix/include/
%define _iconsdir %_datadir/icons/
%define _sysconfdir %_prefix/etc/
%define _docdir %_datadir/doc/

%define branch_date 20070418

%define use_enable_final 0
%{?_no_enable_final: %{expand: %%global use_enable_final 0}}

%define compile_apidox 1
%{?_no_apidox: %{expand: %%global compile_apidox 0}}

%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

%define branch 1
%{?_branch: %{expand: %%global branch 1}}

%define use_enable_pie 1
%{?_no_enable_pie: %{expand: %%global use_enable_pie 0}}

%if %unstable
%define dont_strip 1
%endif

%define lib_major 5
%define lib_name_orig libkdecore4
%define lib_name %mklibname kdecore %{lib_major}
%define libqt %mklibname qt 4

%define lib_name_orig_kdepim %mklibname kdepim
%define lib_major_kdepim 2
%define lib_name_kdepim %lib_name_orig_kdepim%lib_major_kdepim

%define lib_name_orig_kdebase libkdebase
%define lib_major 5
%define lib_name_kdebase %mklibname kdebase %lib_major

%define epoch_kdelibs 30000000

Name: kdelibs4
Summary: K Desktop Environment - Libraries
Version: 3.80.3
Release: %mkrel 0.%branch_date.6
Epoch: %epoch_kdelibs
Group: Graphical desktop/KDE
License: ARTISTIC BSD GPL_V2 LGPL_V2 QPL_V1.0
BuildRoot: %_tmppath/%name-%version-%release-root
URL: http://www.kde.org
Packager:       Mandriva Linux KDE Team <kde@mandriva.com>
%if %branch
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdelibs-%version-%branch_date.tar.bz2
%else
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdelibs-%version.tar.bz2
%endif
Source1:	kdelibs-3.0-mdk-hicolor-index.desktop
Source2:	kdelibs-3.5.4-bmp.desktop

Source3:	kde4.sh
# Laurent - 3.1-41mdk : add focus after click on speedbar
Patch7:	kdelibs-3.2-add-focus-to-location-lineedit.patch
# Laurent - fix kdirwatch + supermount
Patch8:	kdelibs-3.3-fix-kdirwatch-with-read-only-file.patch
# Laurent : use xvt when konsole is not here.
Patch11:	kdelibs-3.2-fix-launch-appl-in-terminal.patch
# Helio: Unifying the xdg pacthes on kstddir
Patch12: kdelibs-3.4.2-mandriva-xdg-settings.patch 
Patch13:	kdelibs-3.2-search-menu-mdk.patch
Patch14: kdelibs-3.4.2-virtual-kfile-desktop-items.patch
Patch15:	kdelibs-3.4.2-disable-kjobviewer.patch
Patch16:	kdelibs-3.2-fix-sortorder.patch
Patch17:	kdelibs-3.2-load-x-gzpostscript.patch
Patch19:	kdelibs-3.2-remove-debug.patch
Patch20:	kdelibs-3.4.2-fix-crash-mdk-bug16466.patch
Patch21:	kdelibs-3.2-fix-create-device-with-supermount.patch
Patch22:	kdelibs-3.2-fix-khtmlpart.patch
Patch24:	kdelibs-3.3.0-patch-tip.patch
Patch26:	kdelibs-3.3.2-fix-kbookmark-advanceddialog.patch
Patch29:	kdelibs-3.3.2-fix-init-java.patch
Patch30:	kdelibs-3.3.2-fix-kurlbar-global.patch
Patch32:	kdelibs-3.3.2-fix-khtml-kde-bug-90267.patch
Patch35:	kdelibs-3.4.0-fix-kcmshell-list.patch
Patch36:	kdelibs-3.5.3-fix-enable-dialogbox.patch
Patch37:	kdelibs-3.4.0-fix-kurlbar-add-entry.patch
Patch39:	kdelibs-3.3.2-fix-detect-aspell-0.60.patch
Patch40:	kdelibs-3.3.2-fix-create-associate-menu-file.patch
Patch42:	kdelibs-3.3.2-fix-associate-file.patch
Patch43:	kdelibs-3.4.92-fix-associate-unknown-apps.patch
Patch44:	kdelibs-3.4.0-fix-kservice-mdk-bug-14653.patch
Patch45:	kdelibs-3.3.2-fix-aspell-0-60-config.patch
Patch46:	kdelibs-3.5.4-fix-document-path.patch
Patch47:	kdelibs-3.4.2-add-item-in-kfile-speedbar.patch
Patch51:	kdelibs-3.5.1-fix-call-config.patch
Patch52: kdelibs-3.5.1-smooth-scrolling.patch
Patch53: kdelibs-3.5.0-rubberband-selection.patch 
Patch54:	kdelibs-3.5.0-add-dnssd-avahi-support.patch	
Patch55:	kdelibs-3.5.2-move-xdg-menu-dir.patch
Patch56:	kdelibs-3.5.3-xinerama.patch	
Patch57:	kdelibs-3.5.3-menu-xdg.patch
Patch58: kdelibs-3.5.4-fix-https-loop.patch
Patch59:	kdelibs-3.5.4-fix-translate-menu.patch
Patch60:	kdelibs-3.4.2-add-default-startup-sound.patch
Patch61:	kdelibs-3.5.4-fix-translate-desktopfile.patch
Patch63:	kdelibs-3.5.5-fix-kate-save-session.patch

BuildRequires: mandriva-create-kde-mdk-menu >= 2007.1
BuildRequires: aspell-devel
BuildRequires: hspell-devel
BuildRequires: avahi-compat-libdns_sd-devel 
BuildRequires: avahi-client-devel
BuildRequires: enchant-devel
BuildRequires: libxslt-proc

#Necessary to change it when we will have i18n for kde4
Requires: kde-l10n

BuildRequires: qt4-devel >= 4.3.0
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
BuildRequires: cmake >= 2.4.5
BuildRequires:	ungif-devel
BuildRequires:	strigi-devel >=  0.3.11-0.20070311
# Now kdelibs4 implemented mimetype freedesktop spec
BuildRequires:	shared-mime-info

%description 
Libraries for the K Desktop Environment.

#--------------------------------------------------------------

%package -n %lib_name
Group:      Development/KDE and Qt
Summary:    Core libraries for KDE
Provides: kdelibs4 = %{epoch_kdelibs}:%version-%release
Provides: %lib_name_orig = %{epoch_kdelibs}:%version-%release
Requires: kdelibs4-common = %{epoch_kdelibs}:%version-%release
# readd it
#Requires: %{libqt} >= 4.2.0

%description -n %lib_name
Libraries for the K Desktop Environment.


#--------------------------------------------------------------

%package -n %lib_name-devel
Group:		Development/KDE and Qt
Summary:	Header files and documentation for compiling KDE applications.
Provides:	%name-devel = %{epoch_kdelibs}:%version-%release
Requires:	%lib_name = %{epoch_kdelibs}:%version-%release
Requires:	acl-devel
Requires:   	qt4-devel >= 4.3.0
Requires:	cmake

BuildRequires: cmake
%define mini_release %mkrel 2
Requires: mandriva-create-kde-mdk-menu >= 2007.1-%mini_release
Requires: libxml2-utils

%description -n %lib_name-devel
This package includes the header files you will need to compile applications 
for KDE. Also included is the KDE API documentation in HTML format for easy 
browsing.


#--------------------------------------------------------------

%package    common
Group:      Development/KDE and Qt
Summary:    Config file and icons file for %name.
Requires(pre):   %lib_name = %{epoch_kdelibs}:%version-%release
Requires: kde-config-file
Requires: 	kde-custom-icons
Requires:	desktop-common-data
%if %unstable
Requires: gdb
%endif
Requires: aspell

%package    devel-doc
Group:      Development/KDE and Qt
Summary:    Development documentation for %name.
Requires:   qt4-doc

%description devel-doc
This packages contains all development documentation for kdelibs

%description common
This packages contains all icons, config file etc...

%post common
%update_icon_cache crystalsvg

%postun common
%clean_icon_cache crystalsvg

%pre common
# here, we put things that we have moved around (like directories)
# that need to be cleaned up prior to the RPM's installation.
# Ugly. Necessary.

mv /usr/share/config /usr/share/config.
while read old new link; do
  if [ -d `dirname $old` -a ! -L $old ]; then
     echo "moving $old to $new linking to $link"
     if [ ! -d $new ]; then
        mkdir -p $new
     fi
     if [ -d $old ]; then
         mv -f $old/* $new
         rm -rf $old
     fi
     #ln -sf $link $old
  fi
done << EOF
/usr/share/config. /etc/kde/ ../../etc/kde
EOF

ln -sf ../../etc/kde /usr/share/config
rm -rf /usr/share/config.


%post -n %{lib_name} -p /sbin/ldconfig
%postun -n %{lib_name} -p /sbin/ldconfig


%prep
%setup -q -nkdelibs-%version-%branch_date
#%patch7 -p1 -b .add_focus_to_kio_filedialogbox_url
#%patch8 -p1 -b .fam_supermout_readonly
#%patch11 -p1 -b .fix_launch_xvt
#%patch14 -p1 -b .virtual_kfile_items
#%patch15 -p1 -b .disable_kjobviewer_by_default
#%patch16 -p1 -b .fix_sort_order
#%patch17 -p1 -b .load_gzpostscript
#%patch19 -p1 -b .remove_debug
#%patch20 -p1 -b .fix_khtml_crash_mdk_bug_16466
#%patch21 -p1 -b .fix_desktop_supermount
#%patch22 -p1 -b .fix_khtml_part
#%patch24 -p1 -b .fix_tipofday
#%patch26 -p1 -b .fix_kbookmark_advanced_dialogbox
#%patch29 -p1 -b .fix_init_java
#%patch30 -p1 -b .add_kfile_item_in_global
#%patch32 -p1 -b .fix_khtml_kde_bug_90267
#%patch36 -p1 -b .fix_disable_button
#%patch37 -p1 -b .add_entry_on_desktop
#%patch39 -p1 -b .fix_aspell_detect
#%patch45 -p1 -b .fix_aspell_0_60_config
#%patch46 -p1 -b .fix_default_document_path
#%patch47 -p1 -b .add_kfilespeedbar_item

#%patch52 -p1 -b .smooth
#%patch53 -p0 -b .rubber
#%patch54 -p0 -b .avahi_support
#%patch55 -p1 -b .move_xdg_menu_dir
#%patch56 -p1 -b .xinerama
#%patch57 -p1 -b .menu_xdg
#%patch58 -p1 -b .fix_https_loop
#%patch59 -p1 -b .fix_translate_menu
#%patch60 -p1 -b .default_startup_sound
#%patch61 -p1 -b .fix_translate_desktopfile
#%patch62 -p1 -b .dcop_wrong_reply

#%patch63 -p1 -b .fix_kate_save_session_tmp_file

%build

cd $RPM_BUILD_DIR/kdelibs-%version-%branch_date
mkdir build
cd build
export QTDIR=/usr/lib/qt4/
export PATH=$QTDIR/bin:$PATH

cmake -DCMAKE_INSTALL_PREFIX=%_prefix \
%if %use_enable_final
      -DKDE4_ENABLE_FINAL=ON \
%endif
%if %use_enable_pie
      -DKDE4_ENABLE_FPIE=ON \
%endif
%if %unstable
      -DCMAKE_BUILD_TYPE=Debug \
%endif
%if "%{_lib}" != "lib"
      -DLIB_SUFFIX=64 \
%endif
	../

%make

%install
rm -fr %buildroot
cd $RPM_BUILD_DIR/kdelibs-%version-%branch_date
cd build

make DESTDIR=%buildroot install

#install -d -m 0755 %buildroot/%_iconsdir/mdk-hicolor/
#install -m 0644 %SOURCE1 %buildroot/%_iconsdir/mdk-hicolor/index.desktop
# Create LMDK menu entries

#install -m 0644 %SOURCE2 %buildroot/%_datadir/mimelnk/image/bmp.desktop
#rm -f %buildroot/%_iconsdir/hicolor/index.theme

install -d %buildroot/etc/profile.d/
install -m 0755 %SOURCE3 %buildroot/etc/profile.d/kde4.sh


cat > $RPM_BUILD_ROOT/%_prefix/README.urpmi <<EOF
Mandriva RPM specific notes

WARNING
-------
These packages are not STABLE. Not to use them in production. 
Install theses packages just for testing (otherwise uninstall
them)

To start kde just to type "kde4" in Shell.

Don't try to use Kmail, mail can be lose.
KDesktop doesn't work very well and will be replaced by Plasma.

We use for the moment KDE standard menu, Mandriva menu is not 
supported for the moment.


INFO about snapshot
-------------------
Now kde4 uses xdg mimetype.
kde4 requires cmake 2.4.5
Merge js from apple.
Requires qt4.3
oKular (new kpdf version) comes back into kdegraphics
Cleanup kdelibs


EOF


%clean
rm -fr %buildroot


%files common
%defattr(-,root,root,-)
%_prefix/README.urpmi
%_bindir/checkXML
%_bindir/cupsdconf
%_bindir/cupsdoprint
%_bindir/imagetops
%_bindir/js
%_bindir/kaddprinterwizard
%_bindir/kbuildsycoca4
%_bindir/kconf_update
%_bindir/kconfig_compiler
%_bindir/kcookiejar
%_bindir/kde-menu
%_bindir/kde4-config
%_bindir/kded
%_bindir/kdeinit
%_bindir/kdeinit_shutdown
%_bindir/kdeinit_wrapper
%_bindir/kdesu_stub
%_bindir/kdontchangethehostname
%_bindir/kdostartupconfig
%_bindir/kio_http_cache_cleaner
%_bindir/kioslave
%_bindir/kjscmd
%_bindir/kjsconsole
%_bindir/klauncher
%_bindir/knotifytest
%_bindir/kpac_dhcp_helper
%_bindir/kross
%_bindir/ksendbugmail
%_bindir/kshell
%_bindir/kstartupconfig
%_bindir/ksvgtopng
%_bindir/ktradertest
%_bindir/kunittestmodrunner
%_bindir/kwrapper
%_bindir/make_driver_db_cups
%_bindir/make_driver_db_lpr
%_bindir/makekdewidgets
%_bindir/meinproc
%_bindir/preparetips

%dir %_datadir/apps/LICENSES/
%_datadir/apps/LICENSES/*

%dir %_datadir/apps/emoticons/
%dir %_datadir/apps/emoticons/Default/
%_datadir/apps/emoticons/Default/*.png
%_datadir/apps/emoticons/Default/*.xml

%_datadir/apps/katepart/katepartreadonlyui.rc
%_datadir/apps/katepart/katepartui.rc
%_datadir/apps/katepart/scripts/*.js
%_datadir/apps/katepart/syntax/*.xml
%_datadir/apps/kcertpart/kcertpart.rc
%_datadir/apps/kcm_componentchooser/kcm_instantmessenger.desktop
%_datadir/apps/kcm_componentchooser/kcm_ktexteditor.desktop
%_datadir/apps/kconf_update/kcookiescfg.upd
%_datadir/apps/kconf_update/kded.upd
%_datadir/apps/kconf_update/kdeprintrc.upd
%_datadir/apps/kconf_update/kio_help.upd
%_datadir/apps/kconf_update/kioslave.upd
%_datadir/apps/kconf_update/move_kio_help_cache.sh
%_datadir/apps/kconf_update/proxytype.pl
%_datadir/apps/kconf_update/useragent.pl
%dir %_datadir/apps/kdeprint/
%_datadir/apps/kdeprint/apsdriver1
%_datadir/apps/kdeprint/apsdriver2
%_datadir/apps/kdeprint/cups_logo.png
%_datadir/apps/kdeprint/cupsd.conf.template
%_datadir/apps/kdeprint/filters/*.desktop
%_datadir/apps/kdeprint/filters/*.xml
%_datadir/apps/kdeprint/icons/crystalsvg/*
%_datadir/apps/kdeprint/lprngtooldriver1
%_datadir/apps/kdeprint/pics/*.png
%_datadir/apps/kdeprint/plugins/*.print
%_datadir/apps/kdeprint/*.png
%_datadir/apps/kdeprint/specials.desktop
%_datadir/apps/kdeprint/testprint.ps
%_datadir/apps/kdeprint/tools/escputil.desktop
%dir %_datadir/apps/kdeui/about/
%_datadir/apps/kdeui/about/*.png
%_datadir/apps/kdeui/about/*.css
%_datadir/apps/kdewidgets/pics/*.png
%_datadir/apps/khtml/css/html4.css
%_datadir/apps/khtml/css/quirks.css
%_datadir/apps/khtml/domain_info
%_datadir/apps/khtml/icons/crystalsvg/*
%_datadir/apps/khtml/khtml.rc
%_datadir/apps/khtml/khtml_browser.rc
%_datadir/apps/khtml/khtml_popupmenu.rc
%_datadir/apps/kjava/icons/crystalsvg/16x16/actions/java.png
%_datadir/apps/kjava/kjava.jar
%_datadir/apps/kjava/kjava.policy
%_datadir/apps/kjava/pluginsinfo
%_datadir/apps/knotifytest/knotifytest.notifyrc
%_datadir/apps/knotifytest/knotifytestui.rc
%_datadir/apps/ksgmltools2/customization/*
%_datadir/apps/ksgmltools2/docbook/README.kde
%_datadir/apps/ksgmltools2/docbook/*

%_datadir/apps/solidfakebluetoothbackend/fakebluetooth.xml
%_datadir/config/kdxspreviewrc
%_datadir/mime/packages/kde.xml

%dir %_docdir/HTML/en/sonnet/
%doc %_docdir/HTML/en/sonnet/*.bz2
%doc %_docdir/HTML/en/sonnet/*.docbook


%_datadir/apps/kssl/ca-bundle.crt
%dir %_datadir/apps/kstyle/pixmaps/
%_datadir/apps/kstyle/pixmaps/riscos/*.png
%_datadir/apps/kstyle/themes/plastik.themerc
%_datadir/apps/kstyle/themes/riscos.themerc
%_datadir/apps/ktexteditor_insertfile/ktexteditor_insertfileui.rc
%_datadir/apps/ktexteditor_kdatatool/ktexteditor_kdatatoolui.rc
%_datadir/apps/ktexteditor_docwordcompletion/docwordcompletionui.rc
%_datadir/apps/proxyscout/proxyscout.notifyrc
%_datadir/apps/solidfakehwbackend/fakecomputer.xml
%_datadir/apps/solidfakenetbackend/fakenetworking.xml
%dir %_datadir/config/colors/
%_datadir/config/colors/*.colors
%_datadir/config/katefiletyperc
%_datadir/config/katesyntaxhighlightingrc
%_datadir/config/kdebug.areas
%_datadir/config/kdebugrc
%_datadir/config/kdeprintrc
%_datadir/config/ksslcalist
%_datadir/config/language.codes
%dir %_datadir/config/ui/
%_datadir/config/ui/kprintpreviewui.rc
%_datadir/config/ui/ui_standards.rc
%_datadir/apps/phonon/phonon.notifyrc

%_iconsdir/*
%_datadir/locale/all_languages
%_datadir/kde4/services/*.protocol
%_datadir/kde4/services/*.desktop
%_datadir/kde4/services/kded/*.desktop
%_datadir/kde4/services/qimageioplugins/*.desktop
%_datadir/kde4/services/solidbackends/*
%_datadir/kde4/services/phononbackends/*.desktop
%_datadir/kde4/servicetypes/*.desktop
%dir %_datadir/apps/katepart/syntax/
%_datadir/apps/katepart/syntax/language.dtd
%_datadir/apps/katepart/syntax/syntax.template
%dir %_datadir/apps/kdeui/pics/
%_datadir/apps/kdeui/pics/*.png

%_sysconfdir/xdg/menus/applications.menu
/etc/profile.d/kde4.sh


%files -n %{lib_name}
%defattr(-,root,root,-)
%_libdir/kde4/*.so
%_libdir/*.so.*
%dir %_libdir/kde4/plugins/designer/
%_libdir/kde4/plugins/designer/*.so
%dir %_libdir/kde4/plugins/imageformats/
%_libdir/kde4/plugins/imageformats/*.so
%dir %_libdir/kde4/plugins/styles/
%_libdir/kde4/plugins/styles/*.so

%dir %_libdir/kde4/libexec/
%_libdir/kde4/libexec/kgrantpty
%_libdir/kde4/libexec/lnusertemp
%_libdir/kde4/libexec/fileshareset
%_libdir/kde4/libexec/kmailservice
%_libdir/kde4/libexec/ktelnetservice

%_libdir/libkdeinit_cupsdconf.so
%_libdir/libkdeinit_kaddprinterwizard.so
%_libdir/libkdeinit_kbuildsycoca4.so.*
%_libdir/libkdeinit_kconf_update.so
%_libdir/libkdeinit_kded.so
%_libdir/libkdeinit_kio_http_cache_cleaner.so
%_libdir/libkdeinit_klauncher.so



%files -n %lib_name-devel
%defattr(-,root,root,-)
%dir %_includedir/knewstuff2/
%dir %_includedir/knewstuff2/core/
%_includedir/knewstuff2/core/*.h
%dir %_includedir/knewstuff2/dxs/
%_includedir/knewstuff2/dxs/*.h
%_includedir/knewstuff2/*.h
%dir %_includedir/knewstuff2/ui/
%_includedir/knewstuff2/ui/*.h
%dir %_includedir/phonon/experimental/
%_includedir/phonon/experimental/*.h
%dir %_includedir/wtf/
%_includedir/wtf/*.h
%dir %_includedir/KDE/
%_includedir/KDE/*
%_includedir/*.h
%dir %_includedir/dnssd/
%_includedir/dnssd/*.h
%dir %_includedir/dom/
%_includedir/dom/*.h
%dir %_includedir/kdeprint/
%_includedir/kdeprint/*.h
%dir %_includedir/kdeprint/lpr/
%_includedir/kdeprint/lpr/*.h
%dir %_includedir/kdesu/
%_includedir/kdesu/*.h
%_includedir/kgenericfactory.tcc
%dir %_includedir/khexedit/
%_includedir/khexedit/*.h
%dir %_includedir/kio/
%_includedir/kio/*.h
%dir %_includedir/kjs/
%_includedir/kjs/*.h
%dir %_includedir/kjsembed/
%_includedir/kjsembed/*.h
%dir %_includedir/kmediaplayer/
%_includedir/kmediaplayer/*.h
%dir %_includedir/kparts/
%_includedir/kparts/*.h
%dir %_includedir/kross/core/
%_includedir/kross/core/*.h
%dir %_includedir/ksettings/
%_includedir/ksettings/*.h
%dir %_includedir/ktexteditor/
%_includedir/ktexteditor/*.h
%dir %_includedir/kunittest/
%_includedir/kunittest/*.h
%dir %_includedir/phonon/
%_includedir/phonon/*.h
%dir %_includedir/phonon/ui/
%_includedir/phonon/ui/*.h
%dir %_includedir/solid/
%_includedir/solid/*.h
%dir %_includedir/solid/ifaces/
%_includedir/solid/ifaces/*.h
%dir %_includedir/sonnet/
%_includedir/sonnet/*.h
%dir %_includedir/threadweaver/
%_includedir/threadweaver/*.h

%dir %_datadir/apps/cmake/modules/
%_datadir/apps/cmake/modules/*
%_libdir/*.so

%exclude %_libdir/libkdeinit_cupsdconf.so
%exclude %_libdir/libkdeinit_kaddprinterwizard.so
%exclude %_libdir/libkdeinit_kconf_update.so
%exclude %_libdir/libkdeinit_kded.so
%exclude %_libdir/libkdeinit_kio_http_cache_cleaner.so
%exclude %_libdir/libkdeinit_klauncher.so



%dir %_datadir/dbus-1/
%dir %_datadir/dbus-1/interfaces/
%_datadir/dbus-1/interfaces/*.xml


%files devel-doc
%defattr(-,root,root,-)
%dir %_docdir/HTML/en/common/
%_docdir/HTML/en/common/*.jpg
%_docdir/HTML/en/common/*.png
%_docdir/HTML/en/common/*.html
%_docdir/HTML/en/common/lgpl-license
%_docdir/HTML/en/common/xml.dcl
%_docdir/HTML/en/common/doxygen.css
%_docdir/HTML/en/common/favicon.ico
%_docdir/HTML/en/common/fdl-license
%_docdir/HTML/en/common/gpl-license



