#
# Conditional build:
%bcond_without	deskbar_applet	# don't build GNOME Deskbar applet extension
%bcond_without	gui		# don't build GNOME based GUI
#
Summary:	Tracker - an indexing subsystem
Summary(pl.UTF-8):	Tracker - podsystem indeksujący
Name:		tracker
Version:	0.6.6
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://www.gnome.org/~jamiemcc/tracker/%{name}-%{version}.tar.bz2
# Source0-md5:	0845998f8f0d715b3f1b306d59fdae4d
URL:		http://www.tracker-project.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
%{?with_gui:BuildRequires:	dbus-glib-devel >= 0.74}
%{?with_deskbar_applet:BuildRequires:	gnome-applet-deskbar-devel >= 2.20.0}
BuildRequires:	exempi-devel >= 1.99.5
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.14.5
BuildRequires:	gmime-devel >= 2.2.15
%{?with_gui:BuildRequires:	gnome-common >= 2.20.0}
%{?with_gui:BuildRequires:	gnome-desktop-devel >= 2.20.0}
%{?with_gui:BuildRequires:	gnome-vfs2-devel >= 2.20.0}
BuildRequires:	gstreamer-devel >= 0.10.15
%{?with_gui:BuildRequires:	gtk+2-devel >= 2:2.12.5}
BuildRequires:	hal-devel >= 0.5.10
BuildRequires:	intltool >= 0.37.0
BuildRequires:	libexif-devel >= 0.6.13
%{?with_gui:BuildRequires:	libglade2-devel >= 1:2.6.2}
%{?with_gui:BuildRequires:	libgnomeui-devel >= 2.20.0}
BuildRequires:	libgsf-devel >= 1.14.7
%{?with_gui:BuildRequires:	libnotify-devel >= 0.4.3}
BuildRequires:	libpng-devel >= 1.2.24
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	pkgconfig
BuildRequires:	poppler-glib-devel >= 0.6
BuildRequires:	qdbm-devel >= 1.8
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	sqlite3-devel >= 3.4.0
BuildRequires:	zlib-devel
Requires:	libtracker = %{version}-%{release}
Suggests:	/usr/bin/pdftotext
# for convert
Suggests:	ImageMagick
Suggests:	djvulibre
# for evince-thumbnailer
Suggests:	evince
# for ssindex
Suggests:	gnumeric
Suggests:	libxslt-progs
Suggests:	w3m
Suggests:	wv
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tracker is an indexing sub-system and search aggregator.

%description -l pl.UTF-8
Tracker jest podsystemem indeksującym i wyszukującym.

%package search-gui
Summary:	GNOME based Tracker GUI
Summary(pl.UTF-8):	Oparty na GNOME graficzny interfejs dla Tracker
Group:		X11/Applications
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires:	%{name} = %{version}-%{release}
Requires:	libtracker-gtk = %{version}-%{release}

%description search-gui
GNOME based Tracker GUI.

%description search-gui -l pl.UTF-8
Oparty na GNOME graficzny interfejs dla Tracker.

%package startup
Summary:	Automatic startup integration for Tracker
Summary(pl.UTF-8):	Integracja funkcji automatycznego startu Tracker
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description startup
Automatic session startup integration for Tracker.

%description startup -l pl.UTF-8
Integracja funkcji automatycznego startu Tracker.

%package -n gnome-applet-deskbar-extension-tracker
Summary:	Tracker extension for GNOME Deskbar applet
Summary(pl.UTF-8):	Rozszerzenie Trackera dla apletu GNOME Deskbar
Group:		X11/Applications
Requires:	gnome-applet-deskbar >= 2.20.0
Requires:	%{name}-search-gui = %{version}-%{release}

%description -n gnome-applet-deskbar-extension-tracker
Tracker extension for GNOME Deskbar applet.

%description -n gnome-applet-deskbar-extension-tracker -l pl.UTF-8
Rozszerzenie Trackera do apletu GNOME Deskbar.

%package -n libtracker
Summary:	Tracker library
Summary(pl.UTF-8):	Biblioteka Tracker
Group:		Libraries

%description -n libtracker
Tracker library.

%description -n libtracker -l pl.UTF-8
Biblioteka Tracker.

