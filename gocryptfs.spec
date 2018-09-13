Name:           gocryptfs
Version:        1.6
Release:        1%{?dist}
Summary:        Encrypted overlay filesystem written in Go
License:        MIT
URL:            https://nuetzlich.net/gocryptfs/
Source0:        https://github.com/sbstnkhlr/gocryptfs/

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
