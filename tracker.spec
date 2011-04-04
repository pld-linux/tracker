%define		ver	0.10
Summary:	Tracker - an indexing subsystem
Summary(pl.UTF-8):	Tracker - podsystem indeksujący
Name:		tracker
Version:	0.10.6
Release:	0.1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/tracker/0.10/%{name}-%{version}.tar.bz2
# Source0-md5:	55f4e808cd6b10da8f891cd945fefe84
Patch0:		evolution3.patch
URL:		http://projects.gnome.org/tracker/
BuildRequires:	NetworkManager-devel >= 0.8.0
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.11
BuildRequires:	dbus-devel >= 1.3.1
BuildRequires:	dbus-glib-devel >= 0.82
BuildRequires:	dia
BuildRequires:	docbook-dtd412-xml
BuildRequires:	enca-devel >= 1.9
BuildRequires:	evolution-data-server-devel >= 2.91.91
BuildRequires:	evolution-devel >= 2.91.91
BuildRequires:	exempi-devel >= 2.1.0
BuildRequires:	flac-devel >= 1.2.1
BuildRequires:	gettext-devel
BuildRequires:	giflib-devel
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	gnome-panel-devel >= 2.91.0
BuildRequires:	graphviz
BuildRequires:	gstreamer-devel >= 0.10.15
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	gtk+2-devel >= 2:2.18.0
BuildRequires:	gtk+3-devel
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	gupnp-dlna-devel >= 0.5
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libexif-devel >= 0.6.13
BuildRequires:	libgee-devel >= 0.3
BuildRequires:	libgnome-keyring-devel >= 2.26.0
BuildRequires:	libgrss-devel >= 0.3
BuildRequires:	libgsf-devel >= 1.14.7
BuildRequires:	libiptcdata-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 2:1.2.24
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 2:2.2
BuildRequires:	libunistring-devel
BuildRequires:	libuuid-devel
BuildRequires:	libvorbis-devel >= 0.22
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	nautilus-devel >= 2.91.0
BuildRequires:	pkgconfig
BuildRequires:	poppler-glib-devel >= 0.16.0
BuildRequires:	rest-devel >= 0.6
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	sqlite3-devel >= 3.7.0
BuildRequires:	taglib-devel >= 1.6
BuildRequires:	totem-pl-parser-devel >= 2.32.2-2
BuildRequires:	upower-devel >= 0.9.0
BuildRequires:	vala
BuildRequires:	xine-lib-devel >= 1.0
BuildRequires:	zlib-devel
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name}-libs = %{version}-%{release}
Requires:	hicolor-icon-theme
# for gunzip
Suggests:	gzip
Obsoletes:	gnome-applet-deskbar-extension-tracker
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
Biblioteki Trackera.

%package devel
Summary:	Header files for Tracker libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek Trackera
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 1:2.26.0
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
Requires:	evolution >= 2.91.91

%description -n evolution-plugin-tracker
Tracker plugin for Evolution.

%description -n evolution-plugin-tracker -l pl.UTF-8
Wtyczka Trackera do Evolution.

%package -n gnome-applet-tracker
Summary:	Search applet for GNOME panel
Summary(pl.UTF-8):	Aplet wyszukiwania dla panelu GNOME
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-panel >= 2.91.0

%description -n gnome-applet-tracker
Search applet for GNOME panel.

%description -n gnome-applet-tracker -l pl.UTF-8
Aplet wyszukiwania dla panelu GNOME.

%package -n nautilus-extension-tracker
Summary:	Tracker extension for Nautilus
Summary(pl.UTF-8):	Rozszerzenie Trackera dla Nautilusa
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	nautilus >= 2.91.0

%description -n nautilus-extension-tracker
Adds Tracker integration to Nautilus.

