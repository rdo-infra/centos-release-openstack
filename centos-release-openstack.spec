%global OpenStackVersion victoria
Summary: OpenStack from the CentOS Cloud SIG repo configs
Name: centos-release-openstack-%{OpenStackVersion}
Version: 1
Release: 1%{?dist}
License: GPL
URL: http://wiki.centos.org/SpecialInterestGroup/Cloud
Source0: CentOS-OpenStack.repo
Source1: RPM-GPG-KEY-CentOS-SIG-Cloud

BuildArch: noarch

Requires: centos-release
Requires: centos-release-advanced-virtualization
Requires: centos-release-rabbitmq-38
Requires: centos-release-ceph-nautilus
Requires: centos-release-nfv-openvswitch
Conflicts: centos-release-openstack

%description
yum Configs and basic docs for OpenStack as delivered via the CentOS Cloud SIG.

%prep

%install
install -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-OpenStack-%{OpenStackVersion}.repo
sed -i -e "s/OPENSTACK_VERSION/%{OpenStackVersion}/g" %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-OpenStack-%{OpenStackVersion}.repo
install -p -d %{buildroot}%{_sysconfdir}/pki/rpm-gpg
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pki/rpm-gpg

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/yum.repos.d/*
%{_sysconfdir}/pki/rpm-gpg

%changelog
* Wed Oct 14 2020 Yatin Karel <ykarel@redhat.com> - %{OpenStackVersion}-1-1
- Victoria Release
- Rely on centos-release-advanced-virtualization and centos-release-nfv-openvswitch
