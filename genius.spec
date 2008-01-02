%define version 0.7.6.1
%define release %mkrel 1

Summary:	A general purpose calculator and math tool
Name:		genius
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Sciences/Mathematics
URL:		http://www.jirka.org/genius.html
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

Source:		http://ftp.5z.com/pub/%{name}/%{name}-%{version}.tar.bz2
Patch0:		%{name}-0.5.5-plugin-libtool-flag.patch.bz2

BuildRequires:	vte-devel
BuildRequires:	libgnomeui2-devel
BuildRequires:	libglade2.0-devel
BuildRequires:	gtksourceview-devel
BuildRequires:	gmp-devel
BuildRequires:	readline-devel
BuildRequires:	termcap-devel
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	scrollkeeper
# the following stuffs are not necessary if not regenerating auto* stuff
BuildRequires:	intltool
BuildRequires:	automake1.8
BuildRequires:	gnome-common
Requires(post): shared-mime-info
Requires(postun): shared-mime-info
Requires(post): scrollkeeper
Requires(postun): scrollkeeper
Requires:	ghostscript

%description
Genius is an advanced calculator and a mathematical programming language.
It handles multiple precision floating point numbers, infinite precision
integers, complex numbers and matrixes.


%prep
%setup -q
%patch0 -p1 -b .no-version

# needed by patch0
autoreconf --force --install

%build
%configure2_5x --enable-mpfr 
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat > $RPM_BUILD_ROOT%{_menudir}/%{name} <<_EOF_
?package(%{name}): \
command="%{_bindir}/genius" \
icon="mathematics_section.png" \
longtitle="Genius Mathematical Tool and Calculator" \
needs="x11" \
section="More Applications/Sciences/Mathematics" \
title="Genius math tool" \
startup_notify="yes" \
xdg="true"
_EOF_

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --remove-category="Scientific" \
  --add-category="X-MandrivaLinux-MoreApplications-Sciences-Mathematics" \
  --add-category="Science" \
  --add-category="Math" \
  --remove-key="Mime-Type" \
  --add-mime-type="text/x-genius" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*


%{find_lang} %{name} --with-gnome

# remove stuff not distributed
# pointless to include header, no plugin has been developed in 4 yrs
rm -rf $RPM_BUILD_ROOT%{_includedir}
rm -f $RPM_BUILD_ROOT%{_libdir}/genius/*.a \
      $RPM_BUILD_ROOT%{_libdir}/genius/*.la

rm -rf %{buildroot}/%{_datadir}/mime/{XMLnamespaces,globs,magic,text,subclasses,aliases,mime.cache}  %{buildroot}/var/lib/scrollkeeper

%post
%update_menus
%update_mime_database
%update_desktop_database
%update_scrollkeeper
%update_icon_cache hicolor

%postun
%clean_menus
%clean_mime_database
%clean_desktop_database
%clean_scrollkeeper
%clean_icon_cache hicolor

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}
%{_datadir}/application-registry/*
%{_datadir}/mime/packages/*
%{_datadir}/mime-info/*
%{_datadir}/omf/*
%{_iconsdir}/hicolor/*/apps/gnome-genius.png
%{_libdir}/%{name}
%{_libexecdir}/genius-readline-helper-fifo
%{_menudir}/%{name}
%{_datadir}/applications/*

