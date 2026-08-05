# Sinir Ağı Nedir?

Sinir ağı, verilerdeki örüntüleri öğrenerek girdilerden bir çıktı üretmeye çalışan makine öğrenmesi modelidir. Bir sinir ağı, **yapay nöron** adı verilen basit işlem birimlerinin katmanlar hâlinde bir araya gelmesiyle oluşur.

Bu modeller eğitim sırasında verilerden **ağırlık** ve **bias (sapma)** değerlerini öğrenir. Öğrenilen bu parametreler, girdilerin sonucu ne kadar etkilediğini belirler. Sinir ağları görüntü tanıma, doğal dil işleme, konuşma tanıma, tahmin ve yüz tanıma gibi birçok alanda kullanılmaktadır.

Sinir ağları insan beynindeki biyolojik nöronlardan esinlenmiştir ancak beynin birebir kopyası değildir. İlk matematiksel nöron modeli 1943 yılında Warren McCulloch ve Walter Pitts tarafından önerilmiştir. Frank Rosenblatt ise 1958 yılında günümüzdeki sinir ağlarının tarihsel temellerinden biri olan **perceptron** modelini geliştirmiştir.

## Sinir Ağları Nasıl Çalışır?

Bir sinir ağının çalışma mantığı spam e-posta tespitiyle açıklanabilir. Modele bir e-posta verildiğinde “ödül”, “para” veya “kazan” gibi kelimeler girdi olarak kullanılabilir. İlk katmanlar bu kelimeleri incelerken sonraki katmanlar kelimeler arasındaki ilişki ve bağlam gibi daha karmaşık özellikleri öğrenebilir. Çıkış katmanı ise e-postanın spam olma olasılığını üretir.

Model eğitim sırasında hangi kelimelerin spam kararı için daha önemli olduğunu kendisi öğrenir. Böylece ham girdileri anlamlı örüntülere dönüştürerek yeni e-postalar hakkında tahmin yapabilir.

## Ağırlık ve Bias Nedir?

**Ağırlıklar**, her girdinin sonucu ne kadar etkileyeceğini belirler. Spam örneğinde “ödül” kelimesi spam kararı için önemliyse bu kelimeye daha yüksek bir ağırlık verilebilir. “Merhaba” gibi birçok e-postada bulunan bir kelimenin ağırlığı ise daha düşük olabilir.

**Bias**, nöronun karar sınırını ayarlayan ek bir değerdir. Ağırlıklar ve bias değerleri modelin parametreleridir ve eğitim sırasında sürekli olarak güncellenir.

Bir nöronun temel hesabı basitçe şu şekilde gösterilebilir:

```text
z = (girdiler × ağırlıklar) + bias
çıktı = aktivasyon_fonksiyonu(z)
```

Aktivasyon fonksiyonu, nöronun ürettiği değeri dönüştürür ve sinir ağının doğrusal olmayan karmaşık ilişkileri öğrenebilmesini sağlar. ReLU, sigmoid ve tanh yaygın aktivasyon fonksiyonlarıdır.

## Sinir Ağının Katmanları

Bir sinir ağı genel olarak üç tür katmandan oluşur:

- **Girdi katmanı:** Modele verilen ham özellikleri içerir. Örneğin bir görüntünün pikselleri veya bir e-postadaki kelimeler girdi olabilir.
- **Gizli katmanlar:** Girdileri ağırlık, bias ve aktivasyon fonksiyonları kullanarak yeni temsillere dönüştürür.
- **Çıkış katmanı:** Modelin son tahminini üretir. Regresyonda bir sayı, sınıflandırmada ise bir sınıf veya olasılık değeri üretebilir.

Bir sinir ağında birden fazla gizli katman bulunuyorsa bu yapı **derin sinir ağı** olarak adlandırılabilir.

## Sinir Ağı Eğitimi

Sinir ağının doğru tahminler yapabilmesi için verilerle eğitilmesi gerekir. Eğitim süreci dört temel adımda gerçekleşir:

### 1. İleri Yayılım

Girdiler sinir ağının katmanlarından geçirilir ve model bir tahmin üretir.

### 2. Hatanın Hesaplanması

Modelin tahmini gerçek sonuçla karşılaştırılır. Aradaki hata bir **loss function** kullanılarak hesaplanır.

### 3. Geri Yayılım

Hata, ağın çıkışından girişine doğru geriye taşınır. Böylece her ağırlık ve bias değerinin hataya ne kadar katkı sağladığı hesaplanır.

### 4. Parametrelerin Güncellenmesi

Gradyan inişi gibi bir optimizasyon yöntemi, ağırlık ve bias değerlerini hatayı azaltacak yönde günceller.

Bu işlem eğitim verileri üzerinde birçok kez tekrarlanır. Model her tekrarda parametrelerini biraz daha düzenleyerek tahminlerini gerçek sonuçlara yaklaştırmaya çalışır.

## Overfitting Sorunu

Sinir ağı çok karmaşık olduğunda veya eğitim verileri yeterli olmadığında model, genel ilişkileri öğrenmek yerine eğitim verilerini ezberleyebilir. Bu duruma **overfitting (aşırı öğrenme)** denir.

Overfitting yapan model eğitim verilerinde başarılı görünür ancak daha önce görmediği verilerde kötü sonuç verebilir. Bu nedenle modelin yalnızca eğitim verisindeki değil, validation ve test verilerindeki performansı da değerlendirilmelidir.

## Sinir Ağı Türleri

### Çok Katmanlı Algılayıcı (MLP)

MLP, girdi, gizli ve çıkış katmanlarından oluşan temel sinir ağı türlerinden biridir. Birçok sinir ağı mimarisinin temelini oluşturur.

### Evrişimsel Sinir Ağları (CNN)

CNN'ler özellikle görüntü gibi ızgara yapısındaki veriler için geliştirilmiştir. Görüntü tanıma, bilgisayarlı görü, yüz tanıma ve tıbbi görüntüleme alanlarında kullanılır.

### Tekrarlayan Sinir Ağları (RNN)

RNN'ler sıralı verileri işlemek için geliştirilmiştir. Konuşma tanıma, zaman serisi tahmini ve metin gibi sıranın önemli olduğu verilerde kullanılabilir.

### Transformer'lar

Transformer'lar, verinin farklı bölümleri arasındaki ilişkileri öğrenmek için **attention (dikkat)** mekanizmasını kullanır. Özellikle doğal dil işlemede yaygınlaşmıştır ve GPT gibi büyük dil modellerinin temelini oluşturur.

## Sinir Ağlarının Kullanım Alanları

Sinir ağlarının başlıca kullanım alanları şunlardır:

- **Bilgisayarlı görü:** Görüntü tanıma, yüz tanıma, tıbbi görüntüleme ve otonom araçlar
- **Doğal dil işleme:** Makine çevirisi, sohbet botları, metin üretme ve özetleme
- **Konuşma tanıma:** Sesin metne çevrilmesi ve sesli asistanlar
- **Tahmin:** Talep, hava durumu ve zaman serisi tahminleri
- **Pekiştirmeli öğrenme:** Oyun oynayan veya karar veren yapay zeka sistemleri
- **Örüntü tanıma:** Dolandırıcılık, anormal davranış ve belge türü tespiti

## Sinir Ağları Neden Önemlidir?

Sinir ağları, basit modellerin yakalamakta zorlandığı karmaşık ve doğrusal olmayan ilişkileri öğrenebilir. Ayrıca görüntü, metin ve ses gibi büyük verilerden önemli özellikleri otomatik olarak çıkarabilir.

CNN, RNN ve Transformer gibi farklı mimariler aynı temel prensiplere dayanır: yapay nöronlar, katmanlar, ağırlıklar, bias değerleri, aktivasyon fonksiyonları ve eğitim sırasında yapılan parametre güncellemeleri.

## Sonuç

Sinir ağları, katmanlar hâlinde düzenlenmiş yapay nöronlardan oluşan ve verilerden ağırlıklarla bias değerlerini öğrenen makine öğrenmesi modelleridir. Eğitim sırasında tahmin yapar, hatasını ölçer ve parametrelerini güncelleyerek daha doğru sonuçlar üretmeye çalışır.

Görüntü tanıma, doğal dil işleme, konuşma tanıma ve tahmin gibi birçok alanda kullanılmaları, sinir ağlarını modern yapay zekanın en önemli yapı taşlarından biri hâline getirmiştir.
