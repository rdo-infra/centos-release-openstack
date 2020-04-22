%global OpenStackVersion train
Summary: OpenStack from the CentOS Cloud SIG repo configs
Name: centos-release-openstack-%{OpenStackVersion}
Version: 2
Release: 1%{?dist}
License: GPL
URL: http://wiki.centos.org/SpecialInterestGroup/Cloud
Source0: CentOS-OpenStack.repo
Source1: RPM-GPG-KEY-CentOS-SIG-Cloud
Source2: RPM-GPG-KEY-CentOS-SIG-Virtualization-RDO
Source3: advanced-virtualization.repo
Source4: ceph-nautilus.repo

BuildArch: noarch

Requires: centos-release
%if 0%{?rhel} == 7
Requires: centos-release-qemu-ev
Requires: centos-release-ceph-nautilus
%else
Requires: centos-release-rabbitmq-38
Requires: centos-release-storage-common
%endif
Conflicts: centos-release-openstack

%description
yum Configs and basic docs for OpenStack as delivered via the CentOS Cloud SIG.

%prep

%install
install -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-OpenStack-%{OpenStackVersion}.repo
sed -i -e "s/OPENSTACK_VERSION/%{OpenStackVersion}/g" %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-OpenStack-%{OpenStackVersion}.repo
install -p -d %{buildroot}%{_sysconfdir}/pki/rpm-gpg
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pki/rpm-gpg

%if 0%{?rhel} == 8
install -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/pki/rpm-gpg
install -p -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/yum.repos.d
install -p -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/yum.repos.d
%endif

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/yum.repos.d/*
%{_sysconfdir}/pki/rpm-gpg

%changelog
* Wed Apr 22 2020 Alfredo Moralejo <amoralej@redhat.com> - %{OpenStackVersion}-2-1
- Add support for CentOS 8

* Tue Oct 15 2019 Yatin Karel <ykarel@redhat.com> - %{OpenStackVersion}-1-1
- Train release

