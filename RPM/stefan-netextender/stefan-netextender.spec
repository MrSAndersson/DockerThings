Name: stefan-netextender
Version: 8.6.801
Release: 1%{?dist}
Summary: Dell netExtender VPN Client

License: Proprietary
Source0: NetExtender.x86_64.tgz
#BuildArch: x86_64
Requires: net-tools NetworkManager-ppp

%description
A srepackage of Dell netExtender into an RPM for ease of automatic install

%prep
tar xf NetExtender.x86_64.tgz --strip 1

%install
./install

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
%doc netExtender.1
%config /etc/ppp/peers/sslvpn

/usr/sbin/netExtender
/usr/bin/netExtenderGui
/usr/sbin/nxMonitor
/usr/sbin/uinstallNetExtender

/usr/lib/NetExtender.jar
/usr/lib64/libNetExtender.so
/usr/lib64/libNetExtenderEpc.so

/usr/share/netExtender/ca-bundle.crt
/usr/share/netExtender/icons/*
/usr/share/netExtender/NetExtender.desktop
/usr/share/applications/sonicwall-netextender.desktop


%changelog