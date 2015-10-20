%global OpenStackVersion liberty
Summary: RDO OpenStack from the CentOS Cloud SIG repo configs
Name: centos-release-rdo-%{OpenStackVersion}
Version: 1
Release: 4%{?dist}
License: GPL
URL: http://rdoproject.org/
Source0: CentOS-OpenStack.repo
Source1: RPM-GPG-KEY-CentOS-SIG-Cloud

BuildArch: noarch

Requires: system-release
Conflicts: centos-release-openstack
Provides: centos-release-openstack-%{OpenStackVersion}
Obsoletes: centos-release-openstack-liberty < 1-4

%description
yum Configs and basic docs for RDO OpenStack as delivered via the CentOS Cloud SIG.

%prep

%install
install -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-RDO-OpenStack-%{OpenStackVersion}.repo
sed -i -e "s/OPENSTACK_VERSION/%{OpenStackVersion}/g" %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-RDO-OpenStack-%{OpenStackVersion}.repo
install -p -d %{buildroot}%{_sysconfdir}/pki/rpm-gpg
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pki/rpm-gpg

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/yum.repos.d/*
%{_sysconfdir}/pki/rpm-gpg

%changelog
* Tue Oct 20 2015 Alan Pevec <apevec@redhat.com> %{OpenStackVersion}-1-4
- %{OpenStackVersion} release
