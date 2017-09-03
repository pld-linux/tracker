#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs
%bcond_with	evolution	# Evolution miner
%bcond_with	icu		# libicu instead of libunistring
%bcond_without	nautilus	# Nautilus extension
%bcond_with	static_libs	# static libraries
%bcond_without	vala		# Vala API

%define		ver	1.0
Summary:	Tracker - an indexing subsystem
Summary(pl.UTF-8):	Tracker - podsystem indeksujący
Name:		tracker
Version:	1.12.1
Release:	3
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/tracker/1.12/%{name}-%{version}.tar.xz
# Source0-md5:	e38b2ec4d2f3ebabd2e35bb5dd8408fa
Patch0:		link.patch
Patch1:		force-tb-fx-miners.patch
Patch2:		%{name}-docs.patch
URL:		http://projects.gnome.org/tracker/
BuildRequires:	NetworkManager-devel >= 0.8.0
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.11
BuildRequires:	dbus-devel >= 1.3.1
BuildRequires:	docbook-dtd412-xml
BuildRequires:	enca-devel >= 1.9
%if %{with evolution}
BuildRequires:	evolution-data-server-devel >= 3.2.0
BuildRequires:	evolution-devel >= 3.2.0
%endif
BuildRequires:	exempi-devel >= 2.1.0
# libavcodec >= 0.8.4 libavformat >= 0.8.4
BuildRequires:	ffmpeg-devel
BuildRequires:	flac-devel >= 1.2.1
BuildRequires:	gettext-tools
BuildRequires:	giflib-devel
BuildRequires:	glib2-devel >= 1:2.44.0
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	graphviz
BuildRequires:	gstreamer-devel >= 1.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0
BuildRequires:	gtk+3-devel >= 3.0.0
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.8}
BuildRequires:	gupnp-dlna-devel >= 0.9.4
BuildRequires:	intltool >= 0.40.0
BuildRequires:	json-glib-devel >= 1.0
BuildRequires:	libcue-devel
BuildRequires:	libexif-devel >= 0.6.13
BuildRequires:	libgee-devel >= 0.8
BuildRequires:	libgrss-devel >= 0.7
BuildRequires:	libgsf-devel >= 1.14.24
BuildRequires:	libgxps-devel
%{?with_icu:BuildRequires:	libicu-devel >= 4.8.1.1}
BuildRequires:	libiptcdata-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmediaart2-devel >= 1.9.0
BuildRequires:	libosinfo-devel >= 0.2.9
BuildRequires:	libpng-devel >= 2:1.2.24
BuildRequires:	libseccomp-devel >= 2.0
BuildRequires:	libsoup-devel >= 2.40
BuildRequires:	libstdc++-devel
BuildRequires:	libstemmer-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 2:2.2
%{!?with_icu:BuildRequires:	libunistring-devel}
BuildRequires:	libuuid-devel
BuildRequires:	libvorbis-devel >= 0.22
BuildRequires:	libxml2-devel >= 1:2.6.31
%{?with_nautilus:BuildRequires:	nautilus-devel >= 3.0.0}
BuildRequires:	pkgconfig
BuildRequires:	poppler-glib-devel >= 0.16.0
BuildRequires:	python >= 1:2.6
BuildRequires:	rpmbuild(macros) >= 1.673
BuildRequires:	sqlite3-devel >= 3.7.15
BuildRequires:	taglib-devel >= 1.6
BuildRequires:	tar >= 1:1.22
BuildRequires:	totem-pl-parser-devel >= 2.32.2-2
BuildRequires:	upower-devel >= 0.9.0
%{?with_vala:BuildRequires:	vala >= 2:0.18.0}
BuildRequires:	xz
BuildRequires:	zlib-devel
# meegotouch >= 0.20, libstreamanalyzer >= 0.7.0
Requires(post,postun):	glib2 >= 1:2.44.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name}-libs = %{version}-%{release}
Requires:	dbus >= 1.3.1
Requires:	flac >= 1.2.1
Requires:	gupnp-dlna >= 0.9.4
Requires:	hicolor-icon-theme
Requires:	libgrss >= 0.7
Requires:	libgsf >= 1.14.24
Requires:	libosinfo >= 0.2.9
Requires:	libpng >= 2:1.2.24
Requires:	libvorbis >= 0.22
Requires:	libxml2 >= 1:2.6.31
Requires:	poppler-glib >= 0.16.0
Requires:	taglib >= 1.6
Requires:	totem-pl-parser >= 2.32.2-2
Requires:	upower-libs >= 0.9.0
# for gunzip
Suggests:	gzip
Obsoletes:	gnome-applet-deskbar-extension-tracker
Obsoletes:	gnome-applet-tracker
Obsoletes:	tracker-search-gui
Obsoletes:	tracker-startup
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# circular dependencies: libtracker-data -> libtracker-libtracker-direct -> libtracker-sparql-backend [->] libtracker-data
%define		skip_post_check_so		.*%{_libdir}/tracker-1.0/libtracker-data.so.*

