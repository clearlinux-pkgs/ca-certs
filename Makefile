PKG_NAME := ca-certs
URL := http://download.clearlinux.org/sources/0.5/ca-certs-0.1.tar.xz

include ../common/Makefile.common

update:
	curl -O https://hg.mozilla.org/mozilla-central/raw-file/0ca37b3cb73d/security/nss/lib/ckfw/builtins/certdata.txt
