Name:           system-installer
Version:        2.0
Release:        0
License:        GPL-2.0
Summary:        Tizen installer
Group:          Base/Utilities
Source:         %{name}-%{version}.tar.xz
Source1001:     system-installer.manifest
Requires:       bmap-tools
Requires:       curl
Requires:       dialog
Requires:       rsync
Requires:		util-linux
BuildArch:		noarch


%description
Installs a Tizen image from an USB stick to a local hard-disk.


%prep
%setup -q
cp %{SOURCE1001} .


%build


%install

install -d %{buildroot}/%{_prefix}/lib/%{name}
install -d %{buildroot}/%{_sysconfdir}
install -d %{buildroot}/%{_sbindir}
install -d %{buildroot}/%{_unitdir}/default.target.wants
install -d %{buildroot}/root
install -m 0644 systemd/system-installer.service %{buildroot}/%{_unitdir}
install -m 0644 scripts/system-installer.conf  %{buildroot}/%{_sysconfdir}/system-installer.conf
install -m 0775 scripts/dialog-helper  %{buildroot}/%{_prefix}/lib/%{name}/dialog-helper
install -m 0775 scripts/wifi  %{buildroot}/%{_prefix}/lib/%{name}/wifi
install -m 0775 scripts/disk-util  %{buildroot}/%{_prefix}/lib/%{name}/disk-util
install -m 0775 scripts/url-util  %{buildroot}/%{_prefix}/lib/%{name}/url-util
install -m 0775 scripts/wifi-util  %{buildroot}/%{_prefix}/lib/%{name}/wifi-util
install -m 0775 scripts/keyboard-util  %{buildroot}/%{_prefix}/lib/%{name}/keyboard-util
install -m 0775 scripts/system-installer  %{buildroot}/%{_sbindir}/system-installer
install -m 0644 scripts/.dialogrc  %{buildroot}/root/.dialogrc
ln -sf ../system-installer.service %{buildroot}/%{_unitdir}/default.target.wants/system-installer.service


%files
%manifest %{name}.manifest
%defattr(-,root,root)
%config %{_sysconfdir}/system-installer.conf
%{_unitdir}/system-installer.service
%{_unitdir}/default.target.wants/system-installer.service
%{_sbindir}/system-installer
%{_prefix}/lib/%{name}/dialog-helper
%{_prefix}/lib/%{name}/wifi
%{_prefix}/lib/%{name}/disk-util
%{_prefix}/lib/%{name}/url-util
%{_prefix}/lib/%{name}/wifi-util
%{_prefix}/lib/%{name}/keyboard-util
/root/.dialogrc
