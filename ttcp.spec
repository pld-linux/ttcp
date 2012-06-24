Summary:	Network bandwidth measurement tool
Summary(pl):	Narz�dzie do monitorowania przepustowo�ci sieci
Name:		ttcp
Version:	1.12
Release:	2
License:	Public Domain
Group:		Networking
# original sources at http://ftp.arl.mil/ftp/pub/ttcp/, maybe modified here?
Source0:	%{name}.tar.gz
# Source0-md5:	698b5e97417d7552a6f881c0e7d4ff5d
URL:		http://ftp.arl.mil/~mike/ttcp.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TTCP is a benchmarking tool for determining TCP and UDP performance
between 2 systems.

%description -l pl
TTCP jest narz�dziem sprawdzaj�cym wydajno�� po��cze� TCP i UDP
pomi�dzy dwoma systemami.

%prep
%setup -q -n %{name}

%build
%{__make} ttcp \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install ttcp $RPM_BUILD_ROOT%{_bindir}
install ttcp.1 $RPM_BUILD_ROOT%{_mandir}/man1


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
