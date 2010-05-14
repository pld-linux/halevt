Summary:	Halevt is a daemon that commands when a device added to your system
Summary(hu.UTF-8):	Halevt egy démon, amely egy parancsot hajt végre, ha egy eszközt csatlakoztatsz a gépedhez
Name:		halevt
Version:	0.1.6.1
Release:	0.4
License:	GPL v2
Group:		Applications
Source0:	http://savannah.nongnu.org/download/halevt/%{name}-%{version}.tar.gz
# Source0-md5:	005f0c8969b0f86d261d85ea03062fde
URL:		http://www.nongnu.org/halevt/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	boolstuff-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	gettext-devel
BuildRequires:	hal-devel
BuildRequires:	man2html
BuildRequires:	pkgconfig
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	__cxx

%description
Halevt is a daemon that commands when a device added to your system.

%description -l pl.UTF-8
Halevt egy démon, amely egy parancsot hajt végre, ha egy eszközt
csatlakoztatsz a gépedhez.

%prep
%setup -q

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp examples/*.xml $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

rm -rf $RPM_BUILD_ROOT%{_infodir}/dir

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
# maybe create a config file?
%dir %{_sysconfdir}/%{name}
%attr(755,root,root) %{_bindir}/*
%doc AUTHORS ChangeLog NEWS README TODO
%{_mandir}/man1/*.1*
%{_infodir}/%{name}.info.*
%{_examplesdir}/%{name}-%{version}
