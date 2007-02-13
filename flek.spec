Summary:	High level cross-platform "environment" libraries based on Fltk
Summary(pl.UTF-8):	Wysykopoziomowe międzyplatformowe biblioteki "środowiskowe" bazujące na Fltk
Name:		flek
Version:	0.2
Release:	4
License:	GPL
Group:		X11/Libraries
Source0:	ftp://flek.sourceforge.net/pub/flek/%{name}-%{version}.agenda.tar.gz
# Source0-md5:	16ead4da819c0154f084a000b5ee19bf
Patch0:		%{name}-DESTDIR.patch
URL:		http://flek.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fltk-devel >= 1.0.11-3
BuildRequires:	libjpeg-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Flek hopes to provide the same layer of functionality for Fltk that
GNOME and KDE do for the GTK+ and Qt toolkits, respectively.
Applications written with Flek should work cooperatively with
applications written in either GNOME or KDE. Flek does not necessarily
intend to become a self contained desktop environment and we don't
plan on duplicating the work of either GNOME or KDE in this regard.
Aren't there enough IRC clients? ;-)

%description -l pl.UTF-8
Flek ma zapewnić ten sam poziom funkcjonalności dla Fltk, co GNOME i
KDE dla GTK+ i Qt. Aplikacje korzystające z Fleka powinny
współpracować z aplikacjami pisanymi dla GNOME lub KDE. Flek nie ma
koniecznie zostać samodzielnym środowiskiem desktopu i nie jest
planowane, by powielał pracę GNOME lub KDE w tym zakresie.

%package devel
Summary:	Flek header files and development documentation
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja programisty Fleka
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Flek header files and development documentation.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja programisty Fleka.

%package static
Summary:	Flek static libraries
Summary(pl.UTF-8):	Biblioteki statyczne Fleka
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Flek static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne Fleka.

%prep
%setup  -q -n %{name}-%{version}.agenda
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
cp -f /usr/share/automake/config.* .
%configure \
	--with-fltk=%{_prefix}
%{__make} src

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README Changelog
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%doc docs
%{_includedir}/Flek
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
