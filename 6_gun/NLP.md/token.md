# Token Nedir?

## Token Tanımı

**Token**, bir yapay zekâ modelinin metni işlerken kullandığı temel metin parçasıdır. İnsanlar bir cümleyi çoğunlukla kelimeler üzerinden okur; dil modelleri ise metni token adı verilen parçalara ayırarak işler.

Bir token:

- Bir kelimenin tamamı,
- Kelimenin bir bölümü,
- Bir harf veya karakter,
- Noktalama işareti,
- Sayı,
- Boşlukla birlikte bir metin parçası

olabilir. Bu nedenle **bir token her zaman bir kelimeye eşit değildir**. Aynı kelime bazı modellerde tek token olurken başka bir modelde birkaç tokene ayrılabilir.

Token, doğrudan “anlam taşıyan en küçük dil birimi” olarak düşünülmemelidir. Daha doğru tanımla token, modelin kullandığı tokenizer tarafından belirlenen işlem birimidir. Bazı tokenlar tek başına anlamlı olabilirken bazıları yalnızca bir kelimenin parçasıdır.

## Tokenization Nedir?

**Tokenization**, bir metnin tokenlara ayrılması işlemidir. Bu işlemi yapan bileşene **tokenizer** denir. Tokenizer, metni modelin önceden belirlenmiş token sözlüğüne göre parçalara ayırır.

Örneğin bir tokenizer İngilizcedeki `tokenization` kelimesini şöyle bölebilir:

```text
token + ization
```

Bir insan bunu tek kelime olarak görürken model iki token olarak işleyebilir. Böylece modelin sözlüğünde bütün kelimelerin ayrı ayrı bulunması gerekmez. Model, daha önce az gördüğü veya hiç görmediği bir kelimeyi bildiği alt parçalara ayırarak işleyebilir.

Türkçe eklemeli bir dil olduğu için kelimeler çok sayıda ek alabilir. Örneğin `evlerimizden` kelimesi kullanılan tokenizera göre şu tür parçalara ayrılabilir:

```text
ev + ler + imiz + den
```

Bu yalnızca açıklayıcı bir örnektir; gerçek bölünme kullanılan modelin tokenizerına göre farklı olabilir.

## Token, Token ID ve Embedding Arasındaki Fark

Dil modelleri metni doğrudan matematiksel olarak işleyemez. Bu nedenle tokenization sonrasında her token, modelin sözlüğündeki bir **token ID** ile eşleştirilir.

Örnek olarak:

```text
"Bugün hava güzel"
        ↓ Tokenization
["Bugün", " hava", " güzel"]
        ↓ Token ID'leri
[4217, 1832, 9056]
```

Buradaki sayılar yalnızca örnektir. Her modelin tokenizerı ve token sözlüğü farklı olduğundan gerçek ID değerleri de değişir.

Token ID ile embedding aynı şey değildir:

- **Token:** Metnin tokenizer tarafından oluşturulan parçasıdır.
- **Token ID:** Bu parçanın modelin sözlüğündeki sayısal kimliğidir.
- **Embedding:** Token ID kullanılarak ulaşılan, modelin öğrenebileceği çok boyutlu sayısal vektördür.

Yani model önce metni tokenlara ayırır, tokenları ID’lere çevirir ve daha sonra bu ID’leri embedding vektörleriyle temsil eder. Sinir ağı asıl hesaplamalarını bu vektörler üzerinde gerçekleştirir.

## Tokenization Türleri

### Kelime Tabanlı Tokenization

Metni kelimelere ayırır. Anlaşılması kolaydır ancak bütün kelimeleri sözlükte tutmak gerekir. Kelimelerin ek almış biçimleri, yazım hataları ve yeni kelimeler sözlüğü çok büyütebilir.

### Karakter Tabanlı Tokenization

Metni tek tek karakterlere ayırır. Bilinmeyen kelime sorunu azalır fakat token dizileri çok uzar. Uzun diziler daha fazla işlem ve bellek gerektirebilir.

### Alt Kelime Tabanlı Tokenization

Kelime ve karakter yöntemleri arasında denge kurar. Sık kullanılan kelimeleri bütün olarak, daha az görülen kelimeleri ise daha küçük parçalara ayırabilir. BPE, WordPiece ve Unigram gibi yöntemler bu yaklaşımın örnekleridir. Modern büyük dil modellerinde çoğunlukla alt kelime veya byte tabanlı tokenization yöntemleri kullanılır.

