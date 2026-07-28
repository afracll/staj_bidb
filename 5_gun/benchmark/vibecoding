## BENCHMARK VERİLERİ VE YAPAY ZEKA REKABETİ

### Model ve Araç Katmanları

Araçlar üç temel kategoride ele alıdnı:
1. Model Katmanı: Modellerin doğrudan mantık ve kodlama yeteneklerini ölçen bağımsız testler (LMSYS Chatbot Arena, SWE-bench Verified).
2. IDE ve CLI Agent'ları: Doğrudan kod tabanına entegre çalışan ve projeyi indeksleyen araçlar (Cursor, Claude Code, GitHub Copilot).
3. Genel Chat Arayüzleri: Kod bloklarını sorgulama, mantık yürütme ve algoritma kurgulama araçları (ChatGPT, Gemini Web).

### Bağımsız Benchmark Metrikleri
İncelediğim temel performans göstergeleri şunlardır:
* LMSYS Chatbot Arena (Coding): Modellerin yazılımcılar tarafından kör test (blind-test) yöntemiyle oylatıldığı, insan tercihine dayalı Elo sıralama sistemidir.
* SWE-bench Verified: Gerçek GitHub depolarındaki karmaşık hataları yapay zekanın tek başına çözebilme başarı oranını (% Resolved Rate) ölçer.
* Artificial Analysis Coding Index: Görev tamamlama süresi (Time per Task) ve API maliyetlerini genel olarak değerlendiren bir indekstir.

### Güncel Sayısal Benchmark Karşılaştırma Tablosu
Kaynaklar: LMSYS Org, SWE-bench Verified ve Artificial Analysis Güncel Tabloları

| Araç / Model Katmanı | Çalışma Arayüzü | SWE-bench Verified Başarı Oranı (%) | Görev Başına Ortalama Maliyet ($) | Tamamlama Hızı | Öne Çıkan Güçlü Yönü |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Claude Opus (4.5/5) | Claude Code (CLI) / Cursor | %76.80 | $0.75 - $11.70 | Derin Düşünme Süresi | Karmaşık mimari kurgulama ve kapsamlı refactoring işlemleri. |
| Gemini Flash/Pro | Gemini CLI / Web Chat | %75.80 | $0.36 | Hızlı (10.8 dk) | Geniş kod tabanlarını okuma ve düşük maliyetli hızlı çözümler. |
| GPT-4o / Codex | ChatGPT Web / Copilot | %72.80 | $0.45 - $8.23 | Dengeli (10.2 dk) | Yaygın kod tamamlama uyumu, geniş kütüphane bilgisi ve genel problem çözümü. |
| ChatGPT (o3-mini) | OpenAI Web Interface | Modeli / Agent Yapısı | Abonelik ($20/ay) veya API | Anlık (Reasoning) | Adım adım mantık yürütme, algoritma ve mülakat soruları çözümü. |
| Cursor CLI (Composer) | Cursor IDE | Agentik Başarı Oranı | $0.55 | 6.8 dakika | IDE içi anlık otomatik tamamlama, hızlı proje indeksleme ve arayüz geliştirme. |

### Vibe Coding Araçlarının Mimarileri ve Özellik Kıyaslaması

#### Kod Tabanı Bağlamı Yönetimi (Context & Indexing)
* Cursor: Projeyi yerel vektör veri tabanında indeksler. `.cursor/rules` dizini altındaki kurallarla projeye özel mimari standartları yapay zekaya öğretir.
* Claude Code (CLI): `CLAUDE.md` dosyası üzerinden proje bağlamını okur. İndeksleme yapmak yerine doğrudan terminal içi dizin ve dosya taraması gerçekleştirir.
* Gemini: 2 Milyon+ Token'lık geniş bağlam penceresi (Context Window) sayesinde büyük kod dosyalarını veya tüm repoyu indekslemeye gerek duymadan tek seferde belleğe alabilir.
* ChatGPT Web: Proje bağlamı sohbet penceresine yüklenen dosyalar ve özel talimatlar (Custom Instructions) ile sınırlıdır. Projeyi canlı olarak indeksleme özelliği yoktur.
* GitHub Copilot: Depo seviyesindeki özel talimatları ve GitHub kütüphane bağlamını kullanarak koddaki yapıyı sorgular.

#### Kod Tahminleme (Autocomplete)
* Cursor (Predictive Tab): Yazılımcı henüz tuşa basmadan veya kodu yazarken sonraki birkaç satırı ve olası değişiklikleri anlık olarak öngörür.
* GitHub Copilot: Sektörde yaygın olan satır içi (inline) kod tamamlama sunar; ancak çoklu dosya seviyesinde canlı tahminleme Cursor kadar anlık değildir.
* Claude Code, ChatGPT & Gemini Web: IDE eklentisi olmadıkları için canlı yazım esnasında otomatik tamamlama sunmazlar, tamamen komut ve görev tabanlı çalışırlar.

#### Otonom Çalışma ve Git Disiplini
* Claude Code: Terminal üzerinde otonom bir döngüde (Gather -> Act -> Verify) çalışır. Başarılı her adımdan sonra otomatik Git commit'leri atarak versiyon kontrolünü korur.
* Cursor: Çoklu dosya düzenleme yeteneği (Composer) ile dosyalar arasındaki değişiklikleri görsel olarak sunar. Bulut agent'ları sayesinde GitHub issue'larından otomatik PR taslağı üretebilir.
* GitHub Copilot: GitHub Actions ve PR botları ile CI/CD süreçlerine entegre olarak otomatik kod incelemesi yapar.
* ChatGPT & Gemini Web: Kod değişikliklerini doğrudan proje dosyalarına yazamaz veya Git commit atamazlar. Kodun geliştirici tarafından kopyalanıp projeye elle yapıştırılması gerekir.
