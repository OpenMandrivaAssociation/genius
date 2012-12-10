Summary:	A general purpose calculator and math tool
Name:		genius
Version:	1.0.15
Release:	2
License:	GPLv3+
Group:		Sciences/Mathematics
URL:		http://www.jirka.org/genius.html

Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.xz

BuildRequires:	vte-devel
BuildRequires:	gtk+2-devel
BuildRequires:	pkgconfig(gtksourceview-2.0)
BuildRequires:	gmp-devel
BuildRequires:	readline-devel
BuildRequires:	mpfr-devel
BuildRequires:	termcap-devel
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	scrollkeeper
BuildRequires:	pkgconfig(gnome-doc-utils)
# the following stuffs are not necessary if not regenerating auto* stuff
BuildRequires:	intltool
BuildRequires:	automake
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
%apply_patches

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
