# Huzur: ürün özeti

Perde sahneleri ve README için kısa özet. Tam ürün hikâyesi claude.ai'deki "Huzur: Ürün Hikâyesi" dokümanında.

**Slogan:** "Randevu hıza değil, kuraya göre." İkinci satır: "Kura, herkesin huzurunda."

**Ad:** Türkiye'de adil kura "noter huzurunda" çekilir; Huzur'da noterin yerini zincir alır ve kura herkesin huzurunda çekilir. Kelime ayrıca gece yarısı sayfa yenileme telaşının bittiğini anlatır.

**Tek cümle:** Huzur, kıt randevuları "ilk gelen alır" yerine herkesin doğrulayabildiği bir kurayla dağıtır ve kazanılan randevuyu kişinin pasaportuna bağlar. Bot hızı bir şey kazandırmaz, randevu satılamaz.

## 90 saniyelik canlı demo

Kural: demo 90 saniye ve canlı; slayt şart değil. Sunumdaki öneri: problemi tek nefeste söyle, sonra demoya geç; formlar dolu, demo kurulu olsun. Başvuru penceresi 45 saniye: `A` ile 0:00'da açılır, yaklaşık 0:40'ta kapanır.

| Süre | Perdede ne olur | Söylenen |
| --- | --- | --- |
| 0:00–0:10 | `A`: parti açılır. Büyük QR ve "Başvuru açık · 45 sn" geri sayımı | "Vize randevuları saniyeler içinde botlara gidiyor ve 400 euroya satılıyor; geçen hafta 60 kişi için gözaltı kararı çıktı. Telefonunuzu çıkarın, QR'ı okutun: tek dokunuşla başvurun." |
| 0:10–0:35 | `B`: bot yarışı, QR'ın yanında. Solda "İlk gelen alır": 20 randevu ilk bloklarda bota gider. Sağda Huzur: 1.000 deneme, 0 kabul. Altta salonun başvuru sayacı yükselir | "Bugünkü sistemde bot hepsini aldı. Huzur'da hız işe yaramıyor: onaysız başvuru zincirde reddediliyor ve bir pasaport bir kez giriyor." |
| 0:35–0:55 | Kapandı → mühür açıldı → kazanan kodlar tek tek düşer; telefonlarda "Kazandın" ya da "Bu partide çıkmadı". Varsa altında Claude'un tek cümlesi | "Başvuru kapandı. Sonucu belirleyen sayı açılışta mühürlendi, kapanış anı zincirden geldi. Kazananlar telefonunuzda." |
| 0:55–1:10 | Doğrula sahnesi: üç yeşil kontrol ve `/dogrula` QR'ı | "Bunu biz değil, telefonunuz doğruluyor: sunucumuza sormadan, zincirden yeniden çekiyor. Kurayı işleten bile sonucu seçemez. Zincirde pasaport numarası yok; kazanan randevu kapıda pasaportla eşleşiyor." |
| 1:10–1:30 | Tek satır iş modeli ve slogan | "Randevuyu dağıtan firma başvuru başına öder, başvuran karaborsaya para vermez. Aynı motor hac kurası, TOKİ ve derbi bileti için de çalışır. Demoda kimlik onayı sahte; gerisi Monad testnetinde canlı. Randevu hıza değil, kuraya göre." |

Prova notları:

- Kronometreyle üç kez üst üste 90 saniyenin altına in.
- Bot sahnesindeki etiket dürüst: "1.000 deneme (kontrata karşı simülasyon) · 3 gerçek işlem, zincirde reddedildi". Konuşmada "bin denemenin hiçbiri geçmedi" de; "bin işlem" deme.
- Sahneye çıkmadan 5 dakika önce perdeyi aç: yoklama sunucuyu uyanık tutar. `ADMIN_TOKEN` perdeye önceden girilir ve hiç görünmez.
- Jüride Türkçe bilmeyen varsa perdede kısa İngilizce alt satır kullan ya da konuşmayı İngilizce yap.
- Kapı demosu 90 saniyeye girmez. Jüri sorarsa örnek partinin kazanan ve "satın alan" kartıyla kapıyı göster.

## Jüri ölçütleri ve vurgular

| Ölçüt (ağırlık) | Vurgu |
| --- | --- |
| Çalışırlık (%24) | Her şey canlı: kontrat, aktarıcı, bot, kura. Sahte olan tek şey kimlik onayı ve bunu söylüyoruz |
| Zincir gerekliliği · Monad uyumu (%20) | Zincir olmadan kura "bize güvenin" olurdu. Zincirde para dolaşmıyor; zincir sonucun doğruluğu için var. Randevu açılışı bir NFT mint'i gibi trafik patlaması; Monad bunun için yapıldı |
| Salon oyu (%20) | Salon kuraya kendisi katılıyor; kazananlar sonucu kendi telefonunda görüyor |
| Problem ve vaat (%16) | Net kullanıcı ve müşteri; başvuru başına ücret; hac, TOKİ, derbi |
| Özgünlük (%12) | Botu yakalamak değil, bot olmayı anlamsız kılmak |
| Sunum (%8) | 90 saniye, kurulu demo, eksikler tek cümleyle |

## İş modeli

Huzur bir B2B yazılım hizmeti: randevuyu ya da bileti dağıtan kurum öder, başvuran ücretsiz başvurur. Ödeme bugünkü kanallardan TL ile yapılır; zincirde para dolaşmaz.

- **Başvuran:** karaborsaya (300–500 euro) ve aracıya para ödemez; gelemezse randevusunu iade eder, hizmet bedeli geri döner.
- **Randevuyu dağıtan firma:** bot trafiğinin şişirdiği sunucu maliyeti ve şikâyet yükü düşer, sözleşme kaybı riski azalır, iade edilen randevu yedeğe geçer.
- **Huzur:** başvuru başına küçük bir ücret; denetim raporu ve "doğrulanabilir kura" rozeti.

## Kaynaklar

- [Euronews: Vize danışmanlık şirketlerine bot operasyonu (20 Ekim 2026)](https://tr.euronews.com/2026/10/20/vize-danismanlik-sirketlerine-bot-operasyonu-60-kisi-icin-gozalti-karari)
- [Euronews: Türklerin Schengen tercihi ve ret oranları (29 Ağustos 2026)](https://tr.euronews.com/2026/08/29/turklerin-schengen-tercihi-en-cok-basvurulan-ulkeler-ve-ret-oranlari)
- [Gazete Oksijen: Lighthouse Reports VFS Global dosyası](https://gazeteoksijen.com/dunya/uluslararasi-arastirmaci-gazetecilik-agindan-vfs-global-dosyasi-vize-almak-isteyenler-nasil-ek-ucret-odemeye-zorlandi-277221)
- [Vize Kodu (AB 810/2009), madde 9](https://www.legislation.gov.uk/eur/2009/810/article/9)
- [Mondaq: Polonya'da kurayla vize randevusu (2024)](https://webiis08.mondaq.com/work-visas/1504086/lottery-visa-appointment-system-in-effect-for-nationals-of-certain-countries)
