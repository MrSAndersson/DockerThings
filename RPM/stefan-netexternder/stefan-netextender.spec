Name: stefan-netextender
Version: 8.6.801
Release: 1%{?dist}
Summary: Dell netExtender VPN Client

License: Proprietary
Source0: NetExtender.x86_64.tgz
BuildArch: x86_64
Requires: net-tools

%description
A srepackage of Dell netExtender into an RPM for ease of automatic install

%prep
tar xf NetExtender.x86_64.tgz

%install

mkdir -p %{buildroot}/usr/lib/firmware/ath10k/QCA6174
install -p -m 644 %{SOURCE0} %{buildroot}/usr/lib/firmware/ath10k/QCA6174

%post

%preun
if [ -f /usr/lib/firmware/ath10k/QCA6174/hw2.1/board-2.bin ]; then
    mv /usr/lib/firmware/ath10k/QCA6174/hw2.1/board.bin /usr/lib/firmware/ath10k/QCA6174/hw2.1/board.bin.old
    mv /usr/lib/firmware/ath10k/QCA6174/hw3.0/board.bin /usr/lib/firmware/ath10k/QCA6174/hw3.0/board.bin.old
fi

%files
/usr/lib/firmware/ath10k/QCA6174/board.bin

%postun
mv /usr/lib/firmware/ath10k/QCA6174/hw2.1/board.bin.old /usr/lib/firmware/ath10k/QCA6174/hw2.1/board.bin
mv /usr/lib/firmware/ath10k/QCA6174/hw3.0/board.bin.old /usr/lib/firmware/ath10k/QCA6174/hw3.0/board.bin

if [ -f /usr/lib/firmware/ath10k/QCA6174/hw2.1/board-2.bin ]; then
    rm /usr/lib/firmware/ath10k/QCA6174/hw2.1/board-2.bin.old
    rm /usr/lib/firmware/ath10k/QCA6174/hw3.0/board-2.bin.old
else
    mv /usr/lib/firmware/ath10k/QCA6174/hw2.1/board-2.bin.old /usr/lib/firmware/ath10k/QCA6174/hw2.1/board-2.bin
    mv /usr/lib/firmware/ath10k/QCA6174/hw3.0/board-2.bin.old /usr/lib/firmware/ath10k/QCA6174/hw3.0/board-2.bin
fi

%changelog