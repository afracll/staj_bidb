# Gradient ve Gradient Descent

## Gradient Nedir?

Gradient, bir fonksiyonun hangi yönde ve ne kadar hızlı değiştiğini gösteren matematiksel bir değerdir. Derin öğrenmede bu fonksiyon genellikle **loss function**, yani kayıp fonksiyonudur. Kayıp fonksiyonu, modelin yaptığı tahmin ile gerçek cevap arasındaki hatayı ölçer.

Gradient sayesinde modeldeki her ağırlık ve bias değerinin bu hatayı ne kadar etkilediği anlaşılır. Başka bir ifadeyle gradient, modelin hatasını azaltmak için parametrelerin hangi yönde değiştirilmesi gerektiğini gösterir.

Bir dağın yamacında olduğumuzu düşünürsek eğim bize yokuşun hangi yönde yükseldiğini gösterir. Amacımız en aşağıdaki noktaya ulaşmaksa eğimin ters yönünde ilerlememiz gerekir. Gradient Descent de benzer şekilde kayıp değerinin azaldığı yöne doğru hareket eder.

## Gradient Sinir Ağında Nasıl Kullanılır?

Sinir ağı önce **forward pass (ileri yayılım)** yaparak bir tahmin üretir. Daha sonra tahmin ile gerçek değer arasındaki hata loss function ile hesaplanır. **Backpropagation (geriye yayılım)** sırasında bu hata ağın son katmanından ilk katmanına doğru iletilir ve her parametrenin gradient değeri bulunur.

Burada kavramların görevleri birbirinden farklıdır:

- **Forward pass:** Modelin tahmin üretmesini sağlar.
- **Loss function:** Tahminin ne kadar hatalı olduğunu ölçer.
- **Backpropagation:** Gradientleri hesaplar.
- **Optimizer:** Hesaplanan gradientleri kullanarak ağırlık ve bias değerlerini günceller.

## Gradient Descent Nedir?

Gradient Descent, kayıp fonksiyonunu küçültmek için model parametrelerini adım adım değiştiren bir optimizasyon yöntemidir. Gradient, kaybın en hızlı arttığı yönü gösterdiği için parametreler gradientin ters yönünde güncellenir.

Temel güncelleme mantığı şu şekildedir:

```text
yeni ağırlık = eski ağırlık - öğrenme oranı × gradient
```

Bu işlem yalnızca bir kez yapılmaz. Eğitim boyunca tekrar edilerek modelin hatası aşamalı olarak azaltılmaya çalışılır.

## Gradient Descent’in Çalışma Adımları

1. Ağırlık ve bias değerleri başlangıç değerleriyle oluşturulur.
2. Model ileri yayılım yaparak tahmin üretir.
3. Kayıp fonksiyonu ile tahmin hatası hesaplanır.
4. Geriye yayılım sayesinde gradientler bulunur.
5. Parametreler gradientin ters yönünde güncellenir.
6. Bu işlemler belirlenen epoch sayısı boyunca tekrarlanır.

## Öğrenme Oranı

**Learning rate (öğrenme oranı)**, parametrelerin her güncellemede ne kadar değiştirileceğini belirleyen bir hiperparametredir.

- Öğrenme oranı çok küçük olursa model yavaş öğrenir ve eğitim uzun sürer.
- Çok büyük olursa model en uygun noktayı geçebilir, kayıp değeri dalgalanabilir veya eğitim başarısız olabilir.
- Uygun bir değer seçildiğinde model daha dengeli şekilde öğrenir.

Bu nedenle öğrenme oranı, Gradient Descent’in başarısını doğrudan etkileyen önemli hiperparametrelerden biridir.

## Gradient Descent Türleri

### Batch Gradient Descent

Gradient hesaplanırken eğitim verilerinin tamamı kullanılır. Güncellemeler daha düzenli olabilir ancak büyük veri setlerinde çok fazla bellek ve işlem süresi gerektirir.

### Stochastic Gradient Descent (SGD)

Parametreler her seferinde tek bir eğitim örneği kullanılarak güncellenir. Daha az bellek gerektirir ve sık güncelleme yapar. Fakat tek tek örneklerden hesaplandığı için güncellemeler gürültülü olabilir ve kayıp değeri sürekli düzgün biçimde azalmayabilir.

### Mini-Batch Gradient Descent

Eğitim verileri küçük gruplara, yani batch’lere ayrılır. Her grubun ardından parametreler güncellenir. Batch Gradient Descent’in düzenliliği ile SGD’nin hız ve bellek avantajları arasında denge kurar. Günümüzde sinir ağlarının eğitiminde en sık kullanılan yaklaşım genellikle budur.

## Karşılaşılabilecek Sorunlar

Gradient Descent her zaman doğrudan en iyi sonuca ulaşamayabilir. Kayıp yüzeyinde yerel minimumlar, düz bölgeler veya eyer noktaları bulunabilir. Gradient çok küçük olduğunda öğrenme yavaşlayabilir. Gradient çok büyük olduğunda ise parametre güncellemeleri kararsız hâle gelebilir. Momentum ve Adam gibi gelişmiş optimizerlar bu sorunların bazılarını azaltmaya çalışır.

## Sonuç

Gradient, model hatasının parametrelere göre hangi yönde değiştiğini gösterir. Gradient Descent ise bu bilgiyi kullanarak ağırlık ve bias değerlerini hatayı azaltacak yönde günceller. Öğrenme oranı adım büyüklüğünü belirlerken Batch, Stochastic ve Mini-Batch yaklaşımları gradientin kaç veri örneğiyle hesaplanacağını belirler. Bu yapı, sinir ağlarının eğitim sürecinin temelini oluşturur.
