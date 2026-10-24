# Huzur: marka kiti

Arayüzü yazan herkes (insan ya da Claude) bu dosyaya uyar. Sunumdaki öneri: "Vibe-coded UI gönderme; LLM'e marka kiti ver: yazı tipi, renk, bileşen." Hazır şablon görünümü (indigo düğmeler, gradyanlı kahraman alanı, her yerde büyük gölge, emoji) kullanılmaz.

## Yön

**Noter onaylı kura.** Resmî kâğıt, mürekkep ve mühür; delikli bir bilet. Güven veren, sakin, okunaklı. Heyecan yalnızca kura anında: kazanan kodlar tek tek düşer, mühür basılır.

- Telefon ekranları açık: kâğıt zemin, mürekkep yazı, bordo vurgu (Türk pasaportunun rengi).
- Perde koyu: mürekkep zemin, kâğıt yazı, kehribar vurgu (rakamlar ve kodlar).
- Her ekranda tek vurgu rengi ve tek birincil düğme.

## Tokenlar

`web/src/styles/tokens.css` olarak aynen kullan. Bileşenler yalnızca anlamsal tokenları (`--bg`, `--fg`, `--accent` ...) kullanır.

```css
:root {
  /* Telefon teması (varsayılan) */
  --bg: #F3EFE6;        /* kâğıt */
  --card: #FFFDF8;
  --fg: #14161C;        /* mürekkep */
  --muted: #6B6455;
  --line: #D9D2C3;
  --accent: #7A1E2E;    /* bordo: birincil düğme, başlık vurgusu */
  --accent-press: #64182A;
  --on-accent: #FFFDF8;
  --ok: #1D7A4C;        /* kazandın, doğrulandı */
  --bad: #B3261E;       /* reddedildi, başka pasaport */
  --monad: #6E54FF;     /* yalnızca "Monad testnet" etiketi */

  --font-sans: "IBM Plex Sans", system-ui, sans-serif;
  --font-mono: "IBM Plex Mono", ui-monospace, monospace;

  --r-card: 12px;
  --r-btn: 14px;
  --shadow-card: 0 1px 0 rgb(20 22 28 / 6%), 0 8px 24px rgb(20 22 28 / 8%);
  --ease: cubic-bezier(.2, .7, .2, 1);
}

.perde {
  /* Perde teması: koyu, projeksiyonda yüksek karşıtlık */
  --bg: #14161C;
  --card: #1C1F27;
  --fg: #F3EFE6;
  --muted: #A7A196;
  --line: #2A2D36;
  --accent: #F2B544;    /* kehribar: sayaçlar, kodlar, kazananlar */
  --on-accent: #14161C;
  --ok: #3FB984;
  --bad: #F0644F;
}
```

Karşıtlık denetlendi: mürekkep/kâğıt yaklaşık 16:1, bordo üstünde açık yazı yaklaşık 10:1, perdede kehribar/mürekkep yaklaşık 10:1, yeşil ve kırmızı iki temada da 4,5:1'in üstünde.

## Yazı tipi

- **IBM Plex Sans** (400, 500, 600, 700): bütün metin. Türkçe karakterlerin hepsi var.
- **IBM Plex Mono** (500, 600): bilet kodu, blok numarası, kısaltılmış hash, sayaçlar. Rakamlar `font-variant-numeric: tabular-nums`.
- Paketler: `@fontsource/ibm-plex-sans` ve `@fontsource/ibm-plex-mono` (npm; dış font sunucusu yok).

| Kullanım | Telefon | Perde |
| --- | --- | --- |
| Sonuç başlığı | 40/44, 700 | 96/104, 700 |
| Başlık | 28/34, 700 | 72/80, 700 |
| Gövde | 17/26, 400 | 36/48, 500 |
| Küçük | 14/20, 500, `--muted` | en az 28 px |
| Bilet kodu | Mono 44, 600, harf aralığı 0.08em | Mono 32 (ızgarada) |
| Sayaç | Mono 56, 600 | Mono 200, 600 |

Aralık ölçeği 4'ün katları: 4, 8, 12, 16, 24, 32, 48, 64, 96.

## Bileşenler

`web/src/components/` altında, her biri kendi CSS modülüyle.

