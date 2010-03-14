#
# Conditional build:
%bcond_with	deskbar_applet	# don't build GNOME Deskbar applet extension
#
Summary:	Tracker - an indexing subsystem
Summary(pl.UTF-8):	Tracker - podsystem indeksujący
Name:		tracker
Version:	0.7.25
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/tracker/0.7/%{name}-%{version}.tar.bz2
# Source0-md5:	b95f8b6a321132ecd7d0ba7e181b2eed
URL:		http://projects.gnome.org/tracker/
BuildRequires:	DeviceKit-power-devel >= 007
BuildRequires:	GConf2-devel >= 2.20.0
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	dbus-devel >= 1.0.0
BuildRequires:	dbus-glib-devel >= 0.78
BuildRequires:	enca-devel >= 1.9
BuildRequires:	evolution-data-server-devel >= 2.26.0
BuildRequires:	evolution-devel >= 2.26.0
BuildRequires:	exempi-devel >= 2.1.0
BuildRequires:	flac-devel >= 1.2.1
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.20.0
%{?with_deskbar_applet:BuildRequires:	gnome-applet-deskbar-devel >= 2.20.0}
BuildRequires:	gnome-panel-devel
BuildRequires:	gstreamer-devel >= 0.10.15
BuildRequires:	gtk+2-devel >= 2:2.16.0
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	hal-devel >= 0.5.10
BuildRequires:	id3lib-devel >= 3.8.3
BuildRequires:	intltool >= 0.37.0
BuildRequires:	libexif-devel >= 0.6.13
BuildRequires:	libgee-devel >= 0.3
BuildRequires:	libgsf-devel >= 1.14.7
BuildRequires:	libiptcdata-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libnotify-devel >= 0.4.3
BuildRequires:	libpng-devel >= 2:1.2.24
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libuuid-devel
BuildRequires:	libvorbis-devel >= 0.22
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	nautilus-devel
BuildRequires:	pkgconfig
BuildRequires:	poppler-glib-devel >= 0.6
%{?with_deskbar_applet:BuildRequires:	rpm-pythonprov}
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	sqlite3-devel >= 3.6.16
BuildRequires:	totem-pl-parser-devel
BuildRequires:	vala
BuildRequires:	xine-lib-devel >= 1.0
BuildRequires:	zlib-devel
Requires(post,postun):	gtk+2
Requires:	%{name}-libs = %{version}-%{release}
Requires:	hicolor-icon-theme
Suggests:	odt2txt
# for gunzip
Suggests:	gzip
Obsoletes:	tracker-search-gui
Obsoletes:	tracker-startup
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tracker is an indexing sub-system and search aggregator.

%description -l pl.UTF-8
Tracker jest podsystemem indeksującym i wyszukującym.


%package libs
Summary:	Tracker libraries
Summary(pl.UTF-8):	Bibliotek Trackera
Group:		Libraries
Obsoletes:	libtracker
Obsoletes:	libtracker-gtk

%description libs
Tracker libraries.

%description libs -l pl.UTF-8
Bibliotek Trackera.

%package devel
Summary:	Header files for Tracker libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek Trackera
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Obsoletes:	libtracker-devel
Obsoletes:	libtracker-gtk-devel
Obsoletes:	libtracker-gtk-static
Obsoletes:	libtracker-static

%description devel
Header files for Tracker libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek Trackera.

%package apidocs
Summary:	Tracker libraries API documentation
Summary(pl.UTF-8):	Dokumentacja API bibliotek Trackera
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
Tracker libraries API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API bibliotek Trackera.

%package -n evolution-plugin-tracker
Summary:	Tracker plugin for Evolution
Summary(pl.UTF-8):	Wtyczka Trackera do Evolution
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	evolution >= 2.28.0

%description -n evolution-plugin-tracker
Tracker plugin for Evolution.

%description -n evolution-plugin-tracker -l pl.UTF-8
Wtyczka Trackera do Evolution.

%package -n gnome-applet-deskbar-extension-tracker
Summary:	Tracker extension for GNOME Deskbar applet
Summary(pl.UTF-8):	Rozszerzenie Trackera dla apletu GNOME Deskbar
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-applet-deskbar >= 2.20.0

