%define  debug_package %{nil}

Name:		formatUSB
Version:	1.0.1
Release:	1%{?dist}
Summary:	Format Removable Media
Source0:	%{name}-%{version}.tar.gz
License:	MPL
URL:		https://github.com/dlk3/formatUSB
BuildArch:	noarch

%description
A command line script to format removable media, optionally with LUKS-based encryption.

%prep
%setup

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 -t %{buildroot}%{_bindir} formatUSB

%files
%license LICENSE
%{_bindir}/formatUSB

%changelog
* Tue Mar 10 2020 David King <dave@daveking.com> - 1.0.1-1
	Fix device name in mounted check section
* Thu Mar 5 2020 David King <dave@daveking.com> - 1.0.0-1
	Initial Version
