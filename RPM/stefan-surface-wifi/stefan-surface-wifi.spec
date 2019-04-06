Name: stefan-surface-wifi
Version: 1
Release: 1%{?dist}
Summary: Fix for broken Surface Go wifi

License: Public Domain
Source0: board.bin
BuildArch: noarch

%description
A small fix for the Surface Go wifi driver

%pre
mv /usr/lib/firmware/ath10k/QCA6174/hw2.1/board.bin /usr/lib/firmware/ath10k/QCA6174/hw2.1/board.bin.old
mv /usr/lib/firmware/ath10k/QCA6174/hw3.0/board.bin /usr/lib/firmware/ath10k/QCA6174/hw3.0/board.bin.old

mv /usr/lib/firmware/ath10k/QCA6174/hw2.1/board-2.bin /usr/lib/firmware/ath10k/QCA6174/hw2.1/board-2.bin.old
mv /usr/lib/firmware/ath10k/QCA6174/hw3.0/board-2.bin /usr/lib/firmware/ath10k/QCA6174/hw3.0/board-2.bin.old

%install
mkdir -p %{buildroot}/usr/lib/firmware/ath10k/QCA6174/hw2.1
install -p -m 644 %{SOURCE0} %{buildroot}/usr/lib/firmware/ath10k/QCA6174/hw2.1
mkdir -p %{buildroot}/usr/lib/firmware/ath10k/QCA6174/hw3.0
install -p -m 644 %{SOURCE0} %{buildroot}/usr/lib/firmware/ath10k/QCA6174/hw3.0

%preun
if [ -f /usr/lib/firmware/ath10k/QCA6174/hw2.1/board-2.bin ]; then
    mv /usr/lib/firmware/ath10k/QCA6174/hw2.1/board.bin /usr/lib/firmware/ath10k/QCA6174/hw2.1/board.bin.old
    mv /usr/lib/firmware/ath10k/QCA6174/hw3.0/board.bin /usr/lib/firmware/ath10k/QCA6174/hw3.0/board.bin.old
fi

%files
/usr/lib/firmware/ath10k/QCA6174/hw2.1/board.bin
/usr/lib/firmware/ath10k/QCA6174/hw3.0/board.bin

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