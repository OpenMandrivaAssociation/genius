%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	A general purpose calculator and math tool
Name:		genius
Version:	1.0.17
Release:	2
License:	GPLv3+
Group:		Sciences/Mathematics
URL:		http://www.jirka.org/genius.html
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	intltool
BuildRequires:	rarian
BuildRequires:	gmp-devel
BuildRequires:	mpfr-devel
BuildRequires:	readline-devel
BuildRequires:	termcap-devel
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtksourceview-2.0)
BuildRequires:	pkgconfig(vte)

Requires:	ghostscript

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
%configure2_5x \
	--enable-mpfr \
	--disable-scrollkeeper \
	--disable-update-mimedb \
	--disable-static
%make

%install
%makeinstall_std

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
%{_libdir}/%{name}
%{_libexecdir}/genius-readline-helper-fifo

%files devel
%{_includedir}/*


