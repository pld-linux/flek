Summary:	High level cross-platform "environment" libraries based on Fltk
Summary(pl):	Wysykopoziomowe miêdzyplatformowe biblioteki "¶rodowiskowe" bazuj±ce na Fltk
Name:		flek
Version:	0.2
Release:	2
License:	GPL
Group:		X11/Libraries
Source0:	ftp://flek.sourceforge.net/pub/%{name}/%{name}-%{version}.agenda.tar.gz
Patch0:		%{name}-DESTDIR.patch
URL:		http://flek.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fltk-devel >= 1.0.11-3
BuildRequires:	libjpeg-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Flek hopes to provide the same layer of functionality for Fltk that
Gnome and KDE do for the Gtk and Qt toolkits, respectively.
Applications written with Flek should work cooperatively with
applications written in either Gnome or KDE. Flek does not necessarily
intend to become a self contained desktop environment and we don't
plan on duplicating the work of either Gnome or KDE in this regard.
Aren't there enough IRC clients? ;-)

%description -l pl
Flek ma zapewniæ ten sam poziom funkcjonalno¶ci dla Fltk, co GNOME i
KDE dla Gtk i Qt. Aplikacje korzystaj±ce z Fleka powinny wspó³pracowaæ
z aplikacjami pisanymi dla GNOME lub KDE. Flek nie ma koniecznie
zostaæ samodzielnym ¶rodowiskiem desktopu i nie jest planowane, by
powiela³ pracê GNOME lub KDE w tym zakresie.

%package devel
Summary:	Flek header files and development documentation
Summary(pl):	Pliki nag³ówkowe i dokumentacja programisty Fleka
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Flek header files and development documentation.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja programisty Fleka.

%package static
Summary:	Flek static libraries
Summary(pl):	Biblioteki statyczne Fleka
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Flek static libraries.

%description static -l pl
Biblioteki statyczne Fleka.

%prep
%setup  -q -n %{name}-%{version}.agenda
%patch0 -p1

%build
aclocal
autoconf
%configure \
	--with-fltk=%{_prefix}
%{__make} src

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README Changelog

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz
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
