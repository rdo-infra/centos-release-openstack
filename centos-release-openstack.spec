%global OpenStackVersion queens
Summary: OpenStack from the CentOS Cloud SIG repo configs
Name: centos-release-openstack-%{OpenStackVersion}
Version: 1
Release: 2%{?dist}
License: GPL
URL: http://wiki.centos.org/SpecialInterestGroup/Cloud
Source0: CentOS-OpenStack.repo
Source1: RPM-GPG-KEY-CentOS-SIG-Cloud

ExclusiveArch:  x86_64 aarch64 ppc64le

Requires: centos-release
Requires: centos-release-ceph-luminous
Requires: centos-release-qemu-ev
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
* Thu Aug 8 2018 Adam Kimball <baha@linux.vnet.ibm.com> %{OpenStackVersion}-1-2
- use contentdir and releasever yum variables

* Tue Feb 27 2018 Alfredo Moralejo <amoralej AT redhat.com> %{OpenStackVersion}-1-1
- %{OpenStackVersion} releases
