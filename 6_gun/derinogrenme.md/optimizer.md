# Derin Öğrenmede Optimizerlar

## Optimizer Nedir?

Optimizer, bir makine öğrenmesi veya derin öğrenme modelinin yaptığı hatayı azaltmak için kullanılan algoritmadır. Modelin tahmini ile gerçek sonuç arasındaki hata **loss function (kayıp fonksiyonu)** tarafından ölçülür. Optimizer ise bu hatayı azaltmak amacıyla modelin öğrenilebilir parametreleri olan **ağırlık ve bias değerlerini** günceller.

Optimizerın görevi doğrudan tahmin yapmak değildir. Backpropagation sırasında hesaplanan gradientleri kullanarak parametrelerin nasıl değiştirileceğine karar verir. Böylece model her eğitim adımında daha doğru sonuç üretmeye çalışır.

## Optimizer Nasıl Çalışır?

Optimizerın eğitim sürecindeki yeri şu şekilde özetlenebilir:

1. Model forward pass yaparak bir tahmin üretir.
2. Loss function tahmin ile gerçek değer arasındaki hatayı hesaplar.
3. Backpropagation, her ağırlık ve bias değerinin gradientini bulur.
4. Optimizer bu gradientleri ve öğrenme oranını kullanarak parametreleri günceller.
5. İşlem eğitim boyunca tekrar edilir.

Optimizerın kullandığı öğrenme oranı, momentum değeri ve benzeri ayarlar **hiperparametredir**. Ağırlıklar ve biaslar ise eğitim sırasında öğrenildiği için **model parametreleridir**.

## Yaygın Optimizer Türleri

### Gradient Descent

Gradient Descent, kayıp değerini azaltmak için parametreleri gradientin ters yönünde günceller. Klasik yöntemde gradient hesaplanırken eğitim verilerinin tamamı kullanılır. Mantığı kolaydır ancak büyük veri setlerinde yavaş çalışabilir ve fazla bellek gerektirebilir.

### Stochastic Gradient Descent (SGD)

SGD, parametreleri her seferinde tek bir veri örneğine göre günceller. Sık güncelleme yaptığı ve daha az bellek kullandığı için büyük veri setlerinde kullanılabilir. Ancak tek bir örnekten hesaplanan gradient değişken olabileceği için eğitim sırasında dalgalanmalar görülebilir.

Uygulamada veriyi küçük gruplara ayıran **Mini-Batch Gradient Descent** yaygın olarak kullanılır. Derin öğrenme kütüphanelerinde “SGD” denildiğinde çoğu zaman mini-batch’lerle çalışan sürüm kastedilir.

### SGD with Momentum

Momentum, önceki güncellemelerin yönünü belirli ölçüde hatırlayarak mevcut gradiente ekler. Hareket eden bir cismin hızını korumasına benzetilebilir. Bu yöntem dalgalanmaları azaltabilir ve modelin doğru yöne daha hızlı ilerlemesini sağlayabilir.

Momentumun avantajı eğitimi hızlandırabilmesi ve gürültülü güncellemeleri daha dengeli hâle getirebilmesidir. Ancak momentum değeri adı verilen ek bir hiperparametrenin seçilmesi gerekir.

### AdaGrad

AdaGrad, bütün parametreler için aynı öğrenme oranını kullanmak yerine her parametreye uyarlanmış farklı öğrenme oranları oluşturur. Sık güncellenmeyen özelliklere daha büyük, sık güncellenen özelliklere daha küçük adımlar uygulayabilir. Bu nedenle seyrek verilerde yararlı olabilir.

En önemli sınırlaması, eğitim ilerledikçe öğrenme oranının sürekli küçülmesidir. Derin ağlarda öğrenme oranı aşırı küçülürse model neredeyse öğrenemez duruma gelebilir.

### RMSprop

RMSprop, AdaGrad’ın öğrenme oranını sürekli küçültme sorununu azaltmak amacıyla geçmiş gradient karelerinin tamamını biriktirmek yerine hareketli ortalamasını kullanır. Böylece her parametre için öğrenme oranı otomatik olarak ayarlanırken eski gradientlerin etkisi zamanla azalır.

Özellikle gradientlerin zaman içinde çok değiştiği problemlerde daha dengeli eğitim sağlayabilir. Bununla birlikte her problemde en iyi sonucu vereceğinin garantisi yoktur.

### AdaDelta

AdaDelta da AdaGrad’ın giderek küçülen öğrenme oranı sorununu çözmeye çalışan bir yöntemdir. Önceki güncellemelerin ve gradientlerin hareketli ortalamalarından yararlanır. Öğrenme oranını elle belirleme ihtiyacını azaltmayı amaçlar. Ancak hesaplama açısından diğer bazı yöntemlere göre daha maliyetli olabilir ve günümüzde Adam kadar sık tercih edilmez.

### Adam

Adam, **Momentum** ve **RMSprop** yaklaşımlarının güçlü yönlerini bir araya getirir. Geçmiş gradientlerin hareketli ortalamasını ve gradient karelerinin hareketli ortalamasını birlikte takip eder. Ayrıca her parametre için uyarlanabilir öğrenme oranı kullanır.

Adam’ın yaygın kullanılmasının nedenleri şunlardır:

- Uygulanması kolaydır.
- Genellikle hızlı ve dengeli öğrenir.
- Çok büyük miktarda ek bellek gerektirmez.
- Seyrek veya gürültülü gradientlerde başarılı olabilir.
- Birçok problemde başlangıç seçeneği olarak iyi sonuç verir.

Bununla birlikte Adam her problem için kesin olarak en iyi optimizer değildir. Bazı görevlerde doğru ayarlanmış SGD with Momentum, yeni veriler üzerinde daha iyi sonuç verebilir.

## Optimizer Nasıl Seçilir?

Tek bir optimizer bütün problemler için en iyi değildir. Seçim yapılırken veri yapısı, model mimarisi, öğrenme hızı ve doğrulama sonuçları dikkate alınmalıdır.

- Yeni bir derin öğrenme projesine başlanıyorsa **Adam** uygun bir başlangıç seçeneği olabilir.
- Görüntü sınıflandırma gibi bazı görevlerde **SGD with Momentum** daha iyi genelleme sağlayabilir.
- Seyrek verilerde **AdaGrad** veya **Adam** denenebilir.
- Sıralı veriler ve değişken gradientler için **RMSprop** yararlı olabilir.

Optimizer seçildikten sonra öğrenme oranı başta olmak üzere ilgili hiperparametrelerin validation verisine göre ayarlanması gerekir. Yalnızca eğitim kaybının düşük olması yeterli değildir; modelin daha önce görmediği verilerde de başarılı olması beklenir.

## Avantajları ve Sınırlamaları

Optimizerlar modelin hatasını zamanla azaltır, karmaşık örüntülerin öğrenilmesini sağlar ve eğitim sürecini daha hızlı veya kararlı hâle getirebilir. Ancak yanlış optimizer veya öğrenme oranı seçimi eğitimi yavaşlatabilir, kayıp değerinin dalgalanmasına ya da modelin iyi bir çözüme ulaşamamasına neden olabilir.

Ayrıca gelişmiş optimizerlar ek hiperparametreler ve hesaplamalar içerir. Model eğitim verisine fazla uyum sağlarsa optimizer başarılı çalışsa bile **overfitting** oluşabilir. Bu nedenle optimizer seçimi; validation sonuçları, model mimarisi ve diğer eğitim ayarlarıyla birlikte değerlendirilmelidir.