## Yapay Zekâ Modelleri Neden Token Kullanır?

### Sözlük Boyutunu Yönetmek

Bir dildeki bütün kelimeleri, ekleri, özel isimleri, argo ifadeleri ve yazım hatalarını ayrı ayrı sözlüğe eklemek mümkün değildir. Alt kelime tokenları sayesinde sınırlı bir token sözlüğü kullanılarak çok sayıda farklı kelime oluşturulabilir.

### Bilinmeyen Kelimeleri İşlemek

Model daha önce görmediği bir kelimeyi bildiği parçalara ayırabilir. Böylece her yeni kelime için ayrı bir sözlük kaydına ihtiyaç duymaz.

### Hesaplamayı Daha Verimli Hâle Getirmek

Metni yalnızca karakterlere ayırmak çok uzun diziler üretir. Yalnızca tam kelimeleri kullanmak ise çok büyük bir sözlük gerektirir. Alt kelime tokenları bu iki yöntem arasında daha kullanışlı bir denge sağlar.

### Dildeki Örüntüleri Öğrenmek

Model, tokenların hangi sıralarla birlikte kullanıldığını eğitim verilerinden öğrenir. Böylece cümle yapıları, kelimeler arasındaki ilişkiler ve bağlama göre değişen anlamlar hakkında örüntüler oluşturabilir.

## Büyük Dil Modelleri Tokenlarla Nasıl Metin Üretir?

Bir kullanıcı modele soru gönderdiğinde genel olarak şu süreç gerçekleşir:

1. Kullanıcının metni tokenizer tarafından tokenlara ayrılır.
2. Tokenlar token ID’lerine dönüştürülür.
3. ID’ler embedding vektörleriyle temsil edilir.
4. Transformer modeli tokenlar arasındaki ilişkileri işler.
5. Model sıradaki token için olasılık değerleri üretir.
6. Seçilen token diziye eklenir ve işlem tekrarlanır.
7. Üretilen tokenlar tekrar okunabilir metne dönüştürülür.

Bu nedenle büyük dil modelleri bir cevabı genellikle token token üretir. Ekranda cevabın parça parça görünmesinin nedenlerinden biri budur.

Modelin yalnızca “en olası kelimeyi” seçtiğini söylemek tam olarak doğru değildir; tahmin bir sonraki **token** için yapılır. Seçim sürecinde sıcaklık gibi ayarlara bağlı olarak en yüksek olasılıklı token veya olasılığı yüksek tokenlardan biri seçilebilir.

## Token ile Kelime ve Karakter Arasındaki Fark

| Birim | Açıklama | Örnek |
| --- | --- | --- |
| Kelime | İnsan dilinde anlamlı kabul edilen dil birimi | `kitaplarımız` |
| Karakter | Tek bir harf, sayı veya sembol | `k`, `7`, `?` |
| Token | Tokenizerın modele göre oluşturduğu işlem parçası | `kitap` + `larımız` olabilir |

Aynı kelime sayısına sahip iki cümlenin token sayısı farklı olabilir. Noktalama işaretleri, boşluklar, sayılar, emojiler, kullanılan dil ve kelimelerin ne kadar yaygın olduğu token sayısını etkileyebilir. Bu nedenle “bir token kesin olarak şu kadar kelimedir” şeklinde evrensel bir oran yoktur.

## Token Sözlüğü ve Özel Tokenlar

Her modelin kullanabildiği tokenların bulunduğu bir **vocabulary**, yani token sözlüğü vardır. Tokenizer, metni bu sözlükteki parçalara dönüştürür.

Bazı modeller normal metin tokenlarının yanında özel tokenlar da kullanır. Bu tokenlar:

- Metnin başlangıcını veya sonunu,
- Cümleler arasındaki ayrımı,
- Doldurma yapılan boş alanları,
- Sistem, kullanıcı ve asistan mesajlarının sınırlarını

gösterebilir. Özel tokenların türü ve görevi model mimarisine göre değişir.

## Context Window ve Token Limiti

