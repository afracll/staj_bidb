# Sinir Ağlarında Ağırlık, Bias ve Katmanlar

Yapay sinir ağları, verilerdeki örüntüleri öğrenerek tahmin yapan makine öğrenmesi modelleridir. Bir sinir ağının öğrenmesinde **ağırlıklar (weights)**, **bias değerleri** ve **katmanlar** önemli bir yere sahiptir. Ağırlıklar girdilerin önemini belirlerken bias, nöronların daha esnek karar vermesini sağlar. Katmanlar ise veriyi adım adım işleyerek sonuca dönüştürür.

## Ağırlık ve Bias Nedir?

### Ağırlıklar (Weights)

Ağırlıklar, her girdinin modelin tahminini ne kadar etkileyeceğini belirleyen sayısal değerlerdir. Sinir ağına verilen her özellik aynı öneme sahip olmayabilir. Model, eğitim sırasında hangi özelliklerin daha önemli olduğunu ağırlıkları değiştirerek öğrenir.

Örneğin bir evin fiyatı tahmin edilirken evin büyüklüğü, oda sayısı ve bulunduğu konum girdi olarak kullanılabilir. Evin büyüklüğü fiyatı daha fazla etkiliyorsa bu girdinin ağırlığı daha yüksek olabilir.

İleri yayılım sırasında girdiler kendi ağırlıklarıyla çarpılır. Eğitim ilerledikçe ağırlıklar, modelin yaptığı hatayı azaltacak şekilde gradyan inişi gibi optimizasyon yöntemleriyle güncellenir. Doğru öğrenilmiş ağırlıklar, modelin daha önce görmediği veriler üzerinde de başarılı tahminler yapmasına yardımcı olur.

### Bias

Bias, bir nöronun hesapladığı değere eklenen ve sonucu kaydıran ek bir model parametresidir. Modelin yalnızca girdilere bağlı kalmadan daha esnek bir şekilde öğrenmesini sağlar. Böylece girdiler düşük veya sıfır olsa bile nöron gerektiğinde etkinleşebilir.

Ev fiyatı örneğinde bias, evin büyüklüğü sıfır kabul edilse bile modelin başlangıç veya taban fiyat gibi bir değer oluşturabilmesine yardımcı olabilir.

Bir nöronun temel hesabı şu şekilde özetlenebilir:

```text
z = (girdiler × ağırlıklar) + bias
çıktı = aktivasyon_fonksiyonu(z)
```

Ağırlık ve bias değerleri eğitim başlamadan önce genellikle küçük rastgele değerlerle başlatılır. Eğitim sırasında ikisi de güncellenerek modelin tahmin hatası azaltılır.

## Sinir Ağının Öğrenme Süreci

### 1. İleri Yayılım (Forward Propagation)

İleri yayılım, verinin giriş katmanından başlayarak ağ boyunca ilerlemesi ve modelin bir tahmin üretmesidir.

1. Veriler giriş katmanına verilir.
2. Her girdi kendi ağırlığıyla çarpılır.
3. Elde edilen değerler toplanır ve bias eklenir.
4. Sonuç ReLU, sigmoid veya tanh gibi bir aktivasyon fonksiyonundan geçirilir.
5. Oluşan çıktı bir sonraki katmana aktarılır ve son katmana kadar aynı işlem devam eder.

### 2. Geriye Yayılım (Backpropagation)

Model tahmin yaptıktan sonra tahmin edilen değer ile gerçek değer arasındaki fark, kayıp fonksiyonu kullanılarak hesaplanır. Bu hata ağın sonundan başına doğru iletilir. Her ağırlık ve bias değerinin hataya ne kadar katkıda bulunduğu belirlenir. Daha sonra optimizasyon algoritması bu değerleri hatayı azaltacak yönde küçük miktarlarda günceller.

İleri ve geriye yayılım işlemleri eğitim boyunca birçok kez tekrarlanır. Böylece model zamanla daha doğru tahminler yapmayı öğrenir.

## Yapay Sinir Ağındaki Ana Katmanlar

Bir yapay sinir ağı temel olarak giriş katmanı, gizli katmanlar ve çıkış katmanından oluşur.

### Giriş Katmanı

Giriş katmanı, ham verilerin sinir ağına alındığı ilk katmandır. Genellikle her nöron verideki bir özelliği temsil eder. Örneğin ev fiyatı tahmininde büyüklük, oda sayısı ve bina yaşı ayrı girdiler olabilir. Bir görüntü işleniyorsa girişler piksel değerlerinden oluşabilir. Bu katman çoğunlukla veriyi alır ve sonraki katmana iletir.

### Gizli Katmanlar

