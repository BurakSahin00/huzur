"""Testnet anahtarlarını ve .env dosyalarını üretir. Repo kökünden bir kez çalıştır:

    pip install eth-account
    python3 scripts/make_keys.py

Ne yapar:
- Yönetici (dağıtım) anahtarı: şifreli keystore olarak ~/.foundry/keystores/deployer
  (Foundry'de --account deployer ile kullanılır; şifreyi sen girersin).
- Sunucu ve bot anahtarları, HMAC_KEY, SEED_KEY, ADMIN_TOKEN: server/.env içine.
- contracts/.env: rollerin verileceği sunucu adresiyle.
Özel anahtarları ekrana yazmaz; yalnızca üç adresi yazar. Var olan dosyanın üzerine yazmaz.
Yalnızca testnet için.
"""

import getpass
import json
import os
import pathlib
import secrets
import sys

from eth_account import Account

ROOT = pathlib.Path(__file__).resolve().parent.parent
KEYSTORE = pathlib.Path.home() / ".foundry" / "keystores" / "deployer"
SERVER_ENV = ROOT / "server" / ".env"
CONTRACTS_ENV = ROOT / "contracts" / ".env"


def fill(example: pathlib.Path, target: pathlib.Path, values: dict[str, str]) -> None:
    """.env.example'ı kopyalar, verilen anahtarların değerlerini doldurur."""
    lines = []
    for line in example.read_text(encoding="utf-8").splitlines():
        key = line.split("=", 1)[0].strip()
        if "=" in line and not line.lstrip().startswith("#") and key in values:
            line = f"{key}={values[key]}"
        lines.append(line)
    target.write_text("\n".join(lines) + "\n", encoding="utf-8")
    if os.name != "nt":
        target.chmod(0o600)


def main() -> None:
    existing = [p for p in (KEYSTORE, SERVER_ENV, CONTRACTS_ENV) if p.exists()]
    if existing:
        sys.exit("Bu dosyalar zaten var, üzerine yazmıyorum: " + ", ".join(map(str, existing)))

    password = getpass.getpass("Yönetici keystore şifresi: ")
    if not password or password != getpass.getpass("Şifre (tekrar): "):
        sys.exit("Şifreler boş ya da farklı.")

    deployer, server, bot = Account.create(), Account.create(), Account.create()

    KEYSTORE.parent.mkdir(parents=True, exist_ok=True)
    KEYSTORE.write_text(json.dumps(Account.encrypt(deployer.key, password)), encoding="utf-8")
    if os.name != "nt":
        KEYSTORE.chmod(0o600)

    fill(
        ROOT / "server" / ".env.example",
        SERVER_ENV,
        {
            "OPERATOR_PRIVATE_KEY": "0x" + bytes(server.key).hex(),
            "BOT_PRIVATE_KEY": "0x" + bytes(bot.key).hex(),
            "HMAC_KEY": secrets.token_hex(32),
            "SEED_KEY": secrets.token_hex(32),
            "ADMIN_TOKEN": secrets.token_hex(32),
        },
    )
    fill(ROOT / "contracts" / ".env.example", CONTRACTS_ENV, {"SERVER_ADDRESS": server.address})

    print(f"Yönetici (faucet buraya): {deployer.address}")
    print(f"Sunucu:                   {server.address}")
    print(f"Bot:                      {bot.address}")


if __name__ == "__main__":
    main()
