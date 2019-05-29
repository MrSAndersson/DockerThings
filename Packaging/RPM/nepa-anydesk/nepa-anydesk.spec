Name: nepa-anydesk
Version: 4.0.1
Release: 1%{?dist}
Summary: Nepa licensed AnyDesk

License: Proprietary
Source0: AnyDeskNepa.tar.gz

%description
Nepa licensed AnyDesk repackaged as an RPM


%prep
tar xfz %{SOURCE0} --strip 1


%install
mkdir -p %{buildroot}/usr/bin
install -p -m 755 anydesk %{buildroot}/usr/bin/

mkdir -p %{buildroot}/usr/share/applications/
install -p -m 644 anydesk.desktop %{buildroot}/usr/share/applications/

mkdir -p %{buildroot}/usr/share/icons/hicolor/16x16/apps
install -p -m 644 icons/hicolor/16x16/apps/anydesk.png %{buildroot}/usr/share/icons/hicolor/16x16/apps/

mkdir -p %{buildroot}/usr/share/icons/hicolor/24x24/apps
install -p -m 644 icons/hicolor/24x24/apps/anydesk.png %{buildroot}/usr/share/icons/hicolor/24x24/apps/

mkdir -p %{buildroot}/usr/share/icons/hicolor/32x32/apps
install -p -m 644 icons/hicolor/32x32/apps/anydesk.png %{buildroot}/usr/share/icons/hicolor/32x32/apps/

mkdir -p %{buildroot}/usr/share/icons/hicolor/48x48/apps
install -p -m 644 icons/hicolor/48x48/apps/anydesk.png %{buildroot}/usr/share/icons/hicolor/48x48/apps/

mkdir -p %{buildroot}/usr/share/icons/hicolor/256x256/apps
install -p -m 644 icons/hicolor/256x256/apps/anydesk.png %{buildroot}/usr/share/icons/hicolor/256x256/apps/

mkdir -p %{buildroot}/usr/share/icons/hicolor/scalable/apps
install -p -m 644 icons/hicolor/scalable/apps/anydesk.svg %{buildroot}/usr/share/icons/hicolor/scalable/apps/

mkdir -p %{buildroot}/usr/share/polkit-1/rules.d
install -p -m 644 polkit-1/com.philandro.anydesk.policy %{buildroot}/usr/share/polkit-1/rules.d/

mkdir -p %{buildroot}/etc/systemd/system
install -p -m 755 systemd/anydesk.service %{buildroot}/etc/systemd/system/


%files
%doc copyright
%doc README

/usr/bin/anydesk
/usr/share/applications/anydesk.desktop
/usr/share/icons/hicolor/16x16/apps/anydesk.png
/usr/share/icons/hicolor/24x24/apps/anydesk.png
/usr/share/icons/hicolor/32x32/apps/anydesk.png
/usr/share/icons/hicolor/48x48/apps/anydesk.png
/usr/share/icons/hicolor/256x256/apps/anydesk.png
/usr/share/icons/hicolor/scalable/apps/anydesk.svg
/usr/share/polkit-1/rules.d/com.philandro.anydesk.policy
/etc/systemd/system/anydesk.service


%clean
rm anydesk anydesk.desktop changelog copyright README
rm -rf %{buildroot} icons systemd polkit-1 init

%changelog