# Transformer Mimarisi Nedir ve Neden Önemlidir?

## Transformer Nedir?

**Transformer**, özellikle metin gibi sıralı verilerde parçalar arasındaki ilişkileri öğrenmek için attention mekanizmasını kullanan bir yapay sinir ağı mimarisidir. İlk olarak makine çevirisi gibi bir diziyi başka bir diziye dönüştüren görevler için geliştirilmiş, daha sonra doğal dil işleme, görüntü işleme, ses, öneri sistemleri ve üretken yapay zekâ gibi birçok alana yayılmıştır.

ChatGPT’nin temelindeki GPT modelleri ve BERT gibi dil modelleri Transformer mimarisinden türetilmiştir. Ancak Transformer yalnızca bir sohbet modeli değildir; farklı amaçlara göre kullanılabilen genel bir sinir ağı mimarisidir.

Transformer’ın temel özelliği, bir dizideki tokenlar arasındaki ilişkileri **attention** ile hesaplamasıdır. Böylece model, bir kelimeyi işlerken cümlenin ilgili diğer bölümlerine bakabilir ve kelimenin bağlama göre taşıdığı anlamı daha iyi temsil edebilir.

## Transformer’a Neden İhtiyaç Duyuldu?

Transformer’dan önce metin ve zaman serileri gibi sıralı verilerde RNN ve LSTM modelleri yaygın olarak kullanılıyordu. RNN’ler kelimeleri sırayla, yani bir önceki adımın sonucuna bağlı olarak işler. Bu yaklaşım kısa dizilerde işe yarasa da bazı sorunlar oluşturabilir:

- Kelimeler tek tek işlendiği için paralel hesaplama sınırlıdır.
- Uzun metinlerin başındaki bilgi sonraki adımlara taşınırken zayıflayabilir.
- Uzak kelimeler arasındaki ilişkileri öğrenmek zorlaşabilir.
- Uzun dizilerde vanishing gradient gibi eğitim sorunları görülebilir.

LSTM modelleri hafıza hücreleri sayesinde bu sorunların bir bölümünü azaltmıştır. Fakat yine de verileri adım adım işlediği için uzun dizilerde eğitim yavaş kalabilir.

Örneğin “Ali 2019 yılında Fransa’ya gitti ve orada ülkenin başkanıyla görüştü” cümlesinde “ülke” kelimesinin Fransa’ya gönderme yaptığı anlaşılmalıdır. Aralarında çok sayıda kelime olduğunda klasik sıralı modeller bu tür uzun mesafeli ilişkileri yakalamakta zorlanabilir. Transformer ise attention kullanarak ilgili tokenlar arasında daha doğrudan bir bağlantı kurabilir.

## Transformer’ın Genel Çalışma Akışı

Bir metin Transformer modeline verildiğinde genel olarak şu işlemler gerçekleşir:

1. Metin tokenlara ayrılır.
2. Tokenlar token ID’lerine dönüştürülür.
3. Her token bir embedding vektörüyle temsil edilir.
4. Tokenların sırasını göstermek için konum bilgisi eklenir.
5. Attention katmanları tokenlar arasındaki ilişkileri hesaplar.
6. Feed-forward katmanları elde edilen temsilleri işler.
7. Bu işlemler birden fazla Transformer katmanında tekrarlanır.
8. Son katmandaki temsiller sınıflandırma, çeviri veya sonraki tokenı tahmin etme gibi görevin çıktısını üretmekte kullanılır.

## Transformer’ın Temel Bileşenleri

### Token Embedding

Transformer ham kelimelerle değil sayısal vektörlerle çalışır. Bu nedenle metindeki tokenlar önce embedding vektörlerine dönüştürülür. Model eğitildikçe embeddingler de güncellenerek tokenların kullanıldığı bağlamlar hakkında daha yararlı temsiller oluşturur.

### Positional Encoding

Self-attention işlemi tek başına tokenların hangi sırada bulunduğunu bilmez. Oysa “Köpek adamı ısırdı” ile “Adam köpeği ısırdı” cümlelerinde aynı kelimeler kullanılmasına rağmen anlam farklıdır.

Bu nedenle token embeddinglerine konum bilgisi eklenir. Orijinal Transformer’da sinüs ve kosinüs tabanlı **positional encoding** kullanılmıştır. Modern modellerde öğrenilebilir konum embeddingleri veya rotary positional embedding gibi farklı yöntemler de bulunur. Ortak amaç, tokenların dizideki sırasını modele bildirmektir.

### Self-Attention

**Self-attention**, dizideki her tokenın diğer tokenlarla ilişkisini inceleyerek bağlama göre yeni bir temsil oluşturmasını sağlar.

