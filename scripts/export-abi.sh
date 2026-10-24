#!/bin/bash
# Kontrat ABI'lerini shared/abi/ altına yazar. Kontrat arayüzü her değiştiğinde çalıştır ve commit et.
# Sunucu ve ön yüz ABI'yi yalnızca buradan okur.
set -e
cd "$(dirname "$0")/.."
(cd contracts && forge build)
mkdir -p shared/abi
for c in Huzur IlkGelen; do
  python3 -c "import json; print(json.dumps(json.load(open('contracts/out/$c.sol/$c.json'))['abi'], indent=2))" >"shared/abi/$c.json"
done
echo "ABI'ler shared/abi/ altına yazıldı."