%description
Tracker is an indexing sub-system and search aggregator.

%description -l pl.UTF-8
Tracker jest podsystemem indeksującym i wyszukującym.

%package libs
Summary:	Tracker libraries
Summary(pl.UTF-8):	Biblioteki Trackera
Group:		Libraries
Requires:	NetworkManager-libs >= 0.8.0
Requires:	enca-libs >= 1.9
Requires:	exempi >= 2.1.0
Requires:	glib2 >= 1:2.44.0
Requires:	json-glib >= 1.0
Requires:	libexif >= 0.6.13
Requires:	libmediaart2 >= 1.9.0
Requires:	libseccomp >= 2.0
Requires:	libsoup >= 2.40
Requires:	sqlite3 >= 3.7.15
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
Requires:	glib2-devel >= 1:2.44.0
Requires:	libmediaart2-devel >= 1.9.0
Obsoletes:	libtracker-devel
Obsoletes:	libtracker-gtk-devel
Obsoletes:	libtracker-gtk-static
%{!?with_static_libs:Obsoletes:	libtracker-static}

%description devel
Header files for Tracker libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek Trackera.

%package static
Summary:	Static Tracker libraries
Summary(pl.UTF-8):	Statyczne biblioteki Trackera
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Tracker libraries.

%description static -l pl.UTF-8
Statyczne biblioteki Trackera.

%package apidocs
Summary:	Tracker libraries API documentation
Summary(pl.UTF-8):	Dokumentacja API bibliotek Trackera
Group:		Documentation
Requires:	gtk-doc-common
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
Tracker libraries API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API bibliotek Trackera.

%package -n bash-completion-tracker
Summary:	Bash completion for tracker command
Summary(pl.UTF-8):	Bashowe uzupełnianie parametrów dla polecenia tracker
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 2.0

%description -n bash-completion-tracker
Bash completion for tracker command.

%description -n bash-completion-tracker -l pl.UTF-8
Bashowe uzupełnianie parametrów dla polecenia tracker.

%package -n evolution-plugin-tracker
Summary:	Tracker plugin for Evolution
Summary(pl.UTF-8):	Wtyczka Trackera do Evolution
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	evolution >= 3.2.0
Requires:	evolution-data-server-devel >= 3.2.0

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
This package adds Tracker integration to Nautilus.

%description -n nautilus-extension-tracker -l pl.UTF-8
Ten pakiet dodaje integrację Trackera z Nautilusem.

%package -n firefox-extension-tracker
Summary:	Tracker extension for Firefox
Summary(pl.UTF-8):	Rozszerzenie Trackera dla Firefox
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	firefox >= 22.0
Obsoletes:	iceweasel-extension-tracker

%description -n firefox-extension-tracker
This package adds Tracker integration to Firefox.

%description -n firefox-extension-tracker -l pl.UTF-8
Ten pakiet dodaje integrację Trackera z Firefoksem.

%package -n thunderbird-extension-tracker
Summary:	Tracker extension for Thunderbird
Summary(pl.UTF-8):	Rozszerzenie Trackera dla Thunderbird
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	thunderbird >= 5.0
Obsoletes:	icedove-extension-tracker
BuildArch:	noarch

%description -n thunderbird-extension-tracker
This package adds Tracker integration to Thunderbird.

%description -n thunderbird-extension-tracker -l pl.UTF-8
Ten pakiet dodaje integrację Trackera z programem Thunderbird.

%package -n vala-tracker
Summary:	tracker API for Vala language
Summary(pl.UTF-8):	API tracker dla języka Vala
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 2:0.18.0
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n vala-tracker
tracker API for Vala language.