Her token embeddinginden üç farklı vektör üretilir:

- **Query (Q):** Tokenın hangi bilgiyi aradığını temsil eder.
- **Key (K):** Tokenın diğer tokenlar tarafından hangi özellik üzerinden bulunabileceğini temsil eder.
- **Value (V):** Tokenın taşıdığı ve diğer tokenlara aktarılabilecek bilgiyi temsil eder.

Bir tokenın Query vektörü diğer tokenların Key vektörleriyle karşılaştırılır. Elde edilen attention skorları, hangi Value vektörlerine ne kadar önem verileceğini belirler. Böylece her token yalnızca kendi bilgisini değil, cümledeki ilgili tokenlardan gelen bilgileri de içeren bağlamsal bir temsil kazanır.

Self-attention işleminin temel formülü şöyledir:

```text
Attention(Q, K, V) = softmax(QKᵀ / √dₖ) × V
```

Formülü ezberlemekten çok mantığını anlamak önemlidir: Query ve Key benzerliği hangi tokenlara dikkat edileceğini, Value ise taşınacak bilgiyi belirler.

### Multi-Head Attention

Transformer tek bir attention hesabı yerine birden fazla **attention head** kullanır. Her head farklı ilişkilere odaklanabilir. Bir head özne ile fiil arasındaki bağlantıyı, başka biri zamirin hangi isme gönderme yaptığını, bir diğeri ise uzak tokenlar arasındaki anlam ilişkisini öğrenebilir.

Head’lerin çıktıları birleştirilip yeniden dönüştürülür. Böylece model aynı cümleyi farklı ilişki türleri açısından birlikte inceleyebilir.

### Feed-Forward Network

Attention sonucunda oluşan her token temsili, ayrı bir küçük sinir ağı olan **feed-forward network** katmanından geçirilir. Bu katman doğrusal dönüşümler ve ReLU, GELU veya başka bir aktivasyon fonksiyonu kullanarak temsilin daha karmaşık özellikler öğrenmesini sağlar.

Attention tokenlar arasında bilgi alışverişi yaparken feed-forward katmanı her tokenın oluşan temsilini işler.

### Residual Connection ve Layer Normalization

Her attention ve feed-forward bloğunda giriş bilgisi bloğun çıktısına eklenir. Buna **residual connection** denir. Residual bağlantılar bilginin ve gradientlerin derin ağ boyunca daha rahat ilerlemesine yardımcı olur.

**Layer normalization** ise katman çıktılarının dağılımını düzenleyerek eğitimin daha kararlı olmasını sağlar. Bu yapılar sayesinde çok sayıda Transformer katmanı üst üste eklenebilir.

## Encoder ve Decoder Yapısı

Orijinal Transformer iki temel bölümden oluşur: encoder ve decoder.

### Encoder

Encoder, giriş dizisini alır ve her token için bağlam içeren temsiller üretir. Encoder self-attention katmanında girişteki bütün tokenlar birbirine dikkat edebilir. Çıktı tek bir vektör değil, dizideki tokenlara karşılık gelen bağlamsal vektörler dizisidir.

Encoder özellikle metni anlama, sınıflandırma ve bilgi çıkarma gibi görevlerde kullanılabilir.

### Decoder

Decoder, çıktıyı token token üretir. Decoder içindeki **masked self-attention**, bir konumdaki tokenın henüz üretilmemiş gelecek tokenlara bakmasını engeller. Böylece model yalnızca önceki tokenları kullanarak sıradaki tokenı tahmin eder.

Orijinal encoder–decoder Transformer’da decoder ayrıca encoderın ürettiği temsillere **cross-attention** ile bakar. Çeviri sırasında decoder, yeni dilde token üretirken giriş cümlesinin ilgili bölümlerine odaklanabilir.

Son aşamada model her olası token için skor üretir ve softmax bu skorları olasılık dağılımına çevirir. Seçilecek token yalnızca her zaman en yüksek olasılıklı token olmak zorunda değildir; kullanılan decoding yöntemine göre olasılığı yüksek seçeneklerden biri de seçilebilir.

## Modern Transformer Türleri

Günümüzde her Transformer modeli orijinal encoder–decoder yapısının tamamını kullanmaz.

| Model türü | Kullandığı bölüm | Temel kullanım | Örnek |
| --- | --- | --- | --- |
| Encoder-only | Yalnızca encoder | Metni anlama, sınıflandırma, varlık tanıma | BERT |
| Decoder-only | Yalnızca decoder | Sonraki token tahmini ve metin üretimi | GPT |
| Encoder–decoder | Her ikisi | Çeviri, özetleme ve metinden metne görevler | T5 |

