Name:           gocryptfs
Version:        %{version}
Release:        1%{?dist}
Summary:        Encrypted overlay filesystem written in Go
License:        MIT
URL:            https://nuetzlich.net/gocryptfs/
Source0:        https://github.com/rfjakob/gocryptfs/releases/download/v%{version}/gocryptfs_v%{version}_linux-static_amd64.tar.gz

%description
gocryptfs uses file-based encryption that is implemented as a mountable FUSE
filesystem. Each file in gocryptfs is stored one corresponding encrypted files
on the hard disk.

%prep
%setup -c %{name}-%{version}

%install
install -D -m 0755 ./gocryptfs %{buildroot}%{_bindir}/gocryptfs
install -D -m 0644 ./gocryptfs.1 %{buildroot}%{_mandir}/man1/gocryptfs.1

%files
%{_bindir}/gocryptfs
%{_mandir}/man1/*

%changelog
* Sun Feb 25 2018 Dawid Zych <dawid.zych@yandex.com> - 1.4.3-1
- Update to 1.4.3
* Fri Jul 14 2017 Dawid Zych <dawid.zych@yandex.com> - 1.4-1
- Update to 1.4
* Fri Apr 21 2017 Dawid Zych <dawid.zych@yandex.com> - 1.2.1-1
- Update to 1.2.1
* Tue Jan 03 2017 Dawid Zych <dawid.zych@yandex.com> - 1.2-1
- Initial packaging.
