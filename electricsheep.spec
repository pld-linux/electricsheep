Summary:	Collaborative screensaver
Summary(pl):	Wygaszacz ekranu wspó³pracuj±cych komputerów
Name:		electricsheep
Version:	2.6.8
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://electricsheep.org/%{name}-%{version}.tar.gz
# Source0-md5:	5c3535a7c679d67d460c1d9e259a5d38
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
Electric Sheep (Elektryczna owca) jest wygaszaczem ekranu realizuj±cym
wspólny sen u¶pionych komputerów w ca³ym Internecie. Jest to modu³
xscreensavera wy¶wietlaj±cy animacjê fraktalnego p³omienia w formacie
MPEG. W tle tworzone s± elementy przysz³ych animacji. Po ukoñczeniu s±
one co jaki¶ czas zapisywane na serwerze, gdzie s± kompresowane w celu
udostêpnienia wszystkim klientom.

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
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/xscreensaver}

%{__make} install \
	SCREENSAVER_DATADIR=%{_datadir}/xscreensaver \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.png
%{_datadir}/xscreensaver/*.xml
%{_mandir}/man1/*
