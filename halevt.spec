Summary:	Halevt is a daemon that commands when a device added to your system
Summary(hu.UTF-8):	Halevt egy démon, amely egy parancsot hajt végre, ha egy eszközt csatlakoztatsz a gépedhez
Name:		halevt
Version:	0.1.6.1
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://savannah.nongnu.org/download/halevt/%{name}-%{version}.tar.gz
# Source0-md5:	005f0c8969b0f86d261d85ea03062fde
URL:		http://www.nongnu.org/halevt/
BuildRequires:	boolstuff-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl.UTF-8

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
