Summary:	High level cross-platform "environment" libraries based on Fltk
Name:		flek
Version:	0.2
Release:	1
License:	GPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/Библиотеки
Group(uk):	X11/Б╕бл╕отеки
Source0:	ftp://flek.sourceforge.net/pub/%{name}/%{name}-%{version}.agenda.tar.gz
URL:		http://flek.sourceforge.net
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

%package devel
Summary:	Flek header files and development documentation
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Разработка/Библиотеки
Group(uk):	X11/Розробка/Б╕бл╕отеки
Requires:	%{name} = %{version}

%description devel
Flek header files and development documentation.

%package static
Summary:	Flek static libraries
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Разработка/Библиотеки
Group(uk):	X11/Розробка/Б╕бл╕отеки
Requires:	%{name} = %{version}

%description static
Flek static libraries.

%prep
%setup  -q -n %{name}-%{version}.agenda

%build
aclocal
autoconf
%configure --with-fltk=%{_prefix}

%{__make} src

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	includedir=$RPM_BUILD_ROOT%{_includedir} \
	bindir=$RPM_BUILD_ROOT%{_bindir}

symlinks -cs $RPM_BUILD_ROOT%{_libdir}

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
