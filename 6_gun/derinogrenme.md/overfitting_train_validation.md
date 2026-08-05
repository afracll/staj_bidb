# Overfitting ve Training/Validation Loss

Bir derin öğrenme modelinin başarılı olması yalnızca eğitim verilerinde düşük hata yapmasına bağlı değildir. Asıl amaç, modelin daha önce görmediği veriler üzerinde de doğru tahminler yapabilmesidir. Modelin bu yeteneğine **genelleme (generalization)** denir. Training loss ve validation loss değerleri birlikte takip edilerek modelin gerçekten öğrenip öğrenmediği ve yeni verilere genelleme yapıp yapamadığı anlaşılabilir.

## Loss Nedir?

**Loss**, modelin tahmini ile gerçek cevap arasındaki hatayı sayısal olarak gösteren değerdir. Loss değeri düşükse modelin tahminleri genellikle gerçek değerlere daha yakındır. Yüksek loss ise modelin daha fazla hata yaptığını gösterir.

Kullanılacak loss function problem türüne göre seçilir. Örneğin regresyon problemlerinde MSE veya MAE, ikili sınıflandırmada Binary Cross-Entropy, çok sınıflı sınıflandırmada ise Categorical Cross-Entropy kullanılabilir.

Loss değerinin genel hesaplama mantığı şu şekildedir:

```text
Ortalama loss = Bütün örneklerdeki hata toplamı / Örnek sayısı
```

## Training Loss Nedir?

**Training loss**, modelin eğitim verileri üzerindeki hata değeridir. Eğitim sırasında model bir batch üzerinde tahmin yapar, hata hesaplanır ve backpropagation ile gradientler bulunur. Optimizer daha sonra ağırlık ve bias değerlerini bu hatayı azaltacak şekilde günceller.

Training loss genellikle her batch için hesaplanır ve epoch sonunda bu değerlerin ortalaması gösterilir. Eğitim düzgün ilerliyorsa training loss’un zaman içinde azalması beklenir. Ancak training loss’un tek başına düşük olması modelin başarılı olduğunu kanıtlamaz. Model eğitim verilerini ezberlemiş de olabilir.

## Validation Loss Nedir?

**Validation loss**, modelin eğitim sırasında kullanılmayan validation verileri üzerindeki hata değeridir. Validation verileriyle modelin ağırlıkları güncellenmez. Bu veriler, her epoch sonunda modelin daha önce görmediği örneklerde nasıl performans gösterdiğini kontrol etmek için kullanılır.

Validation loss sayesinde şu sorulara cevap aranır:

- Model yeni verilere genelleme yapabiliyor mu?
- Eğitim devam etmeli mi, yoksa durdurulmalı mı?
- Model overfitting yapmaya başladı mı?
- Hiperparametrelerde veya model mimarisinde değişiklik gerekiyor mu?

Training loss ile validation loss genellikle epoch sayısına göre aynı grafik üzerinde gösterilir. Bu iki eğrinin birlikte yorumlanması modelin öğrenme durumunu anlamamızı sağlar.

## Training ve Validation Loss Arasındaki Fark

| Özellik | Training Loss | Validation Loss |
| --- | --- | --- |
| Kullanılan veri | Eğitim veri seti | Validation veri seti |
| Temel amacı | Modelin eğitim verisini ne kadar öğrendiğini göstermek | Modelin görülmemiş verilere genellemesini ölçmek |
| Parametre güncellemesi | Hesaplanan gradientler eğitimde kullanılır | Ağırlıklar güncellenmez |
| Ölçülme zamanı | Genellikle her batch’te hesaplanır, epoch sonunda ortalanır | Genellikle her epoch sonunda hesaplanır |

## Loss Grafiklerinin Yorumlanması

### Modelin İyi Öğrenmesi

Training loss ve validation loss birlikte azalıyor ve bir noktadan sonra birbirine yakın değerlerde dengeleniyorsa model genellikle doğru şekilde öğreniyordur. İki eğri arasında küçük bir fark bulunması normaldir. Bu durum modelin eğitim verilerini öğrenirken validation verilerine de genelleme yapabildiğini gösterir.

### Underfitting

Training loss ve validation loss değerlerinin ikisi de yüksek kalıyorsa model **underfitting**, yani eksik öğrenme yaşıyor olabilir. Model eğitim verilerindeki temel ilişkileri bile yeterince öğrenememiştir.

Underfitting’in bazı nedenleri şunlardır:

- Modelin problem için fazla basit olması
- Epoch sayısının yetersiz olması
- Öğrenme oranının uygun olmaması
- Kullanılan özelliklerin yetersiz olması
- Aşırı regularization uygulanması

Bu durumda eğitim süresi artırılabilir, modelin kapasitesi yükseltilebilir, özellikler iyileştirilebilir veya hiperparametreler yeniden ayarlanabilir.

### Overfitting

Training loss azalmaya devam ederken validation loss önce azalıp daha sonra yükselmeye başlıyorsa model **overfitting**, yani aşırı öğrenme yapıyor olabilir. Model eğitim verilerinde çok başarılı olurken yeni verilerde daha fazla hata yapmaya başlamıştır.

Bu durumda training ve validation loss eğrileri arasındaki fark giderek açılır. Validation loss’un en düşük olduğu nokta, çoğu zaman modelin yeni verilere en iyi genelleme yaptığı eğitim aşamasını gösterir.

### Validation Loss’un Daha Düşük Olması

