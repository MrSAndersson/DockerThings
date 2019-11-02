Name: stefan-netextender
Version: 8.6.801
Release: 1%{?dist}
Summary: Dell netExtender VPN Client

License: Proprietary
Source0: NetExtender.x86_64.tgz
#BuildArch: x86_64
Requires: net-tools NetworkManager-ppp

%description
A repackage of Dell netExtender into an RPM for ease of automatic install

%prep
tar xf NetExtender.x86_64.tgz

%install
mkdir -p %{buildroot}/etc/ppp/peers
mkdir -p %{buildroot}/usr/share/man/man1
mkdir -p %{buildroot}/usr/share/netExtender/icons
mkdir -p %{buildroot}/usr/lib
mkdir -p %{buildroot}/usr/lib64
mkdir -p %{buildroot}/usr/share/man/man1/
mkdir -p %{buildroot}/usr/sbin
mkdir -p %{buildroot}/usr/bin


install -m 644 netExtenderClient/sslvpn %{buildroot}/etc/ppp/peers/sslvpn
install -m 755 netExtenderClient/netExtender %{buildroot}/usr/sbin/
install -m 755 netExtenderClient/netExtenderGui %{buildroot}/usr/bin/
install -m 744 netExtenderClient/nxMonitor %{buildroot}/usr/sbin/
install -m 755 netExtenderClient/uninstallNetExtender %{buildroot}/usr/sbin/

#install -m 644 netExtenderClient/netExtender.1 %{buildroot}/usr/share/man/man1/netExtender.1
install -m 755 netExtenderClient/libNetExtender.so %{buildroot}/usr/lib64/
install -m 755 netExtenderClient/libNetExtenderEpc.so %{buildroot}/usr/lib64/
install -m 644 netExtenderClient/ca-bundle.crt %{buildroot}/usr/share/netExtender/

# Don't use USRLIB variable for jar; netExtenderGui is hard-coded to /usr/lib
install -m 644 netExtenderClient/NetExtender.jar %{buildroot}/usr/lib/
install -m 644 netExtenderClient/icons/* %{buildroot}/usr/share/netExtender/icons/
install -m 664 netExtenderClient/NetExtender.desktop %{buildroot}/usr/share/netExtender/

mkdir -p %{buildroot}/usr/share/applications
cp %{buildroot}/usr/share/netExtender/NetExtender.desktop %{buildroot}/usr/share/applications/sonicwall-netextender.desktop


%pre
rm -f /etc/ppp/sslvpn.pid
rm -f /etc/ppp/sslvpn.pid2

%post
/usr/sbin/netExtender -i
chmod 755 /etc/ppp/ip-up /etc/ppp/ip-down
chmod 755 /etc/ppp/ipv6-up /etc/ppp/ipv6-down

chmod -v u+s /usr/sbin/pppd
chmod -v a+x /usr/sbin/pppd
chmod -v a+rx /etc/ppp
chmod -v -R a+r /etc/ppp/peers
chmod -v a+x /etc/ppp/peers


%files
%doc netExtenderClient/netExtender.1
%config /etc/ppp/peers/sslvpn

/usr/sbin/netExtender
/usr/bin/netExtenderGui
/usr/sbin/nxMonitor
/usr/sbin/uninstallNetExtender

/usr/lib/NetExtender.jar
/usr/lib64/libNetExtender.so
/usr/lib64/libNetExtenderEpc.so

/usr/share/netExtender/ca-bundle.crt
/usr/share/netExtender/icons/*
/usr/share/netExtender/NetExtender.desktop
/usr/share/applications/sonicwall-netextender.desktop


%changelog