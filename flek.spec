Summary:	High level cross-platform "environment" libraries based on Fltk
Name:		flek
Version:	0.2
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	ftp://flek.sourceforge.net/pub/%{name}/%{name}-%{version}.agenda.tar.gz
URL:	http://flek.sourceforge.net
BuildRequires:	fltk-devel >= 1.0.11-3
BuildRequires:	libjpeg-devel
BuildRequires:	OpenGL-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define _prefix /usr/X11R6

%description
Flek hopes to provide the same layer of functionality for Fltk that Gnome
and KDE do for the Gtk and Qt toolkits, respectively. Applications written
with Flek should work cooperatively with applications written in either
Gnome or KDE. Flek does not necessarily intend to become a self contained
desktop environment and we don't plan on duplicating the work of either
Gnome or KDE in this regard. Aren't there enough IRC clients? ;-)

%prep
%setup  -q -n %{name}-%{version}.agenda

%build
%configure2_13 \
    --with-fltk=%{_prefix}

%{__make} src

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
