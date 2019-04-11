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
tar xf NetExtender.x86_64.tgz --strip 1

%install
mkdir -p %{buildroot}/etc/ppp/peers
mkdir -p %{buildroot}/usr/share/man/man1
mkdir -p %{buildroot}/usr/share/netExtender/icons
install -m 644 %{buildroot}sslvpn /etc/ppp/peers/sslvpn
install -m 755 %{buildroot}netExtender /usr/sbin
install -m 755 %{buildroot}netExtenderGui /usr/bin
install -m 744 %{buildroot}nxMonitor /usr/sbin
install -m 755 %{buildroot}uninstallNetExtender /usr/sbin

rm -f %{buildroot}/etc/ppp/sslvpn.pid
rm -f %{buildroot}/etc/ppp/sslvpn.pid2
install -m 644 %{buildroot}netExtender.1 /usr/share/man/man1/netExtender.1
install -m 755 %{buildroot}libNetExtender.so $USRLIB
install -m 755 %{buildroot}libNetExtenderEpc.so $USRLIB
install -m 644 %{buildroot}$CABUNDLE /usr/share/netExtender

# Don't use USRLIB variable for jar; netExtenderGui is hard-coded to /usr/lib
install -m 644 %{buildroot}NetExtender.jar /usr/lib
install -m 644 %{buildroot}icons/* /usr/share/netExtender/icons
install -m 664 %{buildroot}NetExtender.desktop /usr/share/netExtender

/usr/sbin/netExtender -i
chmod 755 %{buildroot}/etc/ppp/ip-up %{buildroot}/etc/ppp/ip-down
chmod 755 %{buildroot}/etc/ppp/ipv6-up %{buildroot}/etc/ppp/ipv6-down

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