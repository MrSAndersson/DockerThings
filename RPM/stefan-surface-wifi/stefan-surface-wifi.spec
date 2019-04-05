Name: stefan-surface-wifi
Version: 1
Release: 1%{?dist}
Summary: Fix for broken Surface Go wifi

License: Public Domain
Source0: board.bin
BuildArch: noarch

%description
A small fix for the Surface Go wifi driver

%install
mkdir -p %{buildroot}/%{_bindir}
install -p -m 755 %{SOURCE0} %{buildroot}/%{_bindir}

%files
%{_bindir}/board.bin

%changelog