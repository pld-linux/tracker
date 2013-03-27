#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs
%bcond_with	evolution	# build with Evolution miner
%bcond_without	vala		# do not build Vala API
#
%define		ver	0.16
Summary:	Tracker - an indexing subsystem
Summary(pl.UTF-8):	Tracker - podsystem indeksujący
Name:		tracker
Version:	0.16.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/tracker/0.16/%{name}-%{version}.tar.xz
# Source0-md5:	3f68c0141ed0442ba2977583981972c0
Patch0:		link.patch
Patch1:		force-tb-fx-miners.patch
URL:		http://projects.gnome.org/tracker/
BuildRequires:	NetworkManager-devel >= 0.8.0
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.11
BuildRequires:	dbus-devel >= 1.3.1
BuildRequires:	dbus-glib-devel >= 0.82
BuildRequires:	docbook-dtd412-xml
BuildRequires:	enca-devel >= 1.9
%if %{with evolution}
BuildRequires:	evolution-data-server-devel >= 3.1.0
BuildRequires:	evolution-devel >= 3.1.0
%endif
BuildRequires:	exempi-devel >= 2.1.0
BuildRequires:	flac-devel >= 1.2.1
BuildRequires:	gettext-devel
BuildRequires:	giflib-devel
BuildRequires:	glib2-devel >= 1:2.36.0
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	graphviz
BuildRequires:	gstreamer-devel >= 0.10.31
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.31
BuildRequires:	gtk+3-devel
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.8}
BuildRequires:	gupnp-dlna-devel >= 0.9.4
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libcue-devel
BuildRequires:	libexif-devel >= 0.6.13
BuildRequires:	libgee-devel >= 0.8
BuildRequires:	libgnome-keyring-devel >= 2.26.0
BuildRequires:	libgrss-devel >= 0.5
BuildRequires:	libgsf-devel >= 1.14.7
BuildRequires:	libgxps-devel
BuildRequires:	libiptcdata-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libosinfo-devel >= 0.0.2
BuildRequires:	libpng-devel >= 2:1.2.24
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 2:2.2
BuildRequires:	libunistring-devel
BuildRequires:	libuuid-devel
BuildRequires:	libvorbis-devel >= 0.22
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	nautilus-devel >= 3.0.0
BuildRequires:	pkgconfig
BuildRequires:	poppler-glib-devel >= 0.16.0
BuildRequires:	rest-devel >= 0.7
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	sqlite3-devel >= 3.7.9
BuildRequires:	taglib-devel >= 1.6
BuildRequires:	tar >= 1:1.22
BuildRequires:	totem-pl-parser-devel >= 2.32.2-2
BuildRequires:	upower-devel >= 0.9.0
%{?with_vala:BuildRequires:	vala >= 1:0.14.0}
BuildRequires:	xine-lib-devel >= 1.0
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires(post,postun):	glib2 >= 1:2.36.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name}-libs = %{version}-%{release}
Requires:	hicolor-icon-theme
# for gunzip
Suggests:	gzip
Obsoletes:	gnome-applet-deskbar-extension-tracker
Obsoletes:	gnome-applet-tracker
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
Requires:	glib2-devel >= 1:2.36.0
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
Requires:	evolution >= 3.1.0

%description -n evolution-plugin-tracker
Tracker plugin for Evolution.

%description -n evolution-plugin-tracker -l pl.UTF-8
Wtyczka Trackera do Evolution.

%package -n nautilus-extension-tracker
Summary:	Tracker extension for Nautilus
Summary(pl.UTF-8):	Rozszerzenie Trackera dla Nautilusa
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	nautilus >= 3.0.0

%description -n nautilus-extension-tracker
Adds Tracker integration to Nautilus.

%description -n nautilus-extension-tracker -l pl.UTF-8
Dodaje integrację Trackera z Nautilusem.

%package -n iceweasel-extension-tracker
Summary:	Tracker extension for Iceweasel
Summary(pl.UTF-8):	Rozszerzenie Trackera dla Iceweasel
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	iceweasel >= 4.0

%description -n iceweasel-extension-tracker
Adds Tracker integration to Iceweasel.

%description -n iceweasel-extension-tracker -l pl.UTF-8
Dodaje integrację Trackera z Iceweasel.

%package -n icedove-extension-tracker
Summary:	Tracker extension for Icedove
Summary(pl.UTF-8):	Rozszerzenie Trackera dla Icedove
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	icedove >= 5.0

%description -n icedove-extension-tracker
Adds Tracker integration to Icedove.

%description -n icedove-extension-tracker -l pl.UTF-8
Dodaje integrację Trackera z Icedove.

%package -n vala-tracker
Summary:	tracker API for Vala language
Summary(pl.UTF-8):	API tracker dla języka Vala
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description -n vala-tracker
tracker API for Vala language.

