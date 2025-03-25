Name:           ca-certs
Version:        2.4
Release:        69
License:        MPL-2.0 GPL-2.0
Summary:        System CA Certificates
Url:            https://www.mozilla.org/en-US/about/governance/policies/security-group/certs/
Group:          base
# From Mozilla MPL-2.0, $ make update
Source0:        certdata.txt
# From Debian ca-certificates package GPL-2.0
Source1:        certdata2pem.py
Source2:        blacklist.txt
Source4:        dynamic-trust-store.service
Requires:       p11-kit
Requires:       clrtrust
BuildRequires:  python3-core
Provides:       ca-certificates

%description
System CA Certificates.

%prep
rm -rf *

%build
cp %{SOURCE0} %{SOURCE1} %{SOURCE2} .
python %{SOURCE1}
rm %{SOURCE0} %{SOURCE1} %{SOURCE2}
# make sure clrtrust is capable of generating a trust store out of theses
mkdir -p clr_src/trusted clr_store
cp *.crt clr_src/trusted
CLR_TRUST_STORE=clr_store CLR_CLEAR_TRUST_SRC=clr_src clrtrust generate
rm -rf clr_src clr_store

%install
mkdir -p %{buildroot}/usr/share/ca-certs/trusted
mkdir -p %{buildroot}/usr/share/ca-certs/distrusted
cp *.crt %{buildroot}/usr/share/ca-certs/trusted
mkdir -p %{buildroot}/usr/lib/systemd/system/update-triggers.target.wants
install -m 0644 %{SOURCE4} %{buildroot}/usr/lib/systemd/system/dynamic-trust-store.service
(cd %{buildroot}/usr/lib/systemd/system/update-triggers.target.wants && ln -s ../dynamic-trust-store.service .)

%files
/usr/share/ca-certs/trusted/*.crt
/usr/lib/systemd/system/dynamic-trust-store.service
/usr/lib/systemd/system/update-triggers.target.wants/dynamic-trust-store.service
