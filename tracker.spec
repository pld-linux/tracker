#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs
%bcond_with	icu		# libicu instead of libunistring
%bcond_with	static_libs	# static libraries
%bcond_without	vala		# Vala API

%define		ver	2.0
Summary:	Tracker - an indexing subsystem
Summary(pl.UTF-8):	Tracker - podsystem indeksujący
Name:		tracker
Version:	2.0.4
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/tracker/2.0/%{name}-%{version}.tar.xz
# Source0-md5:	ad1b14754828db76f3aeb47c9d03bb0a
Patch0:		link.patch
Patch1:		%{name}-docs.patch
URL:		http://projects.gnome.org/tracker/
BuildRequires:	NetworkManager-devel >= 0.8.0
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.11
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.44.0
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	graphviz
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	intltool >= 0.40.0
BuildRequires:	json-glib-devel >= 1.0
%{?with_icu:BuildRequires:	libicu-devel >= 4.8.1.1}
BuildRequires:	libsoup-devel >= 2.40
BuildRequires:	libstemmer-devel
BuildRequires:	libtool >= 2:2.2
%{!?with_icu:BuildRequires:	libunistring-devel}
BuildRequires:	libuuid-devel
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.6
BuildRequires:	rpmbuild(macros) >= 1.673
BuildRequires:	sqlite3-devel >= 3.21.0-2
BuildRequires:	tar >= 1:1.22
BuildRequires:	upower-devel >= 0.9.0
%{?with_vala:BuildRequires:	vala >= 2:0.18.0}
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires(post,postun):	glib2 >= 1:2.44.0
Requires:	%{name}-libs = %{version}-%{release}
Requires:	dbus >= 1.3.1
Requires:	libxml2 >= 1:2.6.31
Requires:	upower-libs >= 0.9.0
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
Requires:	glib2 >= 1:2.44.0
Requires:	json-glib >= 1.0
Requires:	libsoup >= 2.40
Requires:	sqlite3 >= 3.21.0-2
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
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static} \
	--disable-unit-tests \
	--with-html-dir=%{_gtkdocdir} \
	--with-unicode-support=%{?with_icu:libicu}%{!?with_icu:libunistring}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/tracker-%{ver}/*.la
%if %{with static_libs}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/tracker-%{ver}/libtracker-*.a
%endif


%find_lang tracker

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f tracker.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tracker
%attr(755,root,root) %{_libdir}/tracker-store
%{_sysconfdir}/xdg/autostart/tracker-store.desktop
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.service
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker.DB.gschema.xml
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker.FTS.gschema.xml
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker.Store.gschema.xml
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker.enums.xml
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker.gschema.xml
%{_datadir}/tracker
%{systemduserunitdir}/tracker-store.service
%{_mandir}/man1/tracker-daemon.1*
%{_mandir}/man1/tracker-index.1*
%{_mandir}/man1/tracker-info.1*
%{_mandir}/man1/tracker-reset.1*
%{_mandir}/man1/tracker-search.1*
%{_mandir}/man1/tracker-sparql.1*
%{_mandir}/man1/tracker-sql.1*
%{_mandir}/man1/tracker-status.1*
%{_mandir}/man1/tracker-store.1*
%{_mandir}/man1/tracker-tag.1*

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
