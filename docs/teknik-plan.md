# Huzur: Teknik Plan

Oct 24, 2026 · @Burak Şahin

Temel ilke: kura zincirde çekilir ve herkes yeniden hesaplayabilir; kişisel veri zincire girmez; seyircinin MON'a ihtiyacı olmaz. Bu plan sabah karar vermekle vakit kaybetmemek için; kod etkinlikte yazılır.

## Etkinlik kuralları ve puanlama

Kaynak: Monad Blitz Ankara v4 sunumu (24 Ekim 2026). Plan bu kurallara göre kuruldu; başka bir bölümle çelişirse bu bölüm geçerli.

**Kurallar**

- Bütün proje kodu bugün yazılır; standart kütüphaneler serbest. Etkinlikten önce hazırlananlar README'de açıklanır.
- Çalışan, herkese açık bir demo bağlantısı şart. Yerelde barındırılan proje diskalifiye edilir.
- Kod herkese açık bir GitHub reposunda durur.
- Kontratlar etkinlik süresi içinde Monad testnetine dağıtılır; adres ve doğrulanmış kaynak kodu gerekir.
- Düzgün bir README: ne yapar, nasıl kurulur, nasıl çalıştırılır.
- Demo 90 saniye ve canlı; slayt şart değil.
- Teslim blitz.devnads.com üzerinden, son saat **16:30**.

**Geçitler.** Üçü de geçilmeli, yoksa proje sıralamaya girmez. Jürilerin yarısından fazlası "hayır" derse geçit kalır.

| Geçit | Huzur nasıl geçer |
| --- | --- |
| Etkinlikte yazıldı | Public repo, gün boyu küçük commit'ler; README'de "Etkinlik öncesi hazırlık" bölümü |
| Monad'da dağıtıldı | `Huzur` ve `IlkGelen` testnette, kaynak kodu doğrulanmış; adresler README'de ve formda |
| Dürüst pitch | Manşet iddia sahnede canlı çalışır: bot hızı işe yaramaz, sonucu kimse seçemez, herkes doğrular |

**Ağırlıklar.** Son puan = 0,8 × jüri puanı + 0,2 × salon oyu. Jüri her ölçüte 1–5 verir (1 → 0, 5 → 100). Salon oyu en çok oy alan projeye göre ölçeklenir: onun oylarının yarısını alan 10 puan alır. Eşitlikte önce Çalışırlık, sonra Zincir gerekliliği bakılır.

| Ölçüt | Ağırlık | Ne ödüllendirir | Huzur'daki karşılığı |
| --- | --- | --- | --- |
| Çalışırlık | %24 | Canlıda ne kadarı çalışıyor; daha gerçek, daha az sahte | Kontrat, aktarıcı, bot ve kura testnette canlı. Sahte olan tek şey kimlik onayı; bunu sahnede söylüyoruz |
| Zincir gerekliliği · Monad uyumu | %20 | Doğruluk için zincir şart; zincir yalnızca ödeme rayı değil | Zincirsiz kura "bize güvenin" olurdu: mühürlü tohum, kapanış bloğundan entropi, zincirde çekiliş, herkesin yeniden hesaplaması, pasaport başına tek başvuru. Zincirde para dolaşmıyor. Monad: randevu açılışı bir NFT mint'i gibi trafik patlamasıdır; 0,3 sn blok ve 0,6 sn kesinlikle kura canlı izlenir, `eth_sendRawTransactionSync` ile makbuz anında gelir |
| Salon oyu | %20 | Salonun seçimi | Salon kuraya kendisi katılıyor; kazananlar sonucu kendi telefonunda görüyor |
| Problem ve vaat | %16 | Net bir kullanıcı ve bugünden sonra yaşaması için sebep | Vize başvuranı ve randevuyu dağıtan firma; başvuru başına ücret; aynı motor hac kurası, TOKİ ve derbi biletine uyar |
| Özgünlük | %12 | Tanıdık şablonlar yerine taze fikir | Botu yakalamak yerine bot olmayı anlamsız kılmak; kimlik zincire girmeden kimliğe bağlı randevu |
| Sunum | %8 | Net demo; eksikler açıkça söylenir | 90 saniye, önceden hazırlanmış parti, tek dokunuş; eksikler tek cümleyle |

**Bundan çıkan kararlar**

- Laptop ve tünel yok: web Vercel'de, sunucu Render'da (Mimari ve Sunucu bölümleri).
- Render'ın diski kalıcı değil ve sunucu her an yeniden başlayabilir. Tohum `SEED_KEY`'den türetilir, bütün durum zincirden yeniden kurulur.
- Kapı pasaport görüntüsü almaz. Numara kapı cihazında kalır, sunucuya yalnızca özet gider. Sunucuda Tesseract ve PassportEye yok.
- Sunum 90 saniyeye indi (`docs/urun-ozeti.md`).
- Arayüz `docs/marka.md`'deki marka kitine uyar. Sunumdaki öneri: hazır şablon görünümlü arayüz yerine LLM'e yazı tipi, renk ve bileşen ver.
- Demo önceden kurulur: tek dokunuşla başvuru, önceden çekilmiş örnek parti, hazır kısayollar.
- Kod 16:30'da donar. Render ve Vercel `main`'e her push'ta yeniden dağıtır; teslimden sonra push yok.

**Teslim listesi**

- [ ] Public repo bağlantısı
- [ ] Canlı demo: Vercel adresi (`/perde`, `/basvur`, `/dogrula?b=<örnek parti>`)
- [ ] Kontrat adresleri, kaynak kodu doğrulanmış
- [ ] README: ne yapar, nasıl çalışır, kurulum, adresler, etkinlik öncesi hazırlık, eksikler
- [ ] Formun istediği diğer alanlar; video isteniyorsa teslimden önce çekilir

**Sunumdaki Monad araçları**