Bir dil modelinin tek seferde işleyebildiği token sayısına **context window**, yani bağlam penceresi denir. Bu pencereye genel olarak sistem talimatları, kullanıcının mesajları, konuşma geçmişi ve üretilen cevap için kullanılan tokenlar dâhil olabilir. Kesin kullanım biçimi modele ve uygulamaya göre değişir.

Konuşma veya belge context window sınırını aşarsa bütün içerik aynı anda modele verilemez. Uygulama eski mesajların bir kısmını çıkarabilir, özetleyebilir veya metni farklı parçalara ayırabilir. Bu nedenle çok uzun konuşmalarda model ilk bölümlerdeki bazı ayrıntıları dikkate alamayabilir.

Token sınırı şu konuları etkiler:

- Modele verilebilecek belge uzunluğunu,
- Modelin aynı anda kullanabileceği konuşma geçmişini,
- Üretilebilecek cevabın uzunluğunu,
- Bellek ve hesaplama ihtiyacını.

## Tokenların Maliyet ve Hıza Etkisi

Birçok yapay zekâ API’sinde kullanım maliyeti **input token** ve **output token** sayılarına göre hesaplanır:

- **Input token:** Modele gönderilen talimat, soru ve ek bağlamdır.
- **Output token:** Modelin ürettiği cevaptır.

Daha uzun girdiler genellikle daha fazla bellek ve hesaplama gerektirir. Daha uzun cevapların token token üretilmesi de yanıt süresini artırabilir. Bu nedenle geliştiriciler açık, doğrudan ve gereksiz tekrar içermeyen promptlar yazmaya çalışır. Ancak yalnızca token sayısını azaltmak için gerekli bağlamı çıkarmak cevabın kalitesini düşürebilir. Amaç en kısa promptu değil, yeterli bilgiyi verimli şekilde sağlayan promptu oluşturmaktır.

## RAG Sistemlerinde Token Kullanımı

RAG sistemlerinde kullanıcı sorusuna cevap verebilmek için dış belgelerden ilgili bilgiler bulunup modele gönderilir. Fakat bütün belge arşivi context window içine sığmayabilir. Bu nedenle belgeler **chunk** adı verilen daha küçük bölümlere ayrılır.

Her chunk’ın uzunluğu ve içerdiği token sayısı önemlidir. Bölümler çok küçük olursa gerekli bağlam parçalanabilir; çok büyük olursa ilgisiz bilgiler context window’u doldurabilir. Bu nedenle token bilgisi, belge parçalama ve doğru bilginin modele gönderilmesi süreçlerinde önemli bir tasarım ölçütüdür.

## Farklı Modellerde Token Sayısı Neden Değişir?

Her yapay zekâ modeli aynı tokenizerı ve token sözlüğünü kullanmaz. Bir tokenizer bir kelimeyi tek token olarak görürken başka biri birkaç parçaya ayırabilir. Bu nedenle aynı cümle GPT, Llama veya başka bir modelde farklı sayıda token oluşturabilir.

Tokenization eğitim verilerindeki dil dağılımından da etkilenir. Bir dil veya kelime türü tokenizerın eğitim verilerinde daha az bulunuyorsa daha küçük parçalara ayrılabilir. Bu yüzden İngilizce için verilen yaklaşık token–kelime oranları Türkçe metinlerde aynı sonucu vermeyebilir. Kesin token sayısı, kullanılacak modelin kendi tokenizerıyla hesaplanmalıdır.

## Sonuç

Token, bir yapay zekâ modelinin metni okurken ve üretirken kullandığı temel işlem parçasıdır. Bir kelime, kelimenin bir bölümü, karakter, sayı veya noktalama işareti token olabilir. Tokenization işlemi metni bu parçalara ayırır; her token önce bir token ID’ye, ardından modelin işleyebileceği embedding vektörüne dönüştürülür.

Tokenlar modelin sınırlı bir sözlükle çok sayıda kelimeyi işleyebilmesini sağlar. Aynı zamanda context window uzunluğunu, işlem süresini, API maliyetini ve bir uygulamada kullanılabilecek veri miktarını etkiler. Bu nedenle token kavramını anlamak yalnızca büyük dil modellerinin çalışma mantığını değil, prompt tasarımı ve RAG gibi güncel yapay zekâ uygulamalarını anlamak açısından da önemlidir.