%package -n libtracker-devel
Summary:	Header files for Tracker library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Tracker
Group:		Development/Libraries
Requires:	dbus-glib-devel >= 0.74
Requires:	glib2-devel >= 1:2.14.5
Requires:	libtracker = %{version}-%{release}

%description -n libtracker-devel
Header files for Tracker library.

%description -n libtracker-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Tracker.

%package -n libtracker-static
Summary:	Static Tracker library
Summary(pl.UTF-8):	Statyczna biblioteka Tracker
Group:		Development/Libraries
Requires:	libtracker-devel = %{version}-%{release}

%description -n libtracker-static
Static Tracker library.

%description -n libtracker-static -l pl.UTF-8
Statyczna biblioteka Tracker.

%package -n libtracker-gtk
Summary:	Tracker-gtk library
Summary(pl.UTF-8):	Biblioteka Tracker-gtk
Group:		X11/Libraries

%description -n libtracker-gtk
Tracker-gtk library.

%description -n libtracker-gtk -l pl.UTF-8
Biblioteka Tracker-gtk.

%package -n libtracker-gtk-devel
Summary:	Header files for Tracker-gtk library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Tracker-gtk
Group:		X11/Development/Libraries
Requires:	dbus-glib-devel >= 0.74
Requires:	gtk+2-devel >= 2:2.12.5
Requires:	libtracker-devel = %{version}-%{release}
Requires:	libtracker-gtk = %{version}-%{release}

%description -n libtracker-gtk-devel
Header files for Tracker-gtk library.

%description -n libtracker-gtk-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Tracker-gtk.

%package -n libtracker-gtk-static
Summary:	Static Tracker-gtk library
Summary(pl.UTF-8):	Statyczna biblioteka Tracker-gtk
Group:		X11/Development/Libraries
Requires:	libtracker-gtk-devel = %{version}-%{release}

%description -n libtracker-gtk-static
Static Tracker-gtk library.

%description -n libtracker-gtk-static -l pl.UTF-8
Statyczna biblioteka Tracker-gtk.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%if %{with deskbar_applet}
	--enable-deskbar-applet=module \
	%else
	--disable-deskbar-applet \
	%endif
	--enable-external-qdbm \
	--enable-video-extractor=gstreamer \
	--enable-file-monitoring=inotify \
	%{?!with_gui:--disable-gui} \
	%{?!with_gui:--disable-libtrackergtk} \
	%{?!with_gui:--disable-trackerapplet} \
	%{?!with_gui:--disable-preferences}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with deskbar_applet}
