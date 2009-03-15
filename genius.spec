%define version 1.0.6
%define release %mkrel 1

Summary:	A general purpose calculator and math tool
Name:		genius
Version:	%{version}
Release:	%{release}
License:	GPLv3+
Group:		Sciences/Mathematics
URL:		http://www.jirka.org/genius.html
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

Source:		http://ftp.5z.com/pub/%{name}/%{name}-%{version}.tar.bz2

BuildRequires:	vte-devel
BuildRequires:	libgnomeui2-devel
BuildRequires:	libglade2.0-devel
BuildRequires:	libgtksourceview-2.0-devel
BuildRequires:	gmp-devel
BuildRequires:	readline-devel
BuildRequires:	mpfr-devel
BuildRequires:	termcap-devel
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	scrollkeeper
# the following stuffs are not necessary if not regenerating auto* stuff
BuildRequires:	intltool
BuildRequires:	automake
Requires:	ghostscript

%description
Genius is an advanced calculator and a mathematical programming language.
It handles multiple precision floating point numbers, infinite precision
integers, complex numbers and matrixes.


%prep
%setup -q

%build
%configure2_5x --enable-mpfr --disable-scrollkeeper --disable-update-mimedb 
make

%install
rm -rf %{buildroot}
%makeinstall_std

%{find_lang} %{name} --with-gnome

# remove stuff not distributed
# pointless to include header, no plugin has been developed in 4 yrs
rm -rf %{buildroot}%{_includedir}
rm -f %{buildroot}%{_libdir}/genius/*.a \
      %{buildroot}%{_libdir}/genius/*.la

%if %mdkversion < 200900
%post
%update_menus
%update_mime_database
%update_desktop_database
%update_scrollkeeper
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%clean_mime_database
%clean_desktop_database
%clean_scrollkeeper
%clean_icon_cache hicolor
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS NEWS README
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}
%{_datadir}/application-registry/*
%{_datadir}/mime/packages/*
%{_datadir}/mime-info/*
%{_datadir}/omf/*
%{_iconsdir}/hicolor/*/apps/gnome-genius.png
%{_iconsdir}/hicolor/*/apps/genius-stock-plot.png
%{_libdir}/%{name}
%{_libexecdir}/genius-readline-helper-fifo
