#!/bin/bash
set -e -o pipefail

curl -q -o certdata.txt https://hg.mozilla.org/mozilla-central/raw-file/tip/security/nss/lib/ckfw/builtins/certdata.txt
git diff --exit-code && exit

make bumpnogit
git commit -m "certdata update" release certdata.txt ca-certs.spec
make koji-nowait