%description -n gnome-applet-deskbar-extension-tracker
Tracker extension for GNOME Deskbar applet.

%description -n gnome-applet-deskbar-extension-tracker -l pl.UTF-8
Rozszerzenie Trackera do apletu GNOME Deskbar.

%package -n nautilus-extension-tracker
Summary:	Tracker extension for Nautilus
Summary(pl.UTF-8):	Rozszerzenie Trackera dla Nautilusa
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	nautilus >= 2.26.0

%description -n nautilus-extension-tracker
Adds Tracker integration to Nautilus.

%description -n nautilus-extension-tracker -l pl.UTF-8
Dodaje integrację Trackera z Nautilusem.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-libvorbis \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir} \
	%{__enable_disable deskbar_applet deskbar-applet}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/evolution/*/plugins/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-2.0/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/tracker-0.7/*/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/tracker-0.7/push-modules/daemon/*.la

%if %{with deskbar_applet}
%py_comp $RPM_BUILD_ROOT%{_libdir}/deskbar-applet/modules-2.20-compatible
%py_ocomp $RPM_BUILD_ROOT%{_libdir}/deskbar-applet/modules-2.20-compatible
rm -f $RPM_BUILD_ROOT%{_libdir}/deskbar-applet/modules-2.20-compatible/*.py
%endif

%find_lang tracker

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f tracker.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tracker-control
%attr(755,root,root) %{_bindir}/tracker-explorer
%attr(755,root,root) %{_bindir}/tracker-import
%attr(755,root,root) %{_bindir}/tracker-info
%attr(755,root,root) %{_bindir}/tracker-preferences
%attr(755,root,root) %{_bindir}/tracker-search
%attr(755,root,root) %{_bindir}/tracker-search-tool
%attr(755,root,root) %{_bindir}/tracker-sparql
%attr(755,root,root) %{_bindir}/tracker-stats
%attr(755,root,root) %{_bindir}/tracker-status
%attr(755,root,root) %{_bindir}/tracker-status-icon
%attr(755,root,root) %{_bindir}/tracker-tag
%attr(755,root,root) %{_libdir}/tracker-extract
%attr(755,root,root) %{_libdir}/tracker-miner-fs
%attr(755,root,root) %{_libdir}/tracker-search-bar
%attr(755,root,root) %{_libdir}/tracker-store
%attr(755,root,root) %{_libdir}/tracker-writeback
%dir %{_libdir}/tracker-0.7/extract-modules
%attr(755,root,root) %{_libdir}/tracker-0.7/extract-modules/libextract-abw.so
#%attr(755,root,root) %{_libdir}/tracker-0.7/extract-modules/libextract-flac.so
%attr(755,root,root) %{_libdir}/tracker-0.7/extract-modules/libextract-gstreamer.so
%attr(755,root,root) %{_libdir}/tracker-0.7/extract-modules/libextract-html.so
%attr(755,root,root) %{_libdir}/tracker-0.7/extract-modules/libextract-jpeg.so
%attr(755,root,root) %{_libdir}/tracker-0.7/extract-modules/libextract-mp3.so
%attr(755,root,root) %{_libdir}/tracker-0.7/extract-modules/libextract-msoffice.so
%attr(755,root,root) %{_libdir}/tracker-0.7/extract-modules/libextract-oasis.so
%attr(755,root,root) %{_libdir}/tracker-0.7/extract-modules/libextract-pdf.so
%attr(755,root,root) %{_libdir}/tracker-0.7/extract-modules/libextract-playlist.so
%attr(755,root,root) %{_libdir}/tracker-0.7/extract-modules/libextract-png.so
%attr(755,root,root) %{_libdir}/tracker-0.7/extract-modules/libextract-ps.so
%attr(755,root,root) %{_libdir}/tracker-0.7/extract-modules/libextract-text.so
%attr(755,root,root) %{_libdir}/tracker-0.7/extract-modules/libextract-tiff.so
%attr(755,root,root) %{_libdir}/tracker-0.7/extract-modules/libextract-vorbis.so
%attr(755,root,root) %{_libdir}/tracker-0.7/extract-modules/libextract-xmp.so
%dir %{_libdir}/tracker-0.7/push-modules
%dir %{_libdir}/tracker-0.7/push-modules/daemon
%attr(755,root,root) %{_libdir}/tracker-0.7/push-modules/daemon/libtracker-module_kmail-daemon-module.so
%dir %{_libdir}/tracker-0.7/writeback-modules
%attr(755,root,root) %{_libdir}/tracker-0.7/writeback-modules/libwriteback-xmp.so
%{_sysconfdir}/xdg/autostart/tracker-miner-fs.desktop
%{_sysconfdir}/xdg/autostart/tracker-status-icon.desktop
%{_sysconfdir}/xdg/autostart/tracker-store.desktop
%{_libdir}/bonobo/servers/GNOME_Search_Bar_Applet.server
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.Extract.service
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.Miner.Applications.service
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.Miner.EMails.service
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.Miner.Files.service
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.service
%{_datadir}/tracker
%{_desktopdir}/tracker-preferences.desktop
%{_desktopdir}/tracker-search-tool.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_mandir}/man1/tracker-control.1*
%{_mandir}/man1/tracker-extract.1*
%{_mandir}/man1/tracker-import.1*
%{_mandir}/man1/tracker-info.1*
%{_mandir}/man1/tracker-miner-fs.1*
%{_mandir}/man1/tracker-preferences.1*
%{_mandir}/man1/tracker-search-bar.1*
%{_mandir}/man1/tracker-search-tool.1*
%{_mandir}/man1/tracker-search.1*
%{_mandir}/man1/tracker-sparql.1*
%{_mandir}/man1/tracker-stats.1*
%{_mandir}/man1/tracker-status-icon.1*
%{_mandir}/man1/tracker-status.1*
%{_mandir}/man1/tracker-store.1*
%{_mandir}/man1/tracker-tag.1*
%{_mandir}/man5/tracker-extract.cfg.5*
%{_mandir}/man5/tracker-fts.cfg.5*
%{_mandir}/man5/tracker-miner-fs.cfg.5*
%{_mandir}/man5/tracker-store.cfg.5*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtracker-client-0.7.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtracker-client-0.7.so.0
%attr(755,root,root) %{_libdir}/libtracker-extract-0.7.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtracker-extract-0.7.so.0
%attr(755,root,root) %{_libdir}/libtracker-miner-0.7.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtracker-miner-0.7.so.0
# required by libtracker-extract and libtracker-miner
%dir %{_libdir}/tracker-0.7
%attr(755,root,root) %{_libdir}/tracker-0.7/libtracker-common.so.*
%attr(755,root,root) %{_libdir}/tracker-0.7/libtracker-data.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtracker-client-0.7.so
%attr(755,root,root) %{_libdir}/libtracker-extract-0.7.so
%attr(755,root,root) %{_libdir}/libtracker-miner-0.7.so
%attr(755,root,root) %{_libdir}/tracker-0.7/libtracker-common.so
%attr(755,root,root) %{_libdir}/tracker-0.7/libtracker-data.so
%{_libdir}/libtracker-client-0.7.la
%{_libdir}/libtracker-extract-0.7.la
%{_libdir}/libtracker-miner-0.7.la
%{_libdir}/tracker-0.7/libtracker-common.la
%{_libdir}/tracker-0.7/libtracker-data.la
%{_includedir}/tracker-0.7
%{_pkgconfigdir}/tracker-client-0.7.pc
%{_pkgconfigdir}/tracker-extract-0.7.pc
%{_pkgconfigdir}/tracker-miner-0.7.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libtracker-client
%{_gtkdocdir}/libtracker-common
%{_gtkdocdir}/libtracker-extract
%{_gtkdocdir}/libtracker-miner
%{_gtkdocdir}/ontology

%files -n evolution-plugin-tracker
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/evolution/2.30/plugins/liborg-freedesktop-Tracker-evolution-plugin.so
%{_libdir}/evolution/2.30/plugins/org-freedesktop-Tracker-evolution-plugin.eplug

%if %{with deskbar_applet}
%files -n gnome-applet-deskbar-extension-tracker
%defattr(644,root,root,755)
%{_libdir}/deskbar-applet/modules-2.20-compatible/tracker-module.py[co]
%endif

%files -n nautilus-extension-tracker
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/nautilus/extensions-2.0/libnautilus-tracker-tags.so
