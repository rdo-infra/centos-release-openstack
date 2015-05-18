Summary: OpenStack from the CentOS Cloud SIG repo configs
Name: centos-release-openstack
Version: kilo
Release: 2%{?dist}
License: GPL
URL: http://wiki.centos.org/SpecialInterestGroup/Cloud
Source0: CentOS-OpenStack.repo
Source1: RPM-GPG-KEY-CentOS-SIG-Cloud

BuildArch: noarch

Requires: centos-release

%description
yum Configs and basic docs for OpenStack as delivered via the CentOS Cloud SIG.

%prep

%install
install -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-OpenStack-%{version}.repo
sed -i -e "s/OPENSTACK_VERSION/%{version}/g" %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-OpenStack-%{version}.repo
install -p -d %{buildroot}%{_sysconfdir}/pki/rpm-gpg
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pki/rpm-gpg

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/yum.repos.d/*
%{_sysconfdir}/pki/rpm-gpg

%changelog
* Mon May 18 2015 Alan Pevec <apevec@redhat.com> %{version}-2
- update repository URL

* Thu May 14 2015 Alan Pevec <apevec@redhat.com> %{version}-1
- Initial version based on centos-release-gluster