Encoder-only modeller girişin tamamını birlikte analiz etmeye uygundur. Decoder-only modeller autoregressive biçimde önceki tokenlardan sıradaki tokenı tahmin eder. Encoder–decoder modeller ise bir giriş dizisini işleyip buna bağlı yeni bir çıktı dizisi üretir.

## Transformer Neden Önemlidir?

### Uzun Mesafeli İlişkileri Öğrenmesi

Attention sayesinde birbirinden uzaktaki tokenlar arasında daha doğrudan ilişkiler kurulabilir. Bu özellik uzun cümlelerde bağlamın ve kelime göndermelerinin öğrenilmesini kolaylaştırır.

### Eğitimin Paralelleştirilebilmesi

RNN’lerde bir sonraki adım önceki adımın tamamlanmasını bekler. Transformer eğitim sırasında dizideki birçok tokenın hesaplamasını paralel yapabilir. Bu durum GPU ve TPU gibi donanımlardan daha etkili yararlanılmasını ve büyük veri setleriyle model eğitilmesini sağlamıştır.

Ancak GPT gibi autoregressive modeller cevap üretirken gelecekteki token henüz bilinmediği için çıktı tokenlarını sırayla oluşturur. Yani paralellik avantajı özellikle eğitim ve giriş dizisinin işlenmesinde görülür.

### Ölçeklenebilmesi

Transformer mimarisi daha fazla veri, parametre ve hesaplama gücüyle büyük modellere ölçeklenebilir. Bu özellik BERT, GPT ve diğer foundation modellerin geliştirilmesinin önünü açmıştır.

### Transfer Learning Sağlaması

Büyük miktarda veri üzerinde önceden eğitilmiş bir Transformer modeli, daha küçük bir veri setiyle belirli bir göreve uyarlanabilir. Fine-tuning adı verilen bu yaklaşım her proje için sıfırdan model eğitme ihtiyacını azaltır.

### Farklı Veri Türlerine Uygulanabilmesi

Transformerlar yalnızca metinle sınırlı değildir. Görüntü parçaları, ses bölümleri veya farklı veri türleri token benzeri temsillere dönüştürülerek attention mekanizmasıyla işlenebilir. Bu özellik multimodal yapay zekâ sistemlerinin gelişmesinde önemli rol oynamıştır.

## Kullanım Alanları

- Makine çevirisi
- Metin üretme ve sohbet sistemleri
- Metin özetleme
- Duygu analizi ve metin sınıflandırma
- Soru cevaplama ve bilgi çıkarma
- Konuşma tanıma
- Görüntü sınıflandırma ve nesne tespiti
- Görüntü, ses ve müzik üretimi
- Öneri sistemleri
- Kod üretme ve kod tamamlama

## Sınırlamaları

Transformer mimarisi güçlü olmasına rağmen bazı sınırlamalara sahiptir:

- Büyük modellerin eğitimi yüksek işlem gücü, bellek ve enerji gerektirir.
- Standart self-attention işleminde token çiftleri karşılaştırıldığı için dizi uzadıkça hesaplama ve bellek maliyeti hızla artar.
- Her modelin aynı anda işleyebileceği sınırlı bir context window vardır.
- Çok büyük ve karmaşık modellerin kararlarını açıklamak zor olabilir.
- Eğitim verilerindeki yanlış bilgiler ve önyargılar modele yansıyabilir.
- Büyük dil modelleri doğru görünmesine rağmen yanlış bilgiler üretebilir.
- Yetersiz veri, yanlış hiperparametreler veya gereğinden uzun eğitim overfitting oluşturabilir.

## Sonuç

Transformer, dizideki tokenlar arasındaki ilişkileri attention mekanizmasıyla öğrenen bir sinir ağı mimarisidir. Token embeddingleri ve konum bilgileriyle başlayan veriler; self-attention, multi-head attention, feed-forward network, residual connection ve layer normalization katmanlarından geçirilir. Orijinal mimaride encoder girişi bağlamsal temsillere dönüştürür, decoder ise bu temsillerden yararlanarak çıktıyı sırayla üretir.

Transformer’ın uzun mesafeli ilişkileri yakalayabilmesi, eğitimin büyük ölçüde paralelleştirilebilmesi ve farklı görevlere ölçeklenebilmesi modern yapay zekânın gelişiminde önemli bir kırılma oluşturmuştur. BERT, GPT ve T5 gibi modellerin yanında günümüzdeki birçok dil, görüntü, ses ve multimodal yapay zekâ sistemi bu mimarinin farklı sürümlerini kullanmaktadır.