%py_comp $RPM_BUILD_ROOT%{_libdir}/deskbar-applet/modules-2.20-compatible
%py_ocomp $RPM_BUILD_ROOT%{_libdir}/deskbar-applet/modules-2.20-compatible
rm -f $RPM_BUILD_ROOT%{_libdir}/deskbar-applet/modules-2.20-compatible/*.py
%endif

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post search-gui
%update_icon_cache hicolor

%postun search-gui
%update_icon_cache hicolor

%post -n libtracker -p /sbin/ldconfig
%postun	-n libtracker -p /sbin/ldconfig

%post -n libtracker-gtk -p /sbin/ldconfig
%postun	-n libtracker-gtk -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/o3totxt
%attr(755,root,root) %{_bindir}/tracker-extract
%attr(755,root,root) %{_bindir}/tracker-files
%attr(755,root,root) %{_bindir}/tracker-meta-folder
%attr(755,root,root) %{_bindir}/tracker-query
%attr(755,root,root) %{_bindir}/tracker-search
%attr(755,root,root) %{_bindir}/tracker-stats
%attr(755,root,root) %{_bindir}/tracker-status
%attr(755,root,root) %{_bindir}/tracker-tag
%attr(755,root,root) %{_bindir}/tracker-thumbnailer
%attr(755,root,root) %{_bindir}/trackerd
%dir %{_libdir}/tracker
%dir %{_libdir}/tracker/extract-modules
%attr(755,root,root) %{_libdir}/tracker/extract-modules/libextract*.so
%dir %{_libdir}/tracker/filters
%dir %{_libdir}/tracker/filters/application
%attr(755,root,root) %{_libdir}/tracker/filters/application/csv_filter
%attr(755,root,root) %{_libdir}/tracker/filters/application/msword_filter
%attr(755,root,root) %{_libdir}/tracker/filters/application/pdf_filter
%attr(755,root,root) %{_libdir}/tracker/filters/application/tab-separated-values_filter
%attr(755,root,root) %{_libdir}/tracker/filters/application/vnd.ms-excel_filter
%attr(755,root,root) %{_libdir}/tracker/filters/application/vnd.oasis.opendocument.presentation-template_filter
%attr(755,root,root) %{_libdir}/tracker/filters/application/vnd.oasis.opendocument.presentation_filter
%attr(755,root,root) %{_libdir}/tracker/filters/application/vnd.oasis.opendocument.spreadsheet-template_filter
%attr(755,root,root) %{_libdir}/tracker/filters/application/vnd.oasis.opendocument.spreadsheet_filter
%attr(755,root,root) %{_libdir}/tracker/filters/application/vnd.oasis.opendocument.text-template_filter
%attr(755,root,root) %{_libdir}/tracker/filters/application/vnd.oasis.opendocument.text_filter
%attr(755,root,root) %{_libdir}/tracker/filters/application/vnd.stardivision.writer_filter
%attr(755,root,root) %{_libdir}/tracker/filters/application/vnd.sun.xml.calc.template_filter
%attr(755,root,root) %{_libdir}/tracker/filters/application/vnd.sun.xml.calc_filter
%attr(755,root,root) %{_libdir}/tracker/filters/application/vnd.sun.xml.draw_filter
%attr(755,root,root) %{_libdir}/tracker/filters/application/vnd.sun.xml.impress.template_filter
%attr(755,root,root) %{_libdir}/tracker/filters/application/vnd.sun.xml.impress_filter
%attr(755,root,root) %{_libdir}/tracker/filters/application/vnd.sun.xml.writer.template_filter
%attr(755,root,root) %{_libdir}/tracker/filters/application/vnd.sun.xml.writer_filter
%attr(755,root,root) %{_libdir}/tracker/filters/application/x-abiword_filter
%attr(755,root,root) %{_libdir}/tracker/filters/application/x-gnumeric_filter
%dir %{_libdir}/tracker/filters/text
%attr(755,root,root) %{_libdir}/tracker/filters/text/csv_filter
%attr(755,root,root) %{_libdir}/tracker/filters/text/djvu_filter
%attr(755,root,root) %{_libdir}/tracker/filters/text/html_filter
%attr(755,root,root) %{_libdir}/tracker/filters/text/spreadsheet_filter
%attr(755,root,root) %{_libdir}/tracker/filters/text/tab-separated-values_filter
%attr(755,root,root) %{_libdir}/tracker/filters/text/x-comma-separated-values_filter
%attr(755,root,root) %{_libdir}/tracker/filters/text/x-tex_filter
%attr(755,root,root) %{_libdir}/tracker/filters/text/xml_filter
%dir %{_libdir}/tracker/thumbnailers
%dir %{_libdir}/tracker/thumbnailers/application
%attr(755,root,root) %{_libdir}/tracker/thumbnailers/application/pdf_thumbnailer
%attr(755,root,root) %{_libdir}/tracker/thumbnailers/application/vnd.oasis.opendocument.graphics_thumbnailer
%attr(755,root,root) %{_libdir}/tracker/thumbnailers/application/vnd.oasis.opendocument.presentation_thumbnailer
%attr(755,root,root) %{_libdir}/tracker/thumbnailers/application/vnd.oasis.opendocument.spreadsheet_thumbnailer
%attr(755,root,root) %{_libdir}/tracker/thumbnailers/application/vnd.oasis.opendocument.text_thumbnailer
%dir %{_libdir}/tracker/thumbnailers/image
%attr(755,root,root) %{_libdir}/tracker/thumbnailers/image/gif_thumbnailer
%attr(755,root,root) %{_libdir}/tracker/thumbnailers/image/jpeg_thumbnailer
%attr(755,root,root) %{_libdir}/tracker/thumbnailers/image/png_thumbnailer
%attr(755,root,root) %{_libdir}/tracker/thumbnailers/image/tiff_thumbnailer
%{_datadir}/dbus-1/services/tracker.service
%dir %{_datadir}/tracker
%dir %{_datadir}/tracker/languages
%{_datadir}/tracker/languages/stopwords.da
%{_datadir}/tracker/languages/stopwords.de
%{_datadir}/tracker/languages/stopwords.en
%{_datadir}/tracker/languages/stopwords.es
%{_datadir}/tracker/languages/stopwords.fi
%{_datadir}/tracker/languages/stopwords.fr
%{_datadir}/tracker/languages/stopwords.it
%{_datadir}/tracker/languages/stopwords.nb
%{_datadir}/tracker/languages/stopwords.nl
%{_datadir}/tracker/languages/stopwords.pt
%{_datadir}/tracker/languages/stopwords.ru
%{_datadir}/tracker/languages/stopwords.sv
%dir %{_datadir}/tracker/services
%{_datadir}/tracker/services/application.metadata
%{_datadir}/tracker/services/audio.metadata
%{_datadir}/tracker/services/default.metadata
%{_datadir}/tracker/services/default.service
%{_datadir}/tracker/services/document.metadata
%{_datadir}/tracker/services/email.metadata
%{_datadir}/tracker/services/file.metadata
%{_datadir}/tracker/services/image.metadata
%{_datadir}/tracker/services/video.metadata
%{_datadir}/tracker/sqlite-cache.sql
%{_datadir}/tracker/sqlite-email.sql
%{_datadir}/tracker/sqlite-metadata.sql
%{_datadir}/tracker/sqlite-service-stored-procs.sql
%{_datadir}/tracker/sqlite-service-triggers.sql
%{_datadir}/tracker/sqlite-service-types.sql
%{_datadir}/tracker/sqlite-service.sql
%{_datadir}/tracker/sqlite-stored-procs.sql
%{_datadir}/tracker/sqlite-tracker-triggers.sql
%{_datadir}/tracker/sqlite-tracker.sql
%{_datadir}/tracker/sqlite-user-data.sql
%{_datadir}/tracker/tracker-introspect.xml
%{_mandir}/man1/tracker-extract.1*
%{_mandir}/man1/tracker-files.1*
%{_mandir}/man1/tracker-meta-folder.1*
%{_mandir}/man1/tracker-query.1*
%{_mandir}/man1/tracker-search.1*
%{_mandir}/man1/tracker-stats.1*
%{_mandir}/man1/tracker-status.1*
%{_mandir}/man1/tracker-tag.1*
%{_mandir}/man1/tracker-thumbnailer.1*
%{_mandir}/man1/trackerd.1*
%{_mandir}/man5/tracker.cfg.5*
%{_mandir}/man7/tracker-services.7*

%if %{with gui}
%files search-gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tracker-applet
%attr(755,root,root) %{_bindir}/tracker-preferences
%attr(755,root,root) %{_bindir}/tracker-search-tool
%{_datadir}/tracker/icons
%{_datadir}/tracker/tracker-applet-prefs.glade
%{_datadir}/tracker/tracker-preferences.glade
%{_desktopdir}/tracker-preferences.desktop
%{_desktopdir}/tracker-search-tool.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_mandir}/man1/tracker-applet.1*
%{_mandir}/man1/tracker-preferences.1*
%{_mandir}/man1/tracker-search-tool.1*
%{_sysconfdir}/xdg/autostart/tracker-applet.desktop
%endif

%files startup
%defattr(644,root,root,755)
%{_sysconfdir}/xdg/autostart/trackerd.desktop

%if %{with deskbar_applet}
%files -n gnome-applet-deskbar-extension-tracker
%defattr(644,root,root,755)
%{_libdir}/deskbar-applet/modules-2.20-compatible/tracker-module.py[co]
%endif

%files -n libtracker
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtrackerclient.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtrackerclient.so.0

%files -n libtracker-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtrackerclient.so
%{_libdir}/libtrackerclient.la
%{_includedir}/tracker-client.h
%{_includedir}/tracker.h
%{_pkgconfigdir}/tracker.pc

%files -n libtracker-static
%defattr(644,root,root,755)
%{_libdir}/libtrackerclient.a

%if %{with gui}
%files -n libtracker-gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtracker-gtk.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtracker-gtk.so.0
%endif

%if %{with gui}
%files -n libtracker-gtk-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtracker-gtk.so
%{_libdir}/libtracker-gtk.la
%{_includedir}/libtracker-gtk
%{_pkgconfigdir}/libtracker-gtk.pc
%endif

%if %{with gui}
%files -n libtracker-gtk-static
%defattr(644,root,root,755)
%{_libdir}/libtracker-gtk.a
%endif
