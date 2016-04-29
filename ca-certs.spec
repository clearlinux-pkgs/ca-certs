Name:           ca-certs
Version:        2.4
Release:        17
License:        MPL-2.0 GPL-2.0
Summary:        System CA Certificates
Url:            https://www.mozilla.org/en-US/about/governance/policies/security-group/certs/
Group:          base
# From Mozilla MPL-2.0, $ make update
Source0:        certdata.txt
# From Debian ca-certificates package GPL-2.0
Source1:        certdata2pem.py
Source2:        blacklist.txt
BuildRequires:  /usr/bin/c_rehash
BuildRequires:  /usr/bin/python

%description
System CA Certificates.

%prep

%build
rm -rf build
mkdir -p build
cp %{SOURCE0} %{SOURCE1} %{SOURCE2} build/
pushd build
python certdata2pem.py
rm *.py *.txt
c_rehash ./
popd

%install
mkdir -p %{buildroot}%{_datadir}/
cp -a build/ %{buildroot}%{_datadir}/ca-certs/

%files
%{_datadir}/ca-certs/*.crt
%{_datadir}/ca-certs/*.0
%{_datadir}/ca-certs/*.1