- **Bilet (`Ticket`).** `--card` zeminli kart, köşe 12 px, `--shadow-card`. Sol kenardan 24 px içeride kesik çizgi (2 px dashed `--line`), üst ve alt kenarda bu çizginin hizasında 10 px yarım daire çentik. Üstte küçük "huzur" yazısı ve "PARTİ #7" (mono, `--muted`). Ortada 6 haneli kod (özetin ilk 6 hanesi, büyük harf). Altta durum satırı: nokta ve "Zincirde", işlem bağlantısı (↗). Kapı için QR "Kapıda göster" açılır alanında. Durumlar: Bekliyor (gri nokta, yavaş nabız), Zincirde (yeşil nokta), Kazandın (2 px `--ok` çerçeve ve Mühür), Çıkmadı (sakin gri metin, dram yok).
- **Mühür (`Stamp`).** Yuvarlatılmış dikdörtgen, -6° dönük, çift çerçeve (3 px ve 1 px), büyük harf, 600, harf aralığı 0.12em. Renk `--ok` (KAZANDIN · SIRA 3, DOĞRULANDI) ya da `--bad` (REDDEDİLDİ). Belirirken ölçek 1.15 → 1 ve opaklık 0 → 1, 220 ms.
- **Düğme (`Button`).** Yükseklik 56 px, köşe 14 px, telefonda tam genişlik ve ekranın altına sabit. Birincil: `--accent` zemin, `--on-accent` yazı; basılıyken `--accent-press`; pasifken %40 opaklık; yüklenirken küçük döner simge ve "Gönderiliyor…". İkincil: saydam zemin, 1.5 px `--fg` çerçeve.
- **Sayaç (`Counter`).** Mono rakamlar, üstünde küçük büyük harfli etiket (`--muted`). Artışta rakamlar kısa bir sayımla değişir.
- **Geri sayım (`Countdown`).** 6 px ince ilerleme çubuğu (`--accent`) ve mono saniye. Son 10 saniyede çubuk `--bad` olur.
- **Yarış paneli (`RacePanel`, perde).** İki eşit sütun, arada ince çizgi. Solda "İlk gelen alır": 5×4 randevu ızgarası; her kutu dolunca `--bad` zemin ve "BOT"; altında "20/20 · 0,8 sn · 3 blok". Sağda "Huzur": büyük sayaç "1.000 deneme", altında `--ok` renkte "0 kabul"; dipnot: "Kontrata karşı simülasyon · 3 gerçek işlem reddedildi ↗".
- **Kod ızgarası (`CodeGrid`, perde).** Gelen bilet kodları mono çipler hâlinde belirir (opaklık 0 → 1, 150 ms). Kurada kazananlar sırayla `--accent` zemine geçer ve sıra numarası alır, 300 ms arayla.
- **Kontrol satırı (`CheckRow`).** 32 px yuvarlak simge (✓ `--ok`, ✗ `--bad`, bekleme için üç nokta), metin ve sağda mono kısaltılmış değer (`0x1a2b…9f0e`).
- **Monad etiketi.** Her ekranın dibinde küçük çip: `--monad` zemin, açık yazı, "Monad testnet"; explorer bağlantıları da bu renkte.

## Yerleşim

- **Telefon:** en fazla 440 px genişlik, ortalı, 20 px kenar boşluğu, güvenli alan payları. Birincil düğme altta sabit.
- **Perde:** 1920×1080 tuval, ekrana `transform: scale()` ile sığdırılır; her projektörde aynı görünür. 96 px kenar boşluğu. Bir sahnede en fazla bir başlık ve bir ana öğe.

## Hareket

- Süreler 150–250 ms, `--ease`. Kazananlar 300 ms arayla. Sayaçlar `requestAnimationFrame` ile.
- `prefers-reduced-motion: reduce` ise animasyon yok, durum doğrudan gösterilir.

## Dil

- Kısa, resmî ama sıcak: "Başvurun alındı", "Zincirde", "Kazandın · Sıra 3", "Bu partide çıkmadı".
- Sayılar Türkçe biçimde: 1.000; 0,6 sn.
- Telefonda teknik sözcük yok: "hash" yerine "mühür", "blok" yerine "kapanış anı". Perdede ve `/dogrula`'da teknik ayrıntı küçük mono yazıyla durabilir.
- Emoji yok. Hash'ler her zaman kısaltılmış.

## Yapma

- Varsayılan Tailwind görünümü, indigo ya da mor gradyan, cam efekti.
- Bir ekranda birden fazla vurgu rengi ya da birincil düğme.
- Cüzdan bağlama düğmesi.
- Uzun hash'i olduğu gibi yazmak.
