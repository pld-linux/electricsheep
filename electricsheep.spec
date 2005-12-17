Summary:	collaborative screensaver
Name:		electricsheep
Version:	2.6.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://electricsheep.org/%{name}-%{version}.tar.gz
# Source0-md5:	59834e2b6a13280e9e6313533c7ff6cf
Patch0:	%{name}-destdir.patch
URL:		http://electricsheep.org
BuildRequires: automake
BuildRequires: autoconf
Requires:	xloadimage
Requires:	xscreensaver
Requires:	expat
Requires:	curl
BuildRoot: /tmp/%{name}-%{version}-root-%(id -u -n)

%description

Electric Sheep is a screensaver that realizes the collective dream of
sleeping computers from all over the internet. It's an xscreensaver
module that displays mpeg video of an animated fractal flame. In the
background it contributes render cycles to the future animations.
Periodically it uploades completed frames to the server, where they
are compressed for distribution to all clients.

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
%{_datadir}/%{name}/*.png
%{_datadir}/control-center/screensavers/electricsheep.xml
%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT
