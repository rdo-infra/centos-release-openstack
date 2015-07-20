%global OpenStackVersion kilo
Summary: OpenStack from the CentOS Cloud SIG repo configs
Name: centos-release-openstack-%{OpenStackVersion}
Version: 1
Release: 2%{?dist}
License: GPL
URL: http://wiki.centos.org/SpecialInterestGroup/Cloud
Source0: CentOS-OpenStack.repo
Source1: RPM-GPG-KEY-CentOS-SIG-Cloud

BuildArch: noarch

Requires: centos-release
Provides: centos-release-openstack = %{OpenStackVersion}
Obsoletes: centos-release-openstack < %{OpenStackVersion}-3

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
* Mon Jul 20 2015 Alan Pevec <apevec@redhat.com> %{OpenStackVersion}-1-2
- Allow users to stay on a specific release. (Thomas <alphacc@gmail.com>)

* Mon May 18 2015 Alan Pevec <apevec@redhat.com> %{OpenStackVersion}-2
- update repository URL

* Thu May 14 2015 Alan Pevec <apevec@redhat.com> %{OpenStackVersion}-1
- Initial version based on centos-release-gluster
