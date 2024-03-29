%define  debug_package %{nil}

Name:		formatUSB
Version:	1.0.6
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
* Sun Aug 14 2022 David King <dave@daveking.com> - 1.0.6-1
        Fix error with partition start specification
* Sat Aug 13 2022 David King <dave@daveking.com> - 1.0.5-1
        - Switch to exfat filesystem for both large and small disks
        - Use sfdisk for partitioning instead of parted
* Fri Aug 12 2022 David King <dave@daveking.com> - 1.0.4-1
	Prompt to format disks larger than the 2TB MSDOS partition size limit
        with either GPT or MSDOS partition table
* Wed Aug 10 2022 David King <dave@daveking.com> - 1.0.3-1
	Handle disks larger than the 2TB MSDOS partition size limit
* Tue Mar 10 2020 David King <dave@daveking.com> - 1.0.1-1
	Fix device name in mounted check section
* Thu Mar 5 2020 David King <dave@daveking.com> - 1.0.0-1
	Initial Version