- `blitz.devnads.com`: token, takım, teslim ve oylama.
- `agents.devnads.com`: `POST /v1/faucet` (istek başına 1 testnet MON, adres başına günde 10), `POST /v1/verify` (MonadVision ve Monadscan'de paralel doğrulama).
- `skills.devnads.com`: kodlama asistanları için Monad becerileri (faucet, kontrat ve ön yüz dağıtımı, indexer). Monad Vakfı bunları denetlemiyor; kurmadan önce oku ve anahtar verme. Bu plan için şart değil.
- `docs.monad.xyz`: ağ bilgileri ve JSON-RPC başvurusu.

## Mimari

```text
Vercel (web)                     Render (sunucu, Frankfurt)              Monad testnet
/basvur ── başvuru ────────────► Uygunluk ──► Aktarıcı ───────────────► Huzur.sol
/kapi ──── bilet + özet ───────► Kapı kaydı ──┘                         IlkGelen.sol (demo)
/perde ─── yoklama, kısayollar ► Önbellek ◄── İzleyici, Bot ◄─────────► okuma ve yazma
/dogrula ◄──────────── zincirden doğrudan okur (viem, sunucuya sormaz) ─ Huzur.sol
                                 Açıklayıcı ──► Claude API (yalnızca herkese açık sayılar)
```

Ön yüz Vercel'de, sunucu Render'da çalışır; ikisi de herkese açık bir adreste. Etkinlik kuralı gereği laptopta barındırma ve tünel yok. Telefonlar sunucuyla konuşur; zincire tek yazan sunucunun aktarıcısıdır, kurayı kontrat çeker, Doğrula sunucuya hiç sormaz. Bot iki kontratı da dener: IlkGelen.sol'de randevuların hepsini alır, Huzur.sol'de uygunluk imzası olmadığı için reddedilir. Claude yalnızca kura sonrası açıklamayı yazar: herkese açık sayıları görür, karara ve anahtarlara erişemez.

**Yığın:** Solidity ve Foundry, FastAPI, Vite + React + viem. Barındırma: Vercel (web) ve Render (sunucu). Monad testnet: chain ID 10143, RPC `https://testnet-rpc.monad.xyz`, explorer `testnet.monadvision.com` (Tanık planlamasında doğrulandı).

## Kontrat tasarımı

Tek kontrat yeterli: `Huzur.sol`. Yanına yalnızca demo için küçük bir `IlkGelen.sol` yazılır.

**Durum**

- `operator`: uygunluk imzalayan ve kapı kaydını yazan adres; rollere bölünmüş hâli Güvenlik bölümünde.
- `Batch`: `slots` (randevu sayısı), `closeBlock` (başvuruların kapandığı blok, açılışta ilan edilir), `seedHash` (tohumun özeti), `entropy` (kapanış bloğunun hash'i), `seed`, `status` (Open, Drawn, Void), `revealDeadline`.
- Parti başına: `commitments[]`, `usedNullifier`, `winnerSlot` (özet → sıra), `checkedIn`.

**Fonksiyonlar**

| Fonksiyon | Kim çağırır | Ne yapar |
| --- | --- | --- |
| `openBatch(slots, closeBlock, seedHash)` | Operatör | Partiyi açar; tohumun özeti baştan zincirde |
| `register(id, nullifier, commitment, sig)` ve `registerBatch(...)` | Herkes (demoda aktarıcı) | Operatörün EIP-712 uygunluk imzasını doğrular; `closeBlock` geçtiyse ya da teklik izi kullanılmışsa reddeder |
| `fixEntropy(id)` | Herkes | `closeBlock` sonrası ilk 256 blok içinde `blockhash(closeBlock)` değerini kaydeder |
| `reveal(id, seed)` | Operatör | `keccak256(seed) == seedHash` ise kurayı çeker |
| `voidBatch(id)` | Herkes | Tohum `revealDeadline` geçtiği hâlde açıklanmadıysa partiyi geçersiz yapar |
| `checkIn(id, commitment)` | Operatör | Yalnızca kazanan ve daha önce giriş yapmamış özet için kapı kaydı |
| `isWinner(id, commitment)` | Herkes (okuma) | Sıra numarasını ya da 0 döner |
| `commitmentsOf(id)` | Herkes (okuma) | Başvuru özetlerini sırasıyla döner; perde ve Doğrula kurayı bununla yeniden çeker |

**Çekiliş**

```solidity
bytes32 r = keccak256(abi.encode(seed, b.entropy));
bytes32[] memory a = commitments[id];
uint256 n = a.length; uint256 k = n < b.slots ? n : b.slots;
for (uint256 i = 0; i < k; i++) {          // kısmi Fisher-Yates
    r = keccak256(abi.encode(r, i));
    uint256 j = i + uint256(r) % (n - i);
    (a[i], a[j]) = (a[j], a[i]);
    winnerSlot[id][a[i]] = uint32(i + 1);
    emit Winner(id, i + 1, a[i]);
}
```

Aynı hesap ön yüzdeki "Doğrula" düğmesinde de yapılır; sonuç kontratınkiyle birebir aynı olmalı.

**256 blok tuzağı.** EVM'de `blockhash` yalnızca son 256 blok için okunabilir. Monad'da blok 300 ms olduğu için bu yaklaşık 77 saniye. `fixEntropy` bu pencerede çağrılmazsa parti geçersiz kalır. Bu yüzden sunucu kapanış bloğunu izleyip çağrıyı hemen yapar; perdede de bir düğme bulunur.

Kapanış bloğu baştan ilan edildiği için operatör blok seçemez. Bloğu üreten taraf hash'i etkileyebilir, ama tohumu bilmediği için sonucu hedefleyemez. Operatörün tek kozu tohumu açıklamamaktır, o da partiyi herkesin gözü önünde düşürür.

**Olaylar:** `BatchOpened`, `Registered(id, index, commitment)`, `Rejected(id, nullifier, reason)`, `EntropyFixed`, `Drawn(id, seed, entropy)`, `Winner(id, slot, commitment)`, `CheckedIn`, `Voided`.

**IlkGelen.sol (demo).** `open(slots)` ve `book(emailHash)`: sınır yalnızca e-posta başına bir randevu. Açılış ve doluş bloklarını saklar; perde dolma süresini buradan yazar. Bot 20 farklı e-postayla tüm randevuları ilk bloklarda alır; bugünkü sistemin birebir modeli.

**Monad notu:** Ücret gas limitinden kesilir. `reveal` ve `registerBatch` için limiti viem tahminiyle ver, gereksiz yüksek limit verme.

**Foundry testleri (ilk 45 dakikada)**

- [ ] Geçersiz imzayla, kapanıştan sonra ya da aynı teklik iziyle başvuru reddedilir.
- [ ] `fixEntropy`, kapanıştan önce ve 256 blok sonrasında reddedilir.
- [ ] Yanlış tohum reddedilir; doğru tohum tam olarak `min(slots, n)` farklı kazanan üretir.
- [ ] Sabit bir tohum ve entropi için kazanan listesi, TypeScript'teki "Doğrula" hesabıyla aynı (test vektörü).
- [ ] Kapı kaydı yalnızca kazanan için ve bir kez yazılır.
- [ ] Süresi geçen parti `voidBatch` ile geçersiz olur.

## Kimlik ve gizlilik

Zincirde iki değer durur ve ikisi de pasaport numarasını açığa çıkarmaz: teklik izi tekrarı engeller, tuzlu özet randevuyu kişiye bağlar.

| Değer | Nasıl üretilir | Ne işe yarar |
| --- | --- | --- |
| Teklik izi (`nullifier`) | Sunucuda `HMAC-SHA256(K_op, pasaportNo ‖ batchId)` | Bir pasaport bir partiye bir kez girer; anahtar sunucuda olduğu için dışarıdan kaba kuvvetle çözülemez |
| Tuzlu özet (`commitment`) | Telefonda `keccak256(pasaportNo ‖ tuz)`, tuz 32 rastgele bayt | Kapıda randevuyu pasaporta bağlar; tuz yalnızca başvuranda kalır |
| Uygunluk imzası | Operatör anahtarıyla EIP-712: `Eligibility{batchId, nullifier, commitment}` | Kontrat yalnızca onaylanmış başvuruyu kabul eder |

**Başvuru akışı**

1. Telefon tuzu üretir, özeti hesaplar, pasaport numarasıyla birlikte sunucuya yollar. Tuz sunucuya gitmez.
2. Sunucu kimliği onaylar (demoda sahte kayıt), teklik izini hesaplar, uygunluğu imzalar ve kuyruğa alır.
3. Telefon "başvuru kartı" gösterir: `batchId` ve tuzu içeren bir QR.

**Kapı akışı**

1. Görevli başvuranın telefonundaki bilet QR'ını okutur; `batchId` ve tuz alınır.
2. Görevli pasaport numarasını pasaporttan yazar. Vakit kalırsa MRZ tarayıcıda okunur (tesseract.js ve `mrz` paketi); fotoğraf cihazdan çıkmaz.
3. Kapı cihazı özeti kendisi hesaplar ve sunucuya yalnızca `batchId` ile özeti gönderir. Sunucu `isWinner` ile bakar; kazanansa `checkIn` yazar. Satılmış randevuda alıcının pasaportu özeti tutturamaz ve ekran kırmızıya döner. Pasaport numarası kapı cihazından çıkmaz.

**Hash uyumu.** Özet TypeScript (viem), Python ve Solidity'de birebir aynı hesaplanmalı: pasaport numarası büyük harf ve `<` dolgusuz, `abi.encodePacked(bytes(no), tuz)`. İlk saat içinde üç dil için tek bir test vektörü sabitle.

**Demo pasaportları.** 6 sahte kimlik (numara ve tuz) ve her biri için bilet QR'ı; kartlarda büyük bir "DEMO" yazısı. Numara elle girildiği için kartlar basılabilir ya da tablette gösterilebilir. Vakit kalırsa kartlara `mrz` paketinin TD3 üreteciyle kontrol haneleri doğru bir MRZ satırı eklenir.

**Örnek parti.** Canlı kurada kimin kazanacağı bilinemez. Kapı demosu ve jürinin sonradan açacağı bağlantı için demo kimlikleriyle önceden çekilmiş bir parti hazırla (`seed_morning.py`). Sahnede o partinin kazanan kartı ve "satın alan" kartı kullanılır; README'deki `/dogrula?b=<id>` bağlantısı da bu partiyi gösterir.

**Passkey (vakit kalırsa).** `base/webauthn-sol` kütüphanesi önce RIP-7212 ön derlemesini dener ([GitHub](https://github.com/base/webauthn-sol)); Monad'ın P-256 ön derlemesi aynı adres ve arayüzle çalışır. Böylece seyirci demosunda "bir cihaz, bir başvuru" zincirde doğrulanır.

**Kişisel veri.** Zincirde pasaport numarası, isim ya da fotoğraf yok. Sunucu pasaport numarasını yalnızca başvuruda, teklik izi için bellekte işler ve saklamaz. Kapıda numara cihazda kalır, sunucuya yalnızca özet gider. Pasaport fotoğrafı hiçbir sunucuya gitmez; Claude'a hiçbir kişisel veri gitmez. Gerçek kurulumda e-pasaport çipi NFC ile okunur ve çipteki verinin devlet imzası doğrulanır (ICAO 9303 pasif doğrulama).

## Sunucu

FastAPI servisi Render'da (Frankfurt bölgesi, Python ortamı) çalışır; ön yüz ayrıca Vercel'de. Sunucu yalnızca ön yüzün adreslerine CORS izni verir (`WEB_ORIGINS`, önizlemeler için isteğe bağlı `WEB_ORIGIN_REGEX`) ve çerez kullanmaz. Zincire yazan tek cüzdan sunucununkidir, seyircinin telefonunda cüzdan ve MON gerekmez.

**Render'ın sınırları.** Ücretsiz örnek 15 dakika istek almazsa uyur ve uyanması yaklaşık bir dakika sürer. Render ücretsiz örneği her an yeniden başlatabilir ve disk kalıcı değildir. Bu yüzden sunucunun bütün durumu zincirden ve ortam değişkenlerinden yeniden kurulabilmeli: tohum dosyası, kuyruk dosyası ya da açıklama dosyası yok. Kart ekleyebiliyorsan demo günü için `0.5c-512mb` örneğe geç; ücret saniye bazında, bir gün yaklaşık 25 sent. Örnek uyumaz ve daha fazla CPU alır. Kurulum `render.yaml` ile: repo kökünde, gizli değerler `sync: false`, dağıtım yalnızca `server/` değişince tetiklenir.

| Uç nokta | Girdi | Çıktı |
| --- | --- | --- |
| `POST /eligibility` | batchId, pasaportNo, commitment | nullifier, imza, kuyruk sırası |
| `GET /batch/:id` | — | Durum, başvuru sayısı, kapanışa kalan blok; çekildiyse kazanan özetleri |
| `POST /checkin` | batchId, commitment | Kazanan mı, sıra no, işlem hash'i |
| `GET /gate/last` | — | Kapıdaki son deneme: sonuç ve nedeni |
| `POST /admin/open` | Randevu sayısı, süre (saniye) | batchId, kapanış bloğu |
| `POST /admin/bot` | — | `IlkGelen` kaç blokta doldu; Huzur'da deneme ve kabul sayısı |
| `GET /health` | — | Cüzdan bakiyeleri, son blok, kuyruk uzunluğu |
| `GET /explain/:id` | — | Kura açıklaması (Claude): Türkçe ve İngilizce metin; yoksa 404 |

`/checkin` ve `/admin/*` yalnızca `X-Admin-Token` başlığıyla çalışır.

**Arka plan görevleri**

- *Aktarıcı:* 1–2 saniyede bir kuyruktaki başvuruları tek `registerBatch` işlemiyle yazar. Geçersiz kaydı kontrat atlar ve Rejected olayı yayar; işlemin tamamı ancak parti kapandıysa geri döner; böylece 100 telefon RPC'ye 100 ayrı işlem göndermez. İşlemi Monad'ın `eth_sendRawTransactionSync` yöntemiyle (`hex_tx`, `timeout_ms`) gönderir; yanıt makbuzla döner ve telefon "zincirde" onayını hemen görür. RPC yöntemi tanımazsa normal `eth_sendRawTransaction` ve makbuz yoklamasına düşer. İlk dağıtımdan sonra testnette bir kez dene.
- *İzleyici:* kapanış bloğu geçer geçmez `fixEntropy`, ardından `reveal` gönderir; kura onaylanınca açıklamayı bir kez ürettirir. Sunucu yeniden başlarsa açık partileri zincirden okur ve tohumlarını `SEED_KEY`'den yeniden türetir.
- *Önbellek:* açılışta ve sonra saniyede bir parti durumunu zincirden okur. Telefonlar zinciri değil bu önbelleği yoklar; salon tek IP'den çıktığı için 100 telefon zinciri doğrudan yoklasa `eth_call` için 25 rps sınırı aşılır.

Aktarıcı ve izleyici aynı anahtarla yazar: işlemleri tek bir kilitli kuyruktan, nonce'u yerelde sayarak gönder. Yoksa iki görev aynı nonce'la çakışır. Sunucu açılışta nonce'u zincirden (`pending`) okur.

**Uygunluk imzası**

```python
nullifier = hmac.new(HMAC_KEY, f"{no}|{batch_id}".encode(), hashlib.sha256).digest()
DOMAIN = {"name": "Huzur", "version": "1", "chainId": 10143, "verifyingContract": CONTRACT}
TYPES = {"Eligibility": [{"name": "batchId", "type": "uint256"},
                         {"name": "nullifier", "type": "bytes32"},
                         {"name": "commitment", "type": "bytes32"}]}
sig = Account.sign_typed_data(OPERATOR_KEY, DOMAIN, TYPES, {
    "batchId": batch_id, "nullifier": nullifier, "commitment": commitment}).signature
```

Teklik izindeki `|` ayırıcısı şart: ayırıcı olmadan `"U1234567" + "81"` ile `"U12345678" + "1"` aynı metni verir. Kontrat aynı özeti OpenZeppelin `EIP712("Huzur", "1")` ile kurar: `_hashTypedDataV4(keccak256(abi.encode(ELIGIBILITY_TYPEHASH, id, nullifier, commitment)))`, typehash `"Eligibility(uint256 batchId,bytes32 nullifier,bytes32 commitment)"`. Plan yazılırken denendi: `eth-account` 0.14'ün imzaladığı özet standart EIP-712 hesabıyla birebir aynı; `commitment` hex metin olarak da verilebilir.

**Partiler**

- `POST /admin/open`: tohumu `SEED_KEY`'den türetir ve özetini, kapanış bloğuyla birlikte zincire koyar. Diskte tohum dosyası yok; sunucu yeniden başlasa da aynı tohum hesaplanır.

  ```python
  seed = hmac.new(SEED_KEY, f"seed|{chain_id}|{contract.lower()}|{batch_id}".encode(), hashlib.sha256).digest()
  seed_hash = keccak(seed)  # abi.encodePacked(bytes32) = 32 baytın kendisi
  ```

  `batch_id` kontratın sıradaki parti numarasıdır; açılış olayındaki numarayla aynı olduğunu doğrula. Parti açan tek adres sunucu olduğu için yarış olmaz. Süre saniye olarak gelir ve son 100 bloğun ortalama süresiyle bloğa çevrilir. Varsayılan 20 randevu ve 45 saniye.
- `make_cards.py`: 6 demo kimlik (numara ve tuz) ve her biri için bilet QR'ı üretir; kartlarda büyük bir "DEMO" yazısı bulunur. Vakit kalırsa `mrz` paketinin `TD3CodeGenerator`'ıyla MRZ satırı da eklenir.
- `seed_morning.py`: örnek parti. Bu 6 kimlikle ayrı bir parti açar (2 randevu), başvuruları yazar, kurayı çeker ve kazanan kartları söyler. Sahnede bir kazanan kart ile kazanmayan bir kart kullanılır; jürinin açacağı doğrulama bağlantısı da bu partiyi gösterir.

**Bot (`POST /admin/bot`)**

- `IlkGelen`: 20 farklı e-posta özetiyle 20 `book` işlemini ardışık nonce'larla aynı anda gönderir; randevuların hepsi ilk bloklarda gider.
- `Huzur`: 1.000 imzasız `register` denemesini Multicall3 `aggregate3` (`allowFailure: true`) ile 250'lik 4 `eth_call` paketinde dener; hepsi `success=false` döner. Explorer'da görünsün diye 3 tanesini gerçek işlem olarak da gönderir. Geri dönecek işlemde gas tahmini hata verir, limiti elle ver.
- Multicall3 testnette kanonik adreste: `0xcA11bde05977b3631167028862bE2a173976CA11`.
- Bot ayrı bir anahtar kullanır; aktarıcının nonce sırasına karışmaz.

**Ayarlar:** `OPERATOR_PRIVATE_KEY`, `BOT_PRIVATE_KEY`, `HMAC_KEY`, `SEED_KEY`, `ADMIN_TOKEN`, `ANTHROPIC_API_KEY`, `RPC_URL`, `CONTRACT_ADDRESS`, `ILKGELEN_ADDRESS`, `WEB_ORIGINS`. Yerelde `server/.env` dosyasından, Render'da ortam değişkenlerinden okunur. Tohumlar açıklanana kadar loglara yazılmaz; `.env` depoya girmez.

**Paketler:** `fastapi`, `uvicorn`, `pydantic-settings`, `eth-account`, `web3`, `qrcode`, `anthropic`. Tesseract ve PassportEye yok: sunucu pasaport görüntüsü almaz.

## Ön yüz

Tek bir Vite + React uygulaması, dört rota. Vercel'de yayınlanır (kök `web/`, SPA yönlendirmesi `web/vercel.json`); API adresi `VITE_API_URL`. Her PR bir önizleme adresi alır. Hiçbir ekranda cüzdan bağlama yok: telefonlar sunucuyla konuşur, perde ve Doğrula zinciri doğrudan okur. `monadTestnet` viem'de hazır tanımlı (`viem/chains`); explorer bağlantılarını `testnet.monadvision.com` olarak kendin ver. Görünüm `docs/marka.md`'deki marka kitine uyar.

| Rota | Kim | Ne yapar |
| --- | --- | --- |
| `/basvur` | Seyirci, perdedeki QR ile | Tek dokunuşla başvuru, başvuru kartı, kura sonucu |
| `/perde` | Projeksiyon | Sunumun kendisi: bot, başvuru, kura, kapı ve doğrulama sahneleri |
| `/kapi` | Görevli, sahnedeki telefon | Pasaport fotoğrafı, başvuru kartı QR'ı, yeşil ya da kırmızı |
| `/dogrula` | Herkes | Kurayı tarayıcıda, yalnızca zincir verisiyle yeniden çeker |

**/basvur.** 45 saniyelik pencerede bitmeli; yazılacak hiçbir şey yok.

1. Sayfa açılınca rastgele bir demo pasaport numarası üretir. Seyirciden gerçek pasaport numarası asla istenmez.
2. "Başvur" tuzu üretir, özeti hesaplar ve `POST /eligibility` çağırır.
3. Başvuru kartı: büyük bilet kodu (özetin ilk 6 hanesi), "zincirde" onayı ve işlem bağlantısı, `batchId` ile tuzu taşıyan QR. Kart `localStorage`'a yazılır (try/catch içinde); yenilenen sayfa aynı kartı gösterir.
4. Telefon `GET /batch/:id`'yi 2 saniyede bir yoklar. Kura çekilince kendi özetini kazananlar arasında arar: "Kazandın · sıra 7" ya da "Bu partide çıkmadı".

```ts
const salt = toHex(crypto.getRandomValues(new Uint8Array(32)));
const commitment = keccak256(encodePacked(['string', 'bytes32'], [pasaportNo, salt]));
```

**/perde.** 1920×1080; ok tuşlarıyla sahne değişir, ayrı slayt gerekmez.

- *Açılış ve kapanış:* tek cümlelik metin sahneleri. 90 saniyelik demoda ayrı rakam ya da iş modeli sahnesi yok.
- *Bot:* iki sütun. Solda `IlkGelen`'in 20 randevusu dolar ve kaç blokta dolduğu yazar; sağda Huzur'da 1.000 deneme, 0 kabul ve 3 gerçek işlemin bağlantısı. Etiket dürüst olmalı: "1.000 deneme (kontrata karşı simülasyon) · 3 gerçek işlem, zincirde reddedildi".
- *Başvuru:* büyük QR, geri sayım (blok ve saniye), sayaç ve gelen bilet kodlarının ızgarası; herkes kendi kodunun perdeye düştüğünü görür. QR adresi `location.origin + '/basvur?b=<id>'` ile kurulur (Vercel adresi). Bot sahnesi bu sahnenin yanında, aynı anda oynar.
- *Kura:* "Kapandı · blok #N" → "Entropi sabitlendi" → "Tohum açıklandı" → kazanan kodlar Fisher-Yates sırasıyla tek tek öne çıkar (yaklaşık 3 saniye). Liste perdede `draw.ts` ile yeniden hesaplanır; sahnenin sonunda Claude'un sade açıklaması çıkar.
- *Kapı:* `GET /gate/last`'taki son deneme tam ekran yeşil ya da kırmızı. Reddedilen denemeler zincire yazılmadığı için bu bilgi sunucudan gelir.
- *Doğrula:* `/dogrula?b=<id>` QR'ı ve perdenin kendi üç kontrolü.

Operatör kısayolları `A` (partiyi aç), `B` (bot) ve `E` (entropiyi elle sabitle) sunucuya `ADMIN_TOKEN` ile gider. Token sunumdan önce girilir ve perdede hiç görünmez. Görünüm: koyu zemin, büyük rakamlar, tek vurgu rengi; en küçük yazı 28 px, hash'ler kısaltılmış ve eşit aralıklı yazıyla.

**/kapi**

1. `ADMIN_TOKEN` bir kez girilir (`sessionStorage`).
2. Başvuru kartının QR'ı canlı kamerayla okunur (`qr-scanner`): `batchId` ve tuz.
3. Görevli pasaport numarasını yazar (büyük harf, `<` yok). Vakit kalırsa MRZ tarayıcıda okunur: `<input type="file" accept="image/*" capture="environment">`, tesseract.js ile MRZ bölgesi, `mrz` paketiyle kontrol haneleri. Fotoğraf cihazdan çıkmaz.
4. Özet cihazda hesaplanır ve `POST /checkin {batchId, commitment}` gider.
5. Tam ekran sonuç: yeşil "Giriş · sıra 3" ve işlem bağlantısı; kırmızı "Bu randevu bu pasaporta ait değil" ya da "Bu randevu zaten kullanıldı".

**/dogrula**

- Sunucuya hiç sormaz; sunucu uyusa ya da kapansa da çalışır.
- Okumalar: `batches(id)` ve `commitmentsOf(id)` (Multicall3 ile tek `eth_call`), kapanış bloğunun hash'i (`getBlock`), hesaplanan kazananlar için `isWinner` (yine tek multicall).
- Üç kontrol: tohum baştaki özetle aynı; entropi kapanış bloğunun hash'iyle aynı; tarayıcıda çekilen sıra kontratınkiyle aynı. Kendi bilet kodu varsa vurgulanır.
- Salondaki herkes aynı anda basacak. viem `fallback` ile üç herkese açık RPC kullan: `testnet-rpc.monad.xyz` (50 rps, `eth_call` için 25), `rpc.ankr.com/monad_testnet` (10 saniyede 300 istek), `rpc-testnet.monadinfra.com` (20 rps, toplu istek yok). Sırayı her telefonda karıştır, `retryCount` ver.
- Kura açıklaması varsa üç kontrolün altında görünür (`GET /explain/:id`). Doğrulamanın kendisi sunucuya sormaz; sunucu yoksa yalnızca açıklama görünmez.

**draw.ts.** Kontrattaki döngünün birebir aynısı; perde ve Doğrula kullanır.

```ts
export function draw(seed: Hex, entropy: Hex, commitments: Hex[], slots: number): Hex[] {
  const a = [...commitments], n = a.length, k = Math.min(n, slots);
  let r = keccak256(encodeAbiParameters([{ type: 'bytes32' }, { type: 'bytes32' }], [seed, entropy]));
  for (let i = 0; i < k; i++) {
    r = keccak256(encodeAbiParameters([{ type: 'bytes32' }, { type: 'uint256' }], [r, BigInt(i)]));
    const j = i + Number(BigInt(r) % BigInt(n - i));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a.slice(0, k); // sıra numarası = indeks + 1
}
```

`abi.encode`'un karşılığı `encodeAbiParameters`'tır, `encodePacked` değil; en sık hata bu.

**Test vektörleri.** viem ve Python'da hesaplandı, ikisi aynı çıktı; Foundry testine aynen koy.

- Özet: `pasaportNo = "U12345678"`, tuz `0x000102…1f` (0'dan 31'e kadar baytlar) → `0xa332d5864eb35ece8a162c8de1ab236317a41a79cd349125fb8ce84041412590`
- Kura: `seed = keccak256("torba-seed")`, `entropy = keccak256("torba-entropy")` (metinlerin baytları), i = 1…8 için `c_i = keccak256(abi.encode(uint256(i)))`, 3 randevu → kazananlar sırasıyla c4, c3, c2.

**Paketler:** `viem`, `react-router-dom`, `qrcode`, `qr-scanner`, `@fontsource/ibm-plex-sans`, `@fontsource/ibm-plex-mono`. Vakit kalırsa `tesseract.js` ve `mrz`.

## Yapay zekâ: kura açıklaması

İlke: zincir kanıtlar, kod doğrular, Claude anlatır. Claude güven zincirinin dışında durur; çıkarılsa Huzur aynen çalışır.

**Ne yapar.** Kura çekilince sunucu, partinin herkese açık sonuçlarından Claude'a iki-üç cümlelik sade bir açıklama yazdırır, Türkçe ve İngilizce. Metin parti başına bir kez üretilip saklanır. Perde kura sahnesinin sonunda, `/dogrula` üç kontrolün altında gösterir. Hash okumayan biri, sonucun neden sonradan değiştirilemeyeceğini bu metinden anlar.

| Parça | Seçim |
| --- | --- |
| Model | `claude-sonnet-5-5`, `effort: low`; parti başına tek çağrı |
| Tetikleyici | İzleyici, `reveal` ya da `voidBatch` onaylanınca bir kez çağırır |
| Uç nokta | `GET /explain/:id` → `{tr, en}`; açıklama yoksa 404 ve ön yüz o kısmı gizler |
| Saklama | Bellekte. Sunucu yeniden başlarsa ilk istekte bir kez yeniden üretilir (kilitli, parti başına tek çağrı) |
| Anahtar | `ANTHROPIC_API_KEY` yalnızca sunucuda: yerelde `server/.env`, Render'da ortam değişkeni. Anthropic konsolunda düşük bir harcama sınırı koy |

**Claude'a giden veri.** Sunucu üç kontrolü kura fonksiyonunun Python sürümüyle kendisi yapar (test vektörleri TypeScript ile aynı). Claude'a yalnızca sayılar ve sonuçlar gider, hash bile gitmez:

```json
{"parti": 7, "durum": "Drawn", "randevu": 20, "basvuru": 84,
 "tohum_ozetle_ayni": true, "entropi_blok_hashiyle_ayni": true, "liste_ayni": true}
```

**Talimat (system)**

```text
Sen Huzur kurasının açıklayıcısısın. Kullanıcı mesajında bir partinin herkese açık sonuçlarını JSON olarak alırsın. Bunu teknik bilgisi olmayan bir vize başvurusu sahibine 2-3 kısa cümleyle anlat: kaç kişi başvurdu, kaç randevu vardı, sonuç neden sonradan değiştirilemez.
Yalnızca JSON'daki bilgileri kullan; yeni sayı, oran ya da tarih yazma.
Bir kontrol false ise bunu açıkça söyle ve sonuca güvenilmemesi gerektiğini belirt.
durum "Voided" ise işletenin başlangıç sayısını süresinde açıklamadığını ve partinin herkesin gözü önünde geçersiz sayıldığını söyle.
Kişiler, kazananlar ya da kaybedenler hakkında konuşma.
"Hash", "blok" ve "tohum" yerine "mühür", "kapanış anı" ve "başlangıç sayısı" gibi gündelik sözcükler kullan.
tr alanına Türkçe metni, en alanına aynı metnin İngilizcesini yaz.
```

**Çağrı ve sayı kontrolü**

```python
SCHEMA = {"type": "object", "additionalProperties": False, "required": ["tr", "en"],
          "properties": {"tr": {"type": "string"}, "en": {"type": "string"}}}
resp = client.messages.create(
    model="claude-sonnet-5-5", max_tokens=2000, system=TALIMAT,
    messages=[{"role": "user", "content": json.dumps(veri, ensure_ascii=False)}],
    output_config={"effort": "low", "format": {"type": "json_schema", "schema": SCHEMA}})
metin = json.loads(next(b.text for b in resp.content if b.type == "text"))
izinli = {str(veri["parti"]), str(veri["randevu"]), str(veri["basvuru"])}
if any(set(re.findall(r"\d+", metin[d])) - izinli for d in ("tr", "en")):
    metin = None  # metinde verilmemiş bir sayı var: açıklama gösterilmez
```

`effort` ve yapılandırılmış çıktı aynı `output_config` içinde gider. Düşünme `max_tokens`'a sayıldığı için sınırı dar tutma.

**Güvenlik sınırları**

- *Kişisel veri gitmez:* pasaport numarası, fotoğraf, tuz, bilet kodu ya da IP yok. Yalnızca zincirde zaten açık olan sayılar ve doğru/yanlış sonuçları.
- *Karar vermez:* kazananları, uygunluğu ve kapı sonucunu kod belirler; yeşil ve kırmızı işaretleri de kod çizer. Claude yalnızca metin yazar.
- *Kullanıcı metni almaz:* ziyaretçinin yazdığı hiçbir şey Claude'a gitmez, istem enjeksiyonu için yüzey kalmaz.
- *Zincire yazamaz:* aracı ve cüzdan anahtarı yok. API anahtarı sunucuda kalır; Vite'ta `VITE_` önekli değişkenler tarayıcıya gömülür, anahtarı oraya koyma.
- *Sayı kontrolü:* metinde verilmemiş bir sayı geçerse metin atılır.
- *Hata olursa:* açıklama görünmez, doğrulama aynen çalışır.

**Vakit kalırsa: soru-cevap.** Telefonda "Bu kura adil mi?", "Kazanamazsam ne olur?" gibi sorular. Bu kez ziyaretçinin metni Claude'a gittiği için iki ek kural var: Claude yalnızca okuma yapan araçları çağırır (`parti_bilgisi`, `kurayi_dogrula`; hesabı araç yapar) ve yanıtlar perdeye yansıtılmaz.

**Geliştirme sırasında.** `Huzur.sol`'ü dağıtmadan önce Claude'a gözden geçirt: imzanın başka partide ya da zincirde tekrar kullanılması (EIP-712 alanında `chainId` ve kontrat adresi, yapıda `batchId`), 256 blok penceresi, `reveal` ve `checkIn` yetkileri. Bulguları sen değerlendirirsin.

**Pitch cümlesi.** "Zincir sonucu kanıtlar ama vatandaş hash okumaz. Claude kanıtı herkesin anlayacağı dile çevirir, ama kanıtın kendisine dokunamaz."

## Güvenlik ve kalite: kontrat ve backend

Hedef: jüri kodu açtığında bunun bilerek yapıldığını görsün. Üç dayanak var: yazılı bir tehdit modeli, testlerle kanıtlanan değişmezler ve sunucuda en az yetki. Her madde "bugün", "vakit kalırsa" ya da "ürün sürümü" diye işaretli; bugünküler mevcut zaman dilimlerinin içine sığar.

**Tehdit modeli**

| Kim | Ne dener | Nasıl durur |
| --- | --- | --- |
| Bot | İmzasız, tekrar ya da kopya başvuru | EIP-712 imza ve `SIGNER_ROLE`; parti başına teklik izi ve özet tekliği |
| Bot | Sunucuyu boğmak | Parti başına üst sınır, IP başına sınır, dolu kuyrukta 503 |
| Randevu alıcısı | Satın aldığı randevuyla girmek | Tuzlu özet randevuyu pasaporta bağlar; kapıda pasaport numarası özeti tutturmalı |
| İşleten | Sonucu seçmek | Tohum açılışta mühürlü, entropi sonradan gelir, aynı tohum iki kez kullanılamaz |
| İşleten | Tohumu saklayıp kurayı yenilemek | Parti herkesin gözü önünde düşer; ürün sürümünde drand |
| İşleten | Başvuruyu sansürlemek | `register` herkese açık; imzalı makbuz başvuranın telefonunda |
| Blok üreticisi | Kapanış hash'ini etkilemek | Tohumu bilmediği için sonucu hedefleyemez |
| Sunucuyu ele geçiren | Sahte uygunluk ya da sahte giriş | Roller ayrık, yönetici anahtarı sunucuda değil, roller geri alınabilir |

**Kontratın değişmezleri.** Testler şu yedi özelliği kanıtlamalı:

1. Bir teklik izi bir partide en fazla bir kez kullanılır.
2. Bir özet bir partiye en fazla bir kez girer.
3. Kazanan sayısı `min(randevu, başvuru)`; sıralar 1…k ve benzersiz.
4. Kapanıştan sonra başvuru eklenmez; çekilişten sonra yalnızca kapı kaydı değişir.
5. Durum yalnızca ileri gider: Open → Drawn ya da Voided.
6. Kapı kaydı yalnızca kazanana ve bir kez yazılır.
7. Kontrat ETH tutmaz ve dış çağrı yapmaz.

**Kontrat nitelikleri**

| Nitelik | Uygulama | Ne zaman |
| --- | --- | --- |
| Rol ayrımı | OpenZeppelin `AccessControl`: `OPERATOR_ROLE` parti açar, `SIGNER_ROLE` uygunluk imzalar, `GATE_ROLE` kapı kaydı yazar. Yönetici anahtarı sunucuda durmaz | Bugün |
| İmza | `EIP712("Huzur", "1")` ve `ECDSA`: yüksek-s (değiştirilebilir) ve bozuk imzalar reddedilir; alanda `chainId` ve kontrat adresi, yapıda `batchId`; imzalayan `SIGNER_ROLE`'de olmalı | Bugün |
| Durum makinesi | Her fonksiyon parti durumunu ve blok aralığını özel hatayla kontrol eder | Bugün |
| Tekrar ve kopya | `usedNullifier`, `registered[id][commitment]`, `usedSeedHash` | Bugün |
| Sınırlı döngüler | `MAX_SLOTS`, `MAX_ENTRIES`, `MAX_BATCH`; çekiliş döngüsü en fazla `MAX_SLOTS` tur | Bugün |
| Zaman pencereleri | Açılışta en kısa ve en uzun süre; `fixEntropy` için 256 blok; `revealDeadline`; `voidBatch` yalnızca bu pencereler kaçınca | Bugün |
| Toplu başvuru | `registerBatch` geçersiz kaydı atlar ve `Rejected(id, nullifier, reason)` yayar; tek `register` geri döner | Bugün |
| Hash tanımları | `seedHash = keccak256(abi.encodePacked(seed))`; özet tanımı Kimlik bölümündeki gibi, üç dilde aynı | Bugün |
| Sade kontrat | `payable`, `receive` ve dış çağrı yok; yeniden giriş (reentrancy) yüzeyi yok | Bugün |
| Olaylar ve hatalar | Her durum değişikliği `batchId` indeksli olay yayar; özel hatalar (`NotOpen`, `RegistrationClosed` gibi); herkese açık fonksiyonlarda NatSpec | Bugün |
| Derleyici | Sabit `solc` sürümü, optimizer açık, `forge fmt` | Bugün |
| Yükseltilemez | Proxy yok: kurallar sonradan değiştirilemez, bu bir güven özelliği. Hata çıkarsa yeni sürüm dağıtılır | Bugün |
| Acil durum | Ayrı bir durdurma düğmesi yok: yeni parti açmayı durdurmak için `OPERATOR_ROLE` geri alınır; açık partiye kimse dokunamaz | Bugün |
| Ölçek | Seyrek Fisher-Yates: listeyi belleğe kopyalamadan yalnızca k okuma; sonuç aynı kalır, `MAX_ENTRIES` kalkar | Ürün sürümü |

**Test planı (Foundry)**

- *Birim:* her fonksiyonun doğru yolu ve her özel hata (`vm.expectRevert(Huzur.NotOpen.selector)`).
- *İmza:* yanlış imzalayan, başka parti, başka zincir (`vm.chainId`), başka kontrat, yüksek-s imza, tekrar gönderim.
- *Zaman:* `vm.roll` ile pencereler; entropi için `vm.setBlockhash(closeBlock, h)` (yalnızca son 256 blok için çalışır).
- *Fuzz:* rastgele tohum, entropi, başvuru ve randevu sayısı → kazananlar benzersiz, sayısı doğru, hepsi listede.
- *Test vektörleri:* özet ve kura (c4, c3, c2), Ön yüz bölümündeki gibi.
- *Ölçüm:* `forge test --gas-report` ile `MAX_ENTRIES` başvuruda `reveal` gas'ı.
- *Statik analiz:* `slither .`; yüksek ve orta bulgu kalmasın. Ardından Claude ile gözden geçirme.
- *Vakit kalırsa:* yukarıdaki yedi değişmez için handler'lı invariant testleri; `forge coverage` (hedef: satırların %90'ı).

**Dağıtım**

- Anahtar: `cast wallet import deployer --interactive` ile şifreli keystore; komutlarda `--account deployer`. Yönetici anahtarı kabuk geçmişine ve `.env`'ye girmez.
- `forge script script/Deploy.s.sol --rpc-url $RPC_URL --account deployer --broadcast`; roller dağıtım betiğinde sunucu adresine verilir.
- Kaynak kodunu Sourcify ile doğrulat (API anahtarı gerekmez): `forge verify-contract <adres> Huzur --chain 10143 --verifier sourcify --verifier-url https://sourcify-api-monad.blockvision.org/`. `foundry.toml`'a Monad belgesindeki ayarları ekle: `metadata_hash = "none"`, `use_literal_content = true`. Monadscan'de de görünsün istersen `agents.devnads.com` `/v1/verify` iki explorer'da birden doğrular. "Kodu herkes okuyabilir" iddiası ve "Monad'da dağıtıldı" geçidi böyle kanıtlanır.
- Kontratlar etkinlik süresi içinde dağıtılır (kural). Adresleri, dağıtım bloğunu, saatini ve commit hash'ini README'ye yaz.

**Backend nitelikleri**

| Alan | Uygulama | Ne zaman |
| --- | --- | --- |
| Ayarlar | Ortam değişkenleri (yerelde `.env`) `pydantic-settings` ile okunur; eksik ya da hatalı değer varsa sunucu açılmaz. Depoda yalnızca `.env.example` ve gizli değer içermeyen `render.yaml` durur | Bugün |
| En az yetki | Sunucu anahtarında yalnızca gereken roller var, yönetici anahtarı yok | Bugün |
| Tohum | `SEED_KEY`'den HMAC ile türetilir; diske yazılmaz, açıklanana kadar loglanmaz; sunucu yeniden başlasa da aynı tohum hesaplanır | Bugün |
| Kimlik doğrulama | `/admin/*` ve `/checkin` için `X-Admin-Token`; `hmac.compare_digest` ile sabit zamanlı karşılaştırma; token URL'de taşınmaz | Bugün |
| Girdi doğrulama | Pydantic modelleri, bilinmeyen alan reddi (`extra="forbid"`); pasaport no büyük harfe çevrilir, `<` atılır, `^[A-Z0-9]{1,9}$`; hex alanlar `^0x[0-9a-fA-F]{64}$`; parti gerçekten var olmalı | Bugün |
| Kötüye kullanım | Parti başına başvuru sınırı, dolu kuyrukta 503; `/eligibility` idempotent: aynı teklik izi tekrar gelirse yeni kayıt açılmaz, mevcut sonuç döner | Bugün |
| IP sınırı | `slowapi`, anahtar olarak Render'ın ilettiği istemci IP'si (`X-Forwarded-For`); salon tek IP'den çıkabildiği için geniş tutulur | Vakit kalırsa |
| Tek yazıcı | Bütün işlemler tek kuyruktan; nonce yerelde sayılır, "nonce too low" hatasında zincirden yeniden okunur | Bugün |
| Gas ve ücret | Gas tahmini + %20 pay, ücrete üst sınır. Monad ücreti gas limitinden kestiği için pay küçük tutulur | Bugün |
| Makbuz | Her işlemin makbuzu beklenir, `status` kontrol edilir; geri dönüşte özel hatanın adı loglanır | Bugün |
| RPC dayanıklılığı | Hatada üstel geri çekilme; okumalarda yedek RPC'ler; bütün dış çağrılarda zaman aşımı (RPC 5 sn, Claude 30 sn) | Bugün |
| İzleyici | Göndermeden önce zincirdeki durumu okur (entropi zaten sabitse göndermez); 256 blok penceresinin son 50 bloğunda uyarır | Bugün |
| Gizlilik | Pasaport numarası yalnızca başvuruda ve yalnızca bellekte; kapıda sunucuya yalnızca özet gelir; loglarda bu alanlar maskelenir; Claude'a yalnızca herkese açık sayılar gider | Bugün |
| Web | CORS yalnızca `WEB_ORIGINS` (Vercel üretim adresi, yerel geliştirme) ve isteğe bağlı `WEB_ORIGIN_REGEX` (önizlemeler); çerez yok; izinli başlıklar `Content-Type` ve `X-Admin-Token`; hata yanıtları genel, iz (stack trace) dönmez | Bugün |
| Güvenlik başlıkları | Vercel'de `web/vercel.json` ile: `Content-Security-Policy` (bağlantı yalnızca API'ye ve RPC'lere), `X-Content-Type-Options: nosniff`, `Referrer-Policy: no-referrer`, `Permissions-Policy: camera=(self)` | Vakit kalırsa |
| Açılış kontrolleri | Kontrat adresinde kod var mı, sunucunun rolleri tam mı, bakiye yeterli mi; eksikse sunucu açılmaz | Bugün |
| Gözlem | `/health` (RPC, son blok, bakiye, kuyruk uzunluğu, son işlem); Render'ın sağlık kontrolü bu ucu kullanır; JSON log ve istek kimliği | Bugün |
| Kalıcı durum | Bugün yok: her şey zincirden ve `SEED_KEY`'den yeniden kurulur. Ürün sürümünde kuyruk için veritabanı | Ürün sürümü |

**Backend kod kalitesi**

- Modüller: `config`, `chain` (istemci ve nonce), `eligibility`, `relayer`, `watcher`, `seeds`, `explain`, `api`.
- `ruff` ile lint ve biçim, tip ipuçları.
- `pytest`: teklik izi ayırıcısı, EIP-712 imzasının doğru adrese dönmesi, özet ve kura test vektörleri, tohum türetmenin aynı girdide aynı sonucu vermesi, token kontrolü, açıklamadaki sayı kontrolü.
- Vakit kalırsa `anvil` ile yerel uçtan uca test: kontrat ve sunucu birlikte, RPC sınırı olmadan.
- README: kök dizindeki iskelet doldurulur; içeriği Etkinlik kuralları bölümündeki teslim listesinde.

**Ürün sürümüne kalanlar:** seyrek Fisher-Yates, drand ile bağımsız rastgelelik, bağımsız güvenlik denetimi, anahtarların KMS ya da HSM'de tutulması, yönetici rolü için çok imzalı cüzdan (Safe), anahtar rotasyonu.

**Zaman etkisi.** Bugünkü maddeler mevcut dilimlere sığar; kontrat dilimi uzarsa Claude açıklamasından ve kapıdan kes. Teslimden önce, 15:50'de 10 dakikalık güvenlik turu: gizli değer depoda değil (`git ls-files`), roller doğru, loglarda kişisel veri yok, `ADMIN_TOKEN` perdede görünmüyor, kontrat kaynağı doğrulanmış.

## Gün planı ve kapsam

Saatler 24 Ekim'e göre; teslim 16:30. Her dilimin sonunda tek bir gözlem "bitti" demek; olmadıysa bir sonraki dilime geçmeden kapsamı kes. Bulut oturumu `web/` üzerinde paralel çalışır (`docs/calisma-duzeni.md`).

| Saat | İş | Bitti sayılır |
| --- | --- | --- |
| 11:20–11:40 | Hazırlık: blitz.devnads.com (token, takım, teslim formu), public repo ve ilk commit, Vercel ve Render hesapları, üç adrese MON, bulut ortamı | Repo herkese açık, ilk commit itildi |
| 11:40–12:30 | Kontratlar ve Foundry testleri, testnete dağıtım, kaynak doğrulama, `export-abi.sh` | Testler yeşil; iki adres explorer'da doğrulanmış |
| 12:30–13:30 | Sunucu: `/eligibility`, aktarıcı, izleyici, önbellek, `/batch`, `/admin/open`, `/health`, CORS; Render'a ilk dağıtım | Render adresinde `/health` yeşil; açılan bir parti zincirde çekildi |
| 11:40–13:30 (bulut) | `web/` iskeleti ve marka kiti, `/basvur` ve `/perde` sahneleri sahte veriyle, `draw.ts` ve test vektörü; Vercel bağlantısı | Vercel önizleme adresi telefonda açılıyor |
| 13:30–14:15 | Ekranları gerçek sunucuya ve zincire bağla; Vercel üretim adresi | 3 telefon Vercel adresinden başvurdu; perdede canlı kura |
| 14:15 | **Kontrol noktası** | Olmadıysa geri kalan her şeyi bırak ve bunu düzelt |
| 14:15–14:55 | Bot ve perdenin bot sahnesi | `IlkGelen` dolu, Huzur'da 0 kabul, 3 red explorer'da |
| 14:55–15:25 | `/dogrula` ve örnek parti (`make_cards.py`, `seed_morning.py`) | Üç kontrol yeşil; örnek partinin doğrulama bağlantısı hazır |
| 15:25–15:50 | Kapı: bilet QR'ı ve elle numara; vakit kalırsa Claude açıklaması | Doğru pasaport yeşil, başka pasaport kırmızı |
| 15:50–16:10 | Güvenlik turu, README'nin son hâli, teslim formu | Form 16:10'da gönderildi |
| 16:10–16:30 | Tampon | — |
| 16:30 | Teslim kapanır; kod donar, `main`'e push yok | — |
| 16:30'dan demoya | 90 saniyelik provalar, yedek video, sahneden önce sunucuyu uyandırma | Üç prova üst üste 90 saniyenin altında |

**Kapsam**

- *Olmazsa olmaz:* `Huzur.sol` ve doğrulanabilir çekiliş (kaynak kodu doğrulanmış), uygunluk imzası ve aktarıcı, canlı adreste `/basvur` ve perdede canlı kura, `IlkGelen` ile bot karşılaştırması, README.
- *Olmalı:* `/dogrula`, örnek parti, `/kapi` (bilet QR'ı ve elle numara).
- *Vakit kalırsa:* Claude ile kura açıklaması, kapıda tarayıcıda MRZ okuma, güvenlik başlıkları, passkey ile "bir cihaz, bir başvuru" (P-256), Claude ile soru-cevap, yedek liste, drand.

## Riskler ve önlemler

| Risk | Önlem |
| --- | --- |
| Teslim saati kaçar ya da son push canlıyı bozar | Formu 16:10'da gönder. Render ve Vercel `main`'e her push'ta yeniden dağıtır; 16:30'dan sonra push yok. Sahneden önce son sürümü kendi telefonunda dene |
| Render sunucuyu uyutur ya da yeniden başlatır; bellek ve disk gider | Tohum `SEED_KEY`'den türetilir; açık partiler, önbellek ve nonce açılışta zincirden kurulur. Sahneden 5 dakika önce perdeyi aç: yoklama sunucuyu uyanık tutar. Kart ekleyebiliyorsan `0.5c-512mb` örnek |
| 60 telefon aynı anda sunucuyu yoklar; ücretsiz örneğin CPU'su az | Ön yüz Vercel'in CDN'inden gelir; telefonlar 2 saniyede bir küçük bir önbellek yanıtı ister; aktarıcı toplu yazar. Gecikme görülürse paralı örneğe geç |
| `fixEntropy` 256 blok (\~77 sn) içinde çağrılmaz, parti düşer | İzleyici otomatik çağırır, perdede `E` kısayolu var. Düşerse yeni parti açmak 30 saniye sürer; provada bir kez dene |
| Herkese açık RPC sınırı (50 rps, `eth_call` için 25 rps) | Telefonlar sunucuyu yoklar, aktarıcı toplu yazar, bot denemeleri multicall paketinde, Doğrula üç RPC'ye dağılır |
| `eth_sendRawTransactionSync` testnette yok ya da zaman aşımına uğrar | Normal gönderim ve makbuz yoklamasına düşer; ilk dağıtımdan sonra bir kez dene |
| Aynı anahtardan iki görev işlem gönderir, nonce çakışır | Aktarıcı ve izleyici tek kilitli kuyruktan yazar; bot ayrı anahtar kullanır |
| Başvuru sayısı randevuyu geçmez, herkes kazanır ve kura anlamsızlaşır | Randevu sayısını açılışta salona göre seç (beklenen başvurunun dörtte biri kadar) |
| Aynı kişi sayfayı yenileyip tekrar başvurur | Kart cihazda hatırlanır, sunucu parti başına üst sınır koyar (ör. 300). Demoda kimlik onayının sahte olduğunu kendin söyle |
| Kapı kamerası bilet QR'ını okumaz | Bilet tam ekran ve parlak gösterilir; kapı sayfası Vercel'in HTTPS adresinden açılır; kamera iznini provada ver |
| Salon interneti zayıf | Laptop için telefon hotspot'u; seyirci mobil veriyle de bağlanabilir |
| Aktarıcının MON'u biter | Blitz token ve faucet'ten önceden al, `/health` bakiyeyi gösterir; gas limitini tahminle ver, Monad ücreti limitten keser |
| Monad testnet yavaşlar ya da durur | Teslimden sonra çekilmiş yedek video; sahnede beklemek yerine videoya geç |
| Gizli değer public repoya girer | `.gitignore` ve her push öncesi `git ls-files` kontrolü. Girerse anahtarı hemen değiştir; geçmişten silmek yetmez |
| Jüride Türkçe bilmeyen var | README İngilizce; perdede kısa İngilizce alt satır; konuşma dilini organizatörle netleştir |
| Claude yanıt vermez ya da açıklamaya verilmemiş bir sayı yazar | Açıklama parti başına bir kez üretilir; metinde verilmemiş bir sayı varsa atılır; hata olursa açıklama gizlenir, doğrulama aynen çalışır |

## Başlamadan önce

- [ ] blitz.devnads.com: token al, takımı kur, teslim formunun alanlarına bak (video isteniyor mu?).
- [ ] Info pack'teki track ve bounty listesine bak.
- [ ] Organizatöre sor: demo sırası, sahnede kurulum süresi, jüride Türkçe bilmeyen var mı.
- [ ] GitHub'da herkese açık repo; ilk commit bu paket: "Etkinlik öncesi hazırlık: plan ve araç ayarları, uygulama kodu yok".
- [ ] Vercel ve Render hesapları GitHub ile bağlı.
- [ ] Sunucu ve bot anahtarı yalnızca testnet için; yönetici anahtarı keystore'da (`cast wallet import deployer --interactive`). Üçüne MON: blitz token, `agents.devnads.com` faucet ya da faucet.monad.xyz.
- [ ] `HMAC_KEY`, `SEED_KEY` ve `ADMIN_TOKEN`: `openssl rand -hex 32`.
- [ ] Foundry, Node 22, Python 3.11+ ve Slither (`pip install slither-analyzer`) kurulu.
- [ ] Laptop için telefon hotspot'u. Sahne düzeni: laptop perdeye bağlı, kapı telefonu elde, demo kartları basılı ya da tablette.

## Kaynaklar

- [Monad testnet ağ bilgileri: RPC uçları, hız sınırları, kanonik kontratlar](https://docs.monad.xyz/developer-essentials/testnets)
- [Monad güncel değerler: blok süresi, kesinlik, gas sınırları](https://docs.monad.xyz/ai/current-facts.md)
- [Monad JSON-RPC: eth_sendRawTransaction ve eth_sendRawTransactionSync](https://docs.monad.xyz/reference/json-rpc/eth_sendRawTransaction)
- [Monad ön derlemeleri (P-256)](https://docs.monad.xyz/developer-essentials/precompiles)
- [Render: ücretsiz örneğin sınırları](https://render.com/docs/free), [Blueprint (render.yaml)](https://render.com/docs/blueprint-spec) ve [fiyatlar](https://render.com/pricing)
- [Vercel: Vite projeleri](https://vercel.com/docs/frameworks/frontend/vite)
- [Foundry](https://getfoundry.sh/)
- [OpenZeppelin EIP712.sol](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/utils/cryptography/EIP712.sol) ve [EIP-712](https://eips.ethereum.org/EIPS/eip-712)
- [Multicall3](https://github.com/mds1/multicall3)
- [viem: fallback taşıyıcısı](https://viem.sh/docs/clients/transports/fallback)
- [qr-scanner](https://github.com/nimiq/qr-scanner) ve [qrcode](https://www.npmjs.com/package/qrcode)
- Vakit kalırsa: [tesseract.js](https://github.com/naptha/tesseract.js) ve [mrz](https://www.npmjs.com/package/mrz)
- [base/webauthn-sol](https://github.com/base/webauthn-sol)
- [drand](https://drand.love/)
- [Claude: yapılandırılmış çıktılar](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)
- [Claude: effort parametresi](https://platform.claude.com/docs/en/build-with-claude/effort)
- [Claude modelleri](https://platform.claude.com/docs/en/models/overview)