%description -n vala-tracker -l pl.UTF-8
API tracker dla języka Vala.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
CPPFLAGS="%{rpmcppflags} -I/usr/include/libstemmer"
%configure \
	%{__enable_disable apidocs gtk-doc} \
	--disable-hal \
	--enable-libcue \
	--enable-libflac \
	--enable-libvorbis \
	%{__enable_disable evolution miner-evolution} \
	--enable-miner-firefox \
	--enable-miner-thunderbird \
	%{__enable_disable nautilus nautilus-extension} \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static} \
	--disable-unit-tests \
	--with-firefox-plugin-dir=%{_datadir}/firefox/browser/extensions \
	--with-html-dir=%{_gtkdocdir} \
	--with-thunderbird-plugin-dir=%{_datadir}/thunderbird/extensions \
	--with-unicode-support=%{?with_icu:libicu}%{!?with_icu:libunistring}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/tracker-%{ver}/*/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/tracker-%{ver}/*.la
%{?with_evolution:%{__rm} $RPM_BUILD_ROOT%{_libdir}/evolution/*/plugins/*.la}
%{?with_nautilus:%{__rm} $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-*/*.la}
%if %{with static_libs}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/tracker-%{ver}/libtracker-*.a
%{__rm} $RPM_BUILD_ROOT%{_libdir}/tracker-%{ver}/*/lib*.a
%endif


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
%attr(755,root,root) %{_bindir}/tracker
%attr(755,root,root) %{_bindir}/tracker-needle
%attr(755,root,root) %{_bindir}/tracker-preferences
%attr(755,root,root) %{_libdir}/tracker-extract
%attr(755,root,root) %{_libdir}/tracker-miner-apps
%attr(755,root,root) %{_libdir}/tracker-miner-fs
%attr(755,root,root) %{_libdir}/tracker-miner-rss
%attr(755,root,root) %{_libdir}/tracker-miner-user-guides
%attr(755,root,root) %{_libdir}/tracker-store
%attr(755,root,root) %{_libdir}/tracker-writeback
%dir %{_libdir}/tracker-%{ver}/extract-modules
%attr(755,root,root) %{_libdir}/tracker-%{ver}/extract-modules/libextract-abw.so
%attr(755,root,root) %{_libdir}/tracker-%{ver}/extract-modules/libextract-bmp.so
%attr(755,root,root) %{_libdir}/tracker-%{ver}/extract-modules/libextract-dvi.so
%attr(755,root,root) %{_libdir}/tracker-%{ver}/extract-modules/libextract-dummy.so
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
%{_sysconfdir}/xdg/autostart/tracker-extract.desktop
%{_sysconfdir}/xdg/autostart/tracker-miner-apps.desktop
%{_sysconfdir}/xdg/autostart/tracker-miner-fs.desktop
%{_sysconfdir}/xdg/autostart/tracker-miner-rss.desktop
%{_sysconfdir}/xdg/autostart/tracker-miner-user-guides.desktop
%{_sysconfdir}/xdg/autostart/tracker-store.desktop
%{_datadir}/appdata/tracker-needle.appdata.xml
%{_datadir}/appdata/tracker-preferences.appdata.xml
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.Miner.Extract.service
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.Miner.Applications.service
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.Miner.Files.service
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.Miner.RSS.service
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.Miner.Userguides.service
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.Writeback.service
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.service
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker.DB.gschema.xml
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker.Extract.gschema.xml
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker.FTS.gschema.xml
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker.Miner.Files.gschema.xml
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker.Needle.gschema.xml
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker.Store.gschema.xml
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker.Writeback.gschema.xml
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker.enums.xml
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker.gschema.xml
%{_datadir}/tracker
%dir %{_datadir}/xul-ext
%{_desktopdir}/tracker-needle.desktop
%{_desktopdir}/tracker-preferences.desktop
%{_iconsdir}/hicolor/*/apps/tracker.png
%{_iconsdir}/hicolor/*/apps/tracker.svg
%{systemduserunitdir}/tracker-extract.service
%{systemduserunitdir}/tracker-miner-apps.service
%{systemduserunitdir}/tracker-miner-fs.service
%{systemduserunitdir}/tracker-miner-rss.service
%{systemduserunitdir}/tracker-miner-user-guides.service
%{systemduserunitdir}/tracker-store.service
%{systemduserunitdir}/tracker-writeback.service
%{_mandir}/man1/tracker-daemon.1*
%{_mandir}/man1/tracker-extract.1*
%{_mandir}/man1/tracker-index.1*
%{_mandir}/man1/tracker-info.1*
%{_mandir}/man1/tracker-miner-fs.1*
%{_mandir}/man1/tracker-miner-rss.1*
%{_mandir}/man1/tracker-needle.1*
%{_mandir}/man1/tracker-preferences.1*
%{_mandir}/man1/tracker-reset.1*
%{_mandir}/man1/tracker-search.1*
%{_mandir}/man1/tracker-sparql.1*
%{_mandir}/man1/tracker-sql.1*
%{_mandir}/man1/tracker-status.1*
%{_mandir}/man1/tracker-store.1*
%{_mandir}/man1/tracker-tag.1*
%{_mandir}/man1/tracker-writeback.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtracker-control-%{ver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtracker-control-%{ver}.so.0
%attr(755,root,root) %{_libdir}/libtracker-miner-%{ver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtracker-miner-%{ver}.so.0
%attr(755,root,root) %{_libdir}/libtracker-sparql-%{ver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtracker-sparql-%{ver}.so.0
# required by libtracker-miner
%dir %{_libdir}/tracker-%{ver}
%attr(755,root,root) %{_libdir}/tracker-%{ver}/libtracker-common.so*
%attr(755,root,root) %{_libdir}/tracker-%{ver}/libtracker-data.so*
%attr(755,root,root) %{_libdir}/tracker-%{ver}/libtracker-extract.so*
%{_libdir}/girepository-1.0/Tracker-%{ver}.typelib
%{_libdir}/girepository-1.0/TrackerControl-%{ver}.typelib
%{_libdir}/girepository-1.0/TrackerMiner-%{ver}.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtracker-control-%{ver}.so
%attr(755,root,root) %{_libdir}/libtracker-miner-%{ver}.so
%attr(755,root,root) %{_libdir}/libtracker-sparql-%{ver}.so
%{_includedir}/tracker-%{ver}
%{_pkgconfigdir}/tracker-control-%{ver}.pc
%{_pkgconfigdir}/tracker-miner-%{ver}.pc
%{_pkgconfigdir}/tracker-sparql-%{ver}.pc
%{_datadir}/gir-1.0/Tracker-%{ver}.gir
%{_datadir}/gir-1.0/TrackerControl-%{ver}.gir
%{_datadir}/gir-1.0/TrackerMiner-%{ver}.gir

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libtracker-control-%{ver}.a
%{_libdir}/libtracker-miner-%{ver}.a
%{_libdir}/libtracker-sparql-%{ver}.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libtracker-control
%{_gtkdocdir}/libtracker-miner
%{_gtkdocdir}/libtracker-sparql
%{_gtkdocdir}/ontology
%endif

%files -n bash-completion-tracker
%defattr(644,root,root,755)
%{bash_compdir}/tracker

%if %{with evolution}
%files -n evolution-plugin-tracker
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/evolution/3.4/plugins/liborg-freedesktop-Tracker-evolution-plugin.so
%{_libdir}/evolution/3.4/plugins/org-freedesktop-Tracker-evolution-plugin.eplug
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.Miner.EMails.service
%endif

%if %{with nautilus}
%files -n nautilus-extension-tracker
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/nautilus/extensions-3.0/libnautilus-tracker-tags.so
%endif

%files -n firefox-extension-tracker
%defattr(644,root,root,755)
%{_datadir}/firefox/browser/extensions/trackerfox@bustany.org
%{_datadir}/xul-ext/trackerfox

%files -n thunderbird-extension-tracker
%defattr(644,root,root,755)
%{_desktopdir}/trackerbird-launcher.desktop
%{_datadir}/thunderbird/extensions/trackerbird@bustany.org
%{_datadir}/xul-ext/trackerbird

%if %{with vala}
%files -n vala-tracker
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/tracker-control-%{ver}.deps
%{_datadir}/vala/vapi/tracker-control-%{ver}.vapi
%{_datadir}/vala/vapi/tracker-miner-%{ver}.deps
%{_datadir}/vala/vapi/tracker-miner-%{ver}.vapi
%{_datadir}/vala/vapi/tracker-sparql-%{ver}.deps
%{_datadir}/vala/vapi/tracker-sparql-%{ver}.vapi
%endif
