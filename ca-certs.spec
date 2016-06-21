Name:           ca-certs
Version:        2.4
Release:        19
License:        MPL-2.0 GPL-2.0
Summary:        System CA Certificates
Url:            https://www.mozilla.org/en-US/about/governance/policies/security-group/certs/
Group:          base
# From Mozilla MPL-2.0, $ make update
Source0:        certdata.txt
# From Debian ca-certificates package GPL-2.0
Source1:        certdata2pem.py
Source2:        blacklist.txt
Source3:        cache-certs
BuildRequires:  /usr/bin/c_rehash
BuildRequires:  /usr/bin/python
BuildRequires:  p11-kit
BuildRequires:  p11-kit-bin

%description
System CA Certificates.

%prep

%build
rm -rf build
mkdir -p build
cp %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} build/
pushd build
python certdata2pem.py
rm *.py *.txt
c_rehash ./
mkdir cache
./cache-certs . cache
rm cache-certs
popd

%install
mkdir -p %{buildroot}%{_datadir}/
cp -a build/ %{buildroot}%{_datadir}/ca-certs/
mkdir -p %{buildroot}%{_datadir}/ca-certs/cache

%files
%{_datadir}/ca-certs/*.crt
%{_datadir}/ca-certs/*.0
%{_datadir}/ca-certs/*.1
%{_datadir}/ca-certs/cache/*.p11-kit
%{_datadir}/ca-certs/cache/extracted/openssl/ca-bundle.trust.pem
%{_datadir}/ca-certs/cache/extracted/pem/tls-ca-bundle.pem
%{_datadir}/ca-certs/cache/extracted/pem/email-ca-bundle.pem
%{_datadir}/ca-certs/cache/extracted/pem/objsign-ca-bundle.pem
%{_datadir}/ca-certs/cache/extracted/java/cacerts