%description -n nautilus-extension-tracker -l pl.UTF-8
Dodaje integrację Trackera z Nautilusem.

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-libflac \
	--enable-libvorbis \
	--enable-gtk-doc \
	--enable-miner-evolution \
	--enable-gdkpixbuf \
	--with-html-dir=%{_gtkdocdir} \
	--disable-unit-tests \
	--disable-silent-rules \
	--disable-hal

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/evolution/3.0/plugins/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/tracker-%{ver}/*/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/tracker-%{ver}/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-*/*.la

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
%attr(755,root,root) %{_bindir}/tracker-needle
%attr(755,root,root) %{_bindir}/tracker-preferences
%attr(755,root,root) %{_bindir}/tracker-search
%attr(755,root,root) %{_bindir}/tracker-sparql
%attr(755,root,root) %{_bindir}/tracker-stats
%attr(755,root,root) %{_bindir}/tracker-tag
%attr(755,root,root) %{_libdir}/tracker-extract
%attr(755,root,root) %{_libdir}/tracker-miner-fs
%attr(755,root,root) %{_libdir}/tracker-miner-rss
%attr(755,root,root) %{_libdir}/tracker-store
%attr(755,root,root) %{_libdir}/tracker-writeback
%dir %{_libdir}/tracker-%{ver}/extract-modules
%attr(755,root,root) %{_libdir}/tracker-%{ver}/extract-modules/libextract-abw.so
%attr(755,root,root) %{_libdir}/tracker-%{ver}/extract-modules/libextract-flac.so
%attr(755,root,root) %{_libdir}/tracker-%{ver}/extract-modules/libextract-gif.so
%attr(755,root,root) %{_libdir}/tracker-%{ver}/extract-modules/libextract-gupnp-dlna.so
%attr(755,root,root) %{_libdir}/tracker-%{ver}/extract-modules/libextract-html.so
%attr(755,root,root) %{_libdir}/tracker-%{ver}/extract-modules/libextract-icon.so
%attr(755,root,root) %{_libdir}/tracker-%{ver}/extract-modules/libextract-jpeg.so
%attr(755,root,root) %{_libdir}/tracker-%{ver}/extract-modules/libextract-mp3.so
%attr(755,root,root) %{_libdir}/tracker-%{ver}/extract-modules/libextract-msoffice.so
%attr(755,root,root) %{_libdir}/tracker-%{ver}/extract-modules/libextract-oasis.so
%attr(755,root,root) %{_libdir}/tracker-%{ver}/extract-modules/libextract-pdf.so
%attr(755,root,root) %{_libdir}/tracker-%{ver}/extract-modules/libextract-playlist.so
%attr(755,root,root) %{_libdir}/tracker-%{ver}/extract-modules/libextract-png.so
%attr(755,root,root) %{_libdir}/tracker-%{ver}/extract-modules/libextract-ps.so
%attr(755,root,root) %{_libdir}/tracker-%{ver}/extract-modules/libextract-text.so
%attr(755,root,root) %{_libdir}/tracker-%{ver}/extract-modules/libextract-tiff.so
%attr(755,root,root) %{_libdir}/tracker-%{ver}/extract-modules/libextract-vorbis.so
%attr(755,root,root) %{_libdir}/tracker-%{ver}/extract-modules/libextract-msoffice-xml.so
%attr(755,root,root) %{_libdir}/tracker-%{ver}/extract-modules/libextract-xmp.so
%dir %{_libdir}/tracker-%{ver}/sparql-modules
%attr(755,root,root) %{_libdir}/tracker-%{ver}/sparql-modules/libtracker-bus.so
%attr(755,root,root) %{_libdir}/tracker-%{ver}/sparql-modules/libtracker-direct.so
%dir %{_libdir}/tracker-%{ver}/writeback-modules
%attr(755,root,root) %{_libdir}/tracker-%{ver}/writeback-modules/libwriteback-taglib.so
%attr(755,root,root) %{_libdir}/tracker-%{ver}/writeback-modules/libwriteback-xmp.so
%{_sysconfdir}/xdg/autostart/tracker-miner-fs.desktop
%{_sysconfdir}/xdg/autostart/tracker-miner-rss.desktop
%{_sysconfdir}/xdg/autostart/tracker-store.desktop
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.Extract.service
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.Miner.Applications.service
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.Miner.EMails.service
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.Miner.Files.service
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.Miner.RSS.service
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.service
%{_datadir}/tracker
%{_desktopdir}/tracker-needle.desktop
%{_desktopdir}/tracker-preferences.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_mandir}/man1/tracker-control.1*
%{_mandir}/man1/tracker-extract.1*
%{_mandir}/man1/tracker-import.1*
%{_mandir}/man1/tracker-info.1*
%{_mandir}/man1/tracker-miner-fs.1*
%{_mandir}/man1/tracker-needle.1*
%{_mandir}/man1/tracker-preferences.1*
%{_mandir}/man1/tracker-search.1*
%{_mandir}/man1/tracker-sparql.1*
%{_mandir}/man1/tracker-stats.1*
%{_mandir}/man1/tracker-store.1*
%{_mandir}/man1/tracker-tag.1*
%{_mandir}/man5/tracker-extract.cfg.5*
%{_mandir}/man5/tracker-fts.cfg.5*
%{_mandir}/man5/tracker-miner-fs.cfg.5*
%{_mandir}/man5/tracker-store.cfg.5*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtracker-client-%{ver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtracker-client-%{ver}.so.0
%attr(755,root,root) %{_libdir}/libtracker-extract-%{ver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtracker-extract-%{ver}.so.0
%attr(755,root,root) %{_libdir}/libtracker-miner-%{ver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtracker-miner-%{ver}.so.0
%attr(755,root,root) %{_libdir}/libtracker-sparql-%{ver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtracker-sparql-%{ver}.so.0
# required by libtracker-extract and libtracker-miner
%dir %{_libdir}/tracker-%{ver}
%attr(755,root,root) %{_libdir}/tracker-%{ver}/libtracker-common.so*
%attr(755,root,root) %{_libdir}/tracker-%{ver}/libtracker-data.so*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtracker-client-%{ver}.so
%attr(755,root,root) %{_libdir}/libtracker-extract-%{ver}.so
%attr(755,root,root) %{_libdir}/libtracker-miner-%{ver}.so
%attr(755,root,root) %{_libdir}/libtracker-sparql-%{ver}.so
%{_datadir}/vala/vapi/tracker-client-%{ver}.vapi
%{_datadir}/vala/vapi/tracker-miner-%{ver}.vapi
%{_datadir}/vala/vapi/tracker-sparql-%{ver}.vapi
%{_datadir}/vala/vapi/tracker-miner-%{ver}.deps
%{_datadir}/vala/vapi/tracker-sparql-%{ver}.deps
%{_includedir}/tracker-%{ver}
%{_pkgconfigdir}/tracker-client-%{ver}.pc
%{_pkgconfigdir}/tracker-extract-%{ver}.pc
%{_pkgconfigdir}/tracker-miner-%{ver}.pc
%{_pkgconfigdir}/tracker-sparql-%{ver}.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libtracker-client
%{_gtkdocdir}/libtracker-extract
%{_gtkdocdir}/libtracker-miner
%{_gtkdocdir}/libtracker-sparql
%{_gtkdocdir}/ontology

%files -n evolution-plugin-tracker
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/evolution/3.0/plugins/liborg-freedesktop-Tracker-evolution-plugin.so
%{_libdir}/evolution/3.0/plugins/org-freedesktop-Tracker-evolution-plugin.eplug

%files -n gnome-applet-tracker
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/tracker-search-bar
%{_datadir}/dbus-1/services/org.gnome.panel.applet.SearchBarFactory.service
%{_datadir}/gnome-panel/4.0/applets/org.gnome.panel.SearchBar.panel-applet
%{_mandir}/man1/tracker-search-bar.1*

%files -n nautilus-extension-tracker
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/nautilus/extensions-3.0/libnautilus-tracker-tags.so