Gizli katmanlar, giriş ve çıkış katmanları arasında bulunur. Sinir ağındaki hesaplamaların büyük kısmı burada yapılır. Girdiler ağırlık ve bias değerleriyle işlenir, ardından aktivasyon fonksiyonlarından geçirilir. Böylece ağ basit özelliklerden daha karmaşık ilişkiler öğrenebilir.

Gizli katmanların sayısı ve her katmandaki nöron sayısı, problemin karmaşıklığına göre belirlenir. Çok sayıda gizli katmana sahip ağlar derin sinir ağları olarak adlandırılır.

### Çıkış Katmanı

Çıkış katmanı modelin son tahminini üretir. Bu katmanın yapısı probleme göre değişir:

- İkili sınıflandırmada genellikle **sigmoid** kullanılır. Örneğin bir e-postanın spam olup olmadığı tahmin edilebilir.
- Çok sınıflı sınıflandırmada genellikle **softmax** kullanılır. Örneğin bir görsel kedi, köpek veya kuş olarak sınıflandırılabilir.
- Regresyon problemlerinde çoğunlukla **doğrusal (linear)** çıktı kullanılır. Örneğin bir evin fiyatı sayısal olarak tahmin edilebilir.

## Yaygın Katman Türleri

### Dense (Tam Bağlantılı) Katman

Bu katmanda her nöron, önceki katmandaki bütün nöronlara bağlıdır. Girdilerin ağırlıklı toplamını hesaplar, bias ekler ve aktivasyon fonksiyonunu uygular. Pek çok sinir ağı modelinde temel katman olarak kullanılır.

### Evrişimsel (Convolutional) Katman

Özellikle görüntü işlemede kullanılan CNN modellerinde bulunur. Filtreler yardımıyla görüntüyü tarar; kenar, doku ve şekil gibi özellikleri öğrenir. Tam bağlantılı katmanlara göre daha az parametre kullanarak görüntülerdeki konumsal bilgiyi koruyabilir.

### Tekrarlayan (Recurrent) Katman

Metin, ses ve zaman serileri gibi sıralı veriler için kullanılır. Önceki adımlardaki bilgileri belirli ölçüde saklayarak verinin sırasını ve zaman içindeki ilişkilerini öğrenmeye çalışır. RNN modellerinin temelini oluşturur.

### Dropout Katmanı

Dropout, eğitim sırasında bazı nöronları rastgele geçici olarak devre dışı bırakır. Böylece ağın yalnızca belirli nöronlara fazla bağımlı olması engellenir. Aşırı öğrenmeyi azaltmaya ve modelin yeni verilere daha iyi genelleme yapmasına yardımcı olur.

### Pooling (Havuzlama) Katmanı

Pooling katmanı, özellikle CNN modellerinde özellik haritalarının boyutunu küçültür. Böylece hesaplama maliyeti azalır ve önemli özellikler korunur. En yaygın türleri maksimum değeri seçen **Max Pooling** ve ortalamayı alan **Average Pooling** yöntemleridir.

### Batch Normalization Katmanı

Bu katman, önceki katmandan gelen değerleri bir veri grubu üzerinden normalleştirir. Değerlerin daha dengeli dağılmasına yardımcı olarak eğitimi daha kararlı ve hızlı hâle getirebilir. Özellikle derin sinir ağlarında sık kullanılır.

## Kullanım Alanları

Sinir ağlarındaki ağırlık, bias ve katman yapıları birçok alanda kullanılmaktadır:

- Görüntülerde nesne ve yüz tanıma
- Metin anlama ve üretme
- Konuşma tanıma
- Otonom araçlarda sensör verilerini işleme
- Sağlık verilerinden hastalık tespiti
- Finansal tahmin ve dolandırıcılık tespiti

## Avantajları ve Sınırlamaları

Sinir ağları karmaşık örüntüleri öğrenebilir, eğitim sırasında hatalarını azaltabilir ve yeterli veriyle yeni örneklere genelleme yapabilir. Fakat ağırlıkların uygun olmayan şekilde başlatılması öğrenmeyi yavaşlatabilir. Modelin çok karmaşık olması aşırı öğrenmeye yol açabilir. Ayrıca büyük ağların eğitimi zaman ve yüksek işlem gücü gerektirir. Milyonlarca parametrenin sonuca nasıl etki ettiğini açıklamak da zor olabilir.

## Sonuç

Ağırlıklar girdilerin önemini, bias değerleri ise nöronların karar esnekliğini belirler. Katmanlar da veriyi sırayla işleyerek son tahmini oluşturur. Model ileri yayılımda tahmin yapar, geriye yayılımda hatasını hesaplayıp ağırlık ve bias değerlerini günceller. Bu işlemin tekrar edilmesiyle sinir ağı verilerdeki örüntüleri öğrenir ve daha doğru sonuçlar üretmeye başlar.
