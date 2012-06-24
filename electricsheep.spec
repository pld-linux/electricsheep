Summary:	Collaborative screensaver
Summary(pl):	Wygaszacz ekranu wsp�pracuj�cych komputer�w
Name:		electricsheep
Version:	2.6.4
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://electricsheep.org/%{name}-%{version}.tar.gz
# Source0-md5:	59834e2b6a13280e9e6313533c7ff6cf
Patch0:		%{name}-destdir.patch
URL:		http://electricsheep.org/
BuildRequires:	SDL-devel
BuildRequires:	XFree86-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	expat-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
Requires:	curl
Requires:	xloadimage
Requires:	xscreensaver
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Electric Sheep is a screensaver that realizes the collective dream of
sleeping computers from all over the Internet. It's an xscreensaver
module that displays MPEG video of an animated fractal flame. In the
background it contributes render cycles to the future animations.
Periodically it uploades completed frames to the server, where they
are compressed for distribution to all clients.

%description -l pl
Electric Sheep (Elektryczna owca) jest wygaszaczem ekranu realizuj�cym
wsp�lny sen u�pionych komputer�w w ca�ym Internecie. Jest to modu�
xscreensavera wy�wietlaj�cy animowacj� fraktalnego p�omienie w
formacie MPEG. W tle tworzone s� elementy przysz�ych animacji. Po
uko�czeniu s� one co jaki� czas zapisywane na serwerze, gdzie s�
kompresowane w celu udost�pnienia wszystkim klientom.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{_bindir},%{_datadir}/control-center/screensavers}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.png
%{_datadir}/control-center/screensavers/electricsheep.xml
%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT
