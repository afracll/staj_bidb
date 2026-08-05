# Sinir Ağlarında Aktivasyon Fonksiyonları: ReLU ve GELU

## Aktivasyon Fonksiyonu Nedir?

Aktivasyon fonksiyonu, bir nöronun hesapladığı değeri dönüştürerek sonraki katmana aktarılacak çıktıyı belirler. Nöron öncelikle girdileri ağırlıklarla çarpar, sonuçları toplar ve bias ekler. Elde edilen değer daha sonra aktivasyon fonksiyonundan geçirilir.

```text
z = (girdiler × ağırlıklar) + bias
çıktı = aktivasyon_fonksiyonu(z)
```

Aktivasyon fonksiyonlarının en önemli görevi sinir ağına **doğrusal olmayanlık** kazandırmaktır. Eğer bütün katmanlarda yalnızca doğrusal işlemler yapılsaydı, katman sayısı artsa bile ağ karmaşık ilişkileri öğrenemezdi. Aktivasyon fonksiyonları sayesinde sinir ağları görüntü, metin ve ses gibi karmaşık verilerdeki örüntüleri öğrenebilir.

Sinir ağlarında sigmoid, tanh, ReLU ve GELU gibi farklı aktivasyon fonksiyonları kullanılabilir. ReLU ve GELU, özellikle derin öğrenme modellerinde yaygın olarak tercih edilen iki fonksiyondur.

## ReLU Nedir?

**ReLU (Rectified Linear Unit)**, basit ve hızlı çalışan bir aktivasyon fonksiyonudur. Girdi pozitifse değeri değiştirmeden geçirir, girdi sıfır veya negatifse çıktı olarak sıfır verir.

```text
ReLU(x) = max(0, x)
```

Örnekler:

```text
ReLU(5)  = 5
ReLU(2)  = 2
ReLU(0)  = 0
ReLU(-3) = 0
```

ReLU’nun hesaplanması oldukça kolaydır. Pozitif girdilerde gradient değeri sabit olduğu için derin ağlarda görülebilen **vanishing gradient**, yani gradientlerin aşırı küçülmesi sorununu azaltmaya yardımcı olur. Bu özellik modelin daha hızlı öğrenmesini sağlayabilir. Ancak ReLU bu sorunu her durumda tamamen ortadan kaldırmaz.

### ReLU’nun Avantajları

- Yapısı basit olduğu için hızlı hesaplanır.
- Derin sinir ağlarının daha verimli eğitilmesine yardımcı olur.
- Pozitif değerlerde gradientin kaybolmasını azaltabilir.
- CNN ve görüntü işleme modellerinde yaygın olarak kullanılır.

### Dying ReLU Sorunu

ReLU’nun en önemli sınırlaması **Dying ReLU** problemidir. Bir nöron sürekli negatif değer üretmeye başlarsa ReLU bu değerleri sıfıra dönüştürür. Negatif bölgede gradient de sıfır olduğu için nöronun ağırlıkları artık güncellenmeyebilir. Böylece nöron sürekli sıfır üreten ve öğrenmeye katkı sağlamayan bir duruma gelebilir.

## GELU Nedir?

**GELU (Gaussian Error Linear Unit)**, ReLU’ya göre daha yumuşak geçiş yapan bir aktivasyon fonksiyonudur. Açılımı Gaussian Error Linear Unit’tir. Matematiksel olarak giriş değeri, standart normal dağılımın kümülatif dağılım fonksiyonuyla ağırlıklandırılır.

```text
GELU(x) = x × Φ(x)
```

Buradaki `Φ(x)`, standart normal dağılımın kümülatif dağılım fonksiyonudur. Formülü ezberlemekten çok çalışma mantığını anlamak daha önemlidir.

ReLU negatif değerlerin tamamını doğrudan sıfıra çevirirken GELU bazı negatif değerlerin küçük miktarda geçmesine izin verir. Sıfır noktasında keskin bir geçiş yapmaz. Bu yumuşak yapı, backpropagation sırasında daha düzenli gradientler oluşmasına yardımcı olabilir.

### GELU’nun Avantajları

- Sıfır çevresinde yumuşak bir geçiş oluşturur.
- Küçük negatif değerleri tamamen yok etmez.
- Dying ReLU sorununa daha az yatkındır.
- Karmaşık modellerde başarılı sonuçlar verebilir.
- Transformer ve doğal dil işleme modellerinde yaygın olarak kullanılır.

### GELU’nun Sınırlamaları

GELU’nun matematiksel işlemi ReLU’dan daha karmaşıktır. Bu nedenle hesaplama maliyeti biraz daha yüksek olabilir. Ayrıca her veri setinde veya modelde ReLU’dan daha iyi sonuç vereceğinin garantisi yoktur.

## ReLU ve GELU Karşılaştırması

| Özellik | ReLU | GELU |
| --- | --- | --- |
| Çalışma biçimi | Negatif değerleri sıfırlar, pozitifleri geçirir | Değerleri yumuşak biçimde ağırlıklandırır |
| Geçiş yapısı | Sıfır noktasında keskin | Yumuşak ve sürekli |
| Hesaplama maliyeti | Daha düşük | Biraz daha yüksek |
| Negatif girdiler | Tamamını sıfırlar | Bazılarını küçük değerlerle geçirir |
| Temel sorun | Dying ReLU oluşabilir | Daha karmaşık hesaplanır |
| Yaygın kullanım | CNN ve klasik derin ağlar | Transformer ve NLP modelleri |

## Hangi Aktivasyon Fonksiyonu Seçilmelidir?

Aktivasyon fonksiyonu seçimi problemin türüne ve model mimarisine göre yapılmalıdır.

- Hesaplama hızı ve basitlik önemliyse **ReLU** iyi bir başlangıç seçeneğidir.
- CNN tabanlı görüntü işleme modellerinde ReLU sık kullanılır.
- Transformer tabanlı modellerde ve doğal dil işleme görevlerinde **GELU** yaygın olarak tercih edilir.
- Dying ReLU sorunu yaşanıyorsa GELU’nun yanında Leaky ReLU gibi alternatifler de denenebilir.

En doğru seçim yalnızca teorik özelliklere bakılarak yapılamaz. Farklı aktivasyon fonksiyonları denenmeli ve modelin validation verisindeki performansı karşılaştırılmalıdır.

## Sonuç

Aktivasyon fonksiyonları sinir ağlarının doğrusal olmayan ve karmaşık ilişkileri öğrenebilmesini sağlar. ReLU basit, hızlı ve etkili bir fonksiyondur ancak negatif bölgede nöronların öğrenmeyi bırakmasına neden olabilir. GELU ise daha yumuşak çalışır ve küçük negatif değerleri tamamen yok etmez, fakat hesaplanması daha karmaşıktır. ReLU özellikle CNN modellerinde, GELU ise Transformer ve NLP modellerinde sık kullanılmaktadır. Hangisinin daha uygun olduğu modelin yapısına, veriye ve yapılan göreve göre belirlenmelidir.