Bazen validation loss, training loss’tan biraz daha düşük olabilir. Bunun nedeni training sırasında kullanılan Dropout veya veri artırma gibi yöntemlerin eğitimi zorlaştırması olabilir. Validation verileri daha kolay örneklerden oluşuyorsa da benzer bir durum görülebilir. Fark küçükse bu durum tek başına sorun anlamına gelmez.

Validation loss’ta ani yükselmeler görülüyorsa yüksek öğrenme oranı, az sayıda validation örneği veya gürültülü veriler gibi nedenler araştırılmalıdır.

## Overfitting Nedir?

Overfitting, modelin eğitim verilerini ve bu verilerdeki gereksiz ayrıntıları veya gürültüyü fazla öğrenmesidir. Model eğitim setinde düşük hata üretir fakat daha önce görmediği veriler üzerinde başarılı olamaz.

Bir öğrencinin soruların mantığını anlamak yerine yalnızca cevapları ezberlediğini düşünelim. Aynı sorular sorulduğunda başarılı olur ancak soru biçimi değiştiğinde zorlanır. Overfitting yapan bir model de benzer şekilde eğitim örneklerini öğrenir fakat yeni örneklere uyum sağlayamaz.

Overfitting’in yaygın nedenleri şunlardır:

- Modelin veri miktarına göre fazla karmaşık olması
- Modelin gereğinden fazla epoch boyunca eğitilmesi
- Eğitim verisinin az veya temsil gücünün düşük olması
- Verideki gürültü ve hataların fazla olması
- Çok fazla gereksiz özellik kullanılması
- Regularization yöntemlerinin kullanılmaması

## Overfitting Nasıl Tespit Edilir?

En temel yöntem training ve validation loss eğrilerini birlikte incelemektir. Training loss düşerken validation loss yükseliyor ve iki değer arasındaki fark büyüyorsa overfitting ihtimali yüksektir.

Model geliştirme sırasında overfitting’i izlemek ve hiperparametreleri ayarlamak için **validation set** kullanılmalıdır. **Test set** ise model ve hiperparametre seçimleri tamamlandıktan sonra yalnızca son performansı tarafsız şekilde değerlendirmek için kullanılmalıdır. Test verisine tekrar tekrar bakarak model ayarlamak, test setine karşı da overfitting oluşmasına neden olabilir.

Veri miktarı uygunsa K-Fold Cross-Validation gibi yöntemlerle model farklı veri bölümleri üzerinde eğitilip değerlendirilebilir. Böylece performansın yalnızca tek bir veri ayrımına bağlı olup olmadığı daha güvenilir şekilde incelenir.

## Overfitting Nasıl Önlenir?

### Early Stopping

Validation loss iyileşmeyi bırakıp yükselmeye başladığında eğitim durdurulur. Böylece model eğitim verisini gereğinden fazla öğrenmeden, validation performansının en iyi olduğu noktadaki ağırlıklar korunur.

### Daha Fazla ve Kaliteli Veri Kullanmak

Daha fazla temiz ve problem alanını temsil eden veri, modelin genel örüntüleri öğrenmesine yardımcı olabilir. Yalnızca veri miktarını artırmak yeterli değildir; verilerin doğru ve ilgili olması da önemlidir.

### Data Augmentation

Özellikle görüntü, ses ve metin verilerinde mevcut örneklerden değiştirilmiş yeni eğitim örnekleri oluşturulabilir. Görüntüyü döndürmek, kırpmak veya yansıtmak buna örnektir. Bu yöntem modelin farklı örnekleri görmesini sağlayarak genelleme gücünü artırabilir.

### Modeli Basitleştirmek

Gereğinden fazla katman, nöron veya parametre varsa model küçültülebilir. Gereksiz özelliklerin çıkarılması da modelin verideki gürültüyü ezberlemesini azaltabilir.

### Regularization

L1 ve L2 regularization yöntemleri büyük ağırlıklara ceza ekleyerek modelin aşırı karmaşık hâle gelmesini önlemeye çalışır. **Dropout** ise eğitim sırasında bazı nöronları rastgele devre dışı bırakarak ağın belirli nöronlara fazla bağımlı olmasını azaltır.

## Loss Değerlerini Etkileyen Faktörler

- **Learning rate:** Çok yüksekse loss dalgalanabilir, çok düşükse öğrenme yavaşlayabilir.
- **Batch size:** Küçük batch’ler daha gürültülü, büyük batch’ler daha dengeli gradientler üretebilir.
- **Model karmaşıklığı:** Fazla basit model underfitting, fazla karmaşık model overfitting yapabilir.
- **Veri kalitesi:** Hatalı, dengesiz veya gürültülü veriler loss değerini yükseltebilir.
- **Ağırlıkların başlangıcı:** Uygun olmayan başlangıç değerleri eğitimi zorlaştırabilir.
- **Optimizer ve regularization:** Parametrelerin nasıl güncellendiğini ve modelin genellemesini etkiler.

## Sonuç

Training loss modelin eğitim verilerindeki hatasını, validation loss ise eğitimde kullanılmayan verilerdeki hatasını gösterir. İki değerin birlikte azalması ve birbirine yakın seviyelerde dengelenmesi genellikle sağlıklı öğrenmeye işaret eder. Her iki loss yüksekse underfitting, training loss düşerken validation loss yükseliyorsa overfitting görülebilir. Amaç training loss’u tek başına en düşük seviyeye indirmek değil, modelin yeni verilere genelleme yapabildiği dengeli noktayı bulmaktır.
