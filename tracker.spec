# Conditional build:
%bcond_without	exif
%bcond_without	pdf
%bcond_without	libxml2
%bcond_without	gsf		# build without libgsf support
%bcond_without	gui		# don't build GNOME based GUI
%bcond_with	sqlite3		# use sqlite3 instead of sqlite2
#
Summary:	Tracker - An indexing subsystem
Summary(pl.UTF-8):	Tracker - podsystem indeksujący
Name:		tracker
Version:	0.6.3
Release:	0.1
License:	GPL v.2
Group:		Libraries
Source0:	http://www.gnome.org/~jamiemcc/tracker/%{name}-%{version}.tar.bz2
# Source0-md5:	f718aa38b7527229f5567834ae247a38
URL:		http://www.gnome.org/projects/tracker/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2:2.10.10
BuildRequires:	gmime-devel >= 2.1.0
BuildRequires:	libexif-devel >= 0.6.13
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel >= 1:2.16.1
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.27
BuildRequires:	pkgconfig
BuildRequires:	python-devel
%if %{with sqlite3}
BuildRequires:	sqlite3-devel >= 3.3.4
%else
BuildRequires:	sqlite-devel
%endif
BuildRequires:	wv-devel >= 1.2.4
BuildRequires:	zlib-devel
# GUI BRs
%if %{with gui}
BuildRequires:	gnome-vfs2-devel >= 2.18.0.1
%endif
Requires:	%{name}-libs = %{version}-%{release}
Requires:	sqlite3
Requires:	poppler
Requires:	file
Requires:	w3m
Requires:	wv >= 1.0.2

BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tracker is an indexing sub-system and search aggregator.

%description -l pl.UTF-8
Tracker jest podsystemem indeksującym i wyszukuj�cym.

%package libs
Summary:	Tracker libraries
Summary(pl.UTF-8):	Bibiloteki Tracker
Group:		Libraries

%description libs
Tracker libraries.

%description libs -l pl.UTF-8
Bibiloteki Tracker.

%package devel
Summary:	Tracker development files
Summary(pl.UTF-8):	Pliki programistyczne Tracker
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Tracker development files.

%description devel -l pl.UTF-8
Pliki programistyczne Tracker.

%package static
Summary:	Tracker static libraries
Summary(pl.UTF-8):	Statyczne biblioteki Tracker
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Tracker static libraries.

%description static -l pl.UTF-8
Statyczne biblioteki Tracker.

%package search-gui
Summary:	GNOME based Tracker GUI
Summary(pl.UTF-8):	Oparty na GNOME graficzny interfejs dla Tracker
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2 >= 2:2.10.10

%description search-gui
GNOME based Tracker GUI.

%description search-gui -l pl.UTF-8
Oparty na GNOME graficzny interfejs dla Tracker.

%package startup
Summary:	Automatic startup integration for Tracker
Summary(pl.UTF-8):	Integracja funkcji automatycznego startu Tracker
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Obsoletes:	tracker-gnome

%description startup
Automatic session startup integration for Tracker.

%description startup -l pl.UTF-8
Integracja funkcji automatycznego startu Tracker.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-static \
	%{?with_apidocs:--enable-gtk-doc} \
	--with-html-dir=%{_gtkdocdir} \
	--%{!?with_gui:dis}%{?with_gui:en}able-gui \
	--%{!?with_gui:dis}%{?with_gui:en}able-deskbar-applet \
	--%{!?with_gui:dis}%{?with_gui:en}able-libtrackergtk \
	--%{!?with_gsf:dis}%{?with_gsf:en}able-gsf \
	--%{!?with_xmp:dis}%{?with_xmp:en}able-xmp \
	--%{!?with_exif:dis}%{?with_exif:en}able-exif \
	--%{!?with_pdf:dis}%{?with_pdf:en}able-pdf \
	--%{!?with_libxml2:dis}%{?with_libxml2:en}able-libxml2 \
	--enable-preferences
#--enable-external-sqlite
#--enable-video-extractor=ARG enables one of the (gstreamer, xine, external, auto)
#--enable-file-monitoring=ARG enables one of the (inotify, fam, polling, auto)

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/o3totxt
%attr(755,root,root) %{_bindir}/trackerd
%attr(755,root,root) %{_bindir}/tracker-extract
%attr(755,root,root) %{_bindir}/tracker-files
%attr(755,root,root) %{_bindir}/tracker-thumbnailer
%attr(755,root,root) %{_bindir}/tracker-meta-folder
%attr(755,root,root) %{_bindir}/tracker-query
%attr(755,root,root) %{_bindir}/tracker-search
%attr(755,root,root) %{_bindir}/tracker-status
%attr(755,root,root) %{_bindir}/tracker-tag
%attr(755,root,root) %{_bindir}/tracker-stats
%{_datadir}/dbus-1/services/tracker.service
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/thumbnailers
%dir %{_libdir}/%{name}/thumbnailers/application
%dir %{_libdir}/%{name}/thumbnailers/image
%attr(755,root,root) %{_libdir}/%{name}/thumbnailers/application/pdf_thumbnailer
%attr(755,root,root) %{_libdir}/%{name}/thumbnailers/application/vnd.oasis.opendocument.*_thumbnailer
%attr(755,root,root) %{_libdir}/%{name}/thumbnailers/image/*_thumbnailer
%{_libdir}/%{name}/filters
%{_mandir}/man*/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/services
%{_datadir}/%{name}/sqlite-*.sql

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/libtracker-gtk
%{_includedir}/*.h
%{_libdir}/*.la
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

%if %{with gui}
%files search-gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tracker-search-tool
%attr(755,root,root) %{_bindir}/tracker-preferences
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/*/apps/*.svg
%{_desktopdir}/*.desktop
%{_datadir}/%{name}/tracker-introspect.xml
%{_datadir}/%{name}/tracker-preferences.glade
%dir %{_datadir}/%{name}/icons
%{_datadir}/%{name}/icons/thumbnail_frame.png
%dir %{_datadir}/%{name}/languages
%{_datadir}/%{name}/languages/stopwords.da
%{_datadir}/%{name}/languages/stopwords.de
%{_datadir}/%{name}/languages/stopwords.en
%{_datadir}/%{name}/languages/stopwords.es
%{_datadir}/%{name}/languages/stopwords.fi
%{_datadir}/%{name}/languages/stopwords.fr
%{_datadir}/%{name}/languages/stopwords.it
%{_datadir}/%{name}/languages/stopwords.nb
%{_datadir}/%{name}/languages/stopwords.nl
%{_datadir}/%{name}/languages/stopwords.pt
%{_datadir}/%{name}/languages/stopwords.ru
%{_datadir}/%{name}/languages/stopwords.sv
%endif

%files startup
%defattr(644,root,root,755)
%{_sysconfdir}/xdg/autostart/trackerd.desktop
