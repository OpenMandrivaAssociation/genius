%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	A general purpose calculator and math tool
Name:		genius
Version:	1.0.27
Release:	1
License:	GPLv3+
Group:		Sciences/Mathematics
URL:		http://www.jirka.org/genius.html
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	intltool
BuildRequires:	pkgconfig(amtk-5)
BuildRequires:	pkgconfig(glib-2.0) >= 2.12.0
BuildRequires:	pkgconfig(gmodule-2.0) >= 2.12.0
BuildRequires:	pkgconfig(gio-2.0) >= 2.16.0
BuildRequires:	pkgconfig(gtk+-3.0) >= 2.18.0
BuildRequires:	pkgconfig(vte-2.91)
BuildRequires:	pkgconfig(gtksourceview-4)
BuildRequires:	gmp-devel
BuildRequires:	pkgconfig(readline)
BuildRequires:	pkgconfig(mpfr)
#BuildRequires:	pkgconfig(tinfo)
BuildRequires:	automake
Requires:	ghostscript
Requires:	gtk-update-icon-cache


%description
Genius is an advanced calculator and a mathematical programming language.
It handles multiple precision floating point numbers, infinite precision
integers, complex numbers and matrixes.

%package devel
Summary:	Files to develop genius plugins
Requires:	%{name} = %{version}

%description devel
Genius is an advanced calculator and a mathematical programming language.
It handles multiple precision floating point numbers, infinite precision
integers, complex numbers and matrixes.

This package contains developmend files and not required for runnind genius.

%prep
%setup -q
%autopatch -p1

%build
%configure \
	--enable-mpfr \
	--disable-scrollkeeper \
	--disable-update-mimedb \
	--disable-static
%make_build

%install
%make_install

%{find_lang} %{name} --with-gnome

%files -f %{name}.lang
%doc AUTHORS NEWS README
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}
%{_datadir}/application-registry/*
%{_datadir}/mime/packages/*
%{_datadir}/mime-info/*
%{_iconsdir}/hicolor/*/apps/gnome-genius.png
%{_iconsdir}/hicolor/*/apps/genius-stock-plot.png
%{_iconsdir}/hicolor/scalable/apps/gnome-genius.svg
%{_libdir}/%{name}
%{_libexecdir}/genius-readline-helper-fifo

%files devel
%{_includedir}/*