%description -n vala-tracker -l pl.UTF-8
API tracker dla języka Vala.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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
	--enable-libcue \
	%{__enable_disable apidocs gtk-doc} \
	%{__enable_disable evolution miner-evolution} \
	--enable-gdkpixbuf \
	--with-html-dir=%{_gtkdocdir} \
	--enable-miner-firefox \
	--with-firefox-plugin-dir=%{_datadir}/iceweasel/extensions \
	--enable-miner-thunderbird \
	--with-thunderbird-plugin-dir=%{_datadir}/icedove/extensions \
	--disable-unit-tests \
	--disable-silent-rules \
	--disable-hal

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{?with evolution:%{__rm} $RPM_BUILD_ROOT%{_libdir}/evolution/*/plugins/*.la}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/tracker-%{ver}/*/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/tracker-%{ver}/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-*/*.la

%find_lang tracker

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%glib_compile_schemas

%postun
%update_icon_cache hicolor
%glib_compile_schemas

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f tracker.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tracker-control
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
%attr(755,root,root) %{_libdir}/tracker-%{ver}/extract-modules/libextract-dvi.so
%attr(755,root,root) %{_libdir}/tracker-%{ver}/extract-modules/libextract-epub.so
%attr(755,root,root) %{_libdir}/tracker-%{ver}/extract-modules/libextract-flac.so
%attr(755,root,root) %{_libdir}/tracker-%{ver}/extract-modules/libextract-gif.so
%attr(755,root,root) %{_libdir}/tracker-%{ver}/extract-modules/libextract-gstreamer.so
%attr(755,root,root) %{_libdir}/tracker-%{ver}/extract-modules/libextract-html.so
%attr(755,root,root) %{_libdir}/tracker-%{ver}/extract-modules/libextract-icon.so
%attr(755,root,root) %{_libdir}/tracker-%{ver}/extract-modules/libextract-iso.so
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
%attr(755,root,root) %{_libdir}/tracker-%{ver}/extract-modules/libextract-xps.so
%dir %{_libdir}/tracker-%{ver}/writeback-modules
%attr(755,root,root) %{_libdir}/tracker-%{ver}/writeback-modules/libwriteback-taglib.so
%attr(755,root,root) %{_libdir}/tracker-%{ver}/writeback-modules/libwriteback-xmp.so
%{_sysconfdir}/xdg/autostart/tracker-miner-fs.desktop
%{_sysconfdir}/xdg/autostart/tracker-miner-rss.desktop
%{_sysconfdir}/xdg/autostart/tracker-store.desktop
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.Extract.service
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.Miner.Applications.service
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.Miner.Files.service
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.Miner.RSS.service
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.Writeback.service
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.service
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker.DB.gschema.xml
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker.Extract.gschema.xml
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker.FTS.gschema.xml
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker.Miner.Files.gschema.xml
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker.Store.gschema.xml
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker.Writeback.gschema.xml
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker.enums.xml
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker.gschema.xml
%{_datadir}/tracker
%dir %{_datadir}/xul-ext
%{_desktopdir}/tracker-needle.desktop
%{_desktopdir}/tracker-preferences.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_mandir}/man1/tracker-control.1*
%{_mandir}/man1/tracker-extract.1*
%{_mandir}/man1/tracker-import.1*
%{_mandir}/man1/tracker-info.1*
%{_mandir}/man1/tracker-miner-fs.1*
%{_mandir}/man1/tracker-miner-rss.1*
%{_mandir}/man1/tracker-needle.1*
%{_mandir}/man1/tracker-preferences.1*
%{_mandir}/man1/tracker-search.1*
%{_mandir}/man1/tracker-sparql.1*
%{_mandir}/man1/tracker-stats.1*
%{_mandir}/man1/tracker-store.1*
%{_mandir}/man1/tracker-tag.1*
%{_mandir}/man1/tracker-writeback.1*

%files libs
%defattr(644,root,root,755)
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
%{_libdir}/girepository-1.0/Tracker-%{ver}.typelib
%{_libdir}/girepository-1.0/TrackerExtract-%{ver}.typelib
%{_libdir}/girepository-1.0/TrackerMiner-%{ver}.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtracker-extract-%{ver}.so
%attr(755,root,root) %{_libdir}/libtracker-miner-%{ver}.so
%attr(755,root,root) %{_libdir}/libtracker-sparql-%{ver}.so
%{_includedir}/tracker-%{ver}
%{_pkgconfigdir}/tracker-extract-%{ver}.pc
%{_pkgconfigdir}/tracker-miner-%{ver}.pc
%{_pkgconfigdir}/tracker-sparql-%{ver}.pc
%{_datadir}/gir-1.0/Tracker-%{ver}.gir
%{_datadir}/gir-1.0/TrackerExtract-%{ver}.gir
%{_datadir}/gir-1.0/TrackerMiner-%{ver}.gir

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libtracker-extract
%{_gtkdocdir}/libtracker-miner
%{_gtkdocdir}/libtracker-sparql
%{_gtkdocdir}/ontology
%endif

%if %{with evolution}
%files -n evolution-plugin-tracker
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/evolution/3.4/plugins/liborg-freedesktop-Tracker-evolution-plugin.so
%{_libdir}/evolution/3.4/plugins/org-freedesktop-Tracker-evolution-plugin.eplug
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.Miner.EMails.service
%endif

%files -n nautilus-extension-tracker
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/nautilus/extensions-3.0/libnautilus-tracker-tags.so

%files -n iceweasel-extension-tracker
%defattr(644,root,root,755)
%{_datadir}/iceweasel/extensions/trackerfox@bustany.org
%{_datadir}/xul-ext/trackerfox

%files -n icedove-extension-tracker
%defattr(644,root,root,755)
%{_desktopdir}/trackerbird-launcher.desktop
%{_datadir}/icedove/extensions/trackerbird@bustany.org
%{_datadir}/xul-ext/trackerbird

%if %{with vala}
%files -n vala-tracker
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/tracker-miner-%{ver}.deps
%{_datadir}/vala/vapi/tracker-miner-%{ver}.vapi
%{_datadir}/vala/vapi/tracker-sparql-%{ver}.deps
%{_datadir}/vala/vapi/tracker-sparql-%{ver}.vapi
%endif
