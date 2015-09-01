PKG_NAME := ca-certs
URL := http://download.clearlinux.org/sources/0.5/ca-certs-0.1.tar.xz

-include ../common/Makefile.common

update:
	curl -q -o certdata.txt https://hg.mozilla.org/mozilla-central/raw-file/tip/security/nss/lib/ckfw/builtins/certdata.txt
	git diff --exit-code
