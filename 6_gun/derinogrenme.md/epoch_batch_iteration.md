# Derin Öğrenmede Epoch, Batch ve Iteration

Bir sinir ağı eğitilirken eğitim verileri modele belirli bir düzen içinde verilir. **Epoch**, **batch**, **batch size** ve **iteration** kavramları bu eğitim sürecinin nasıl ilerlediğini açıklar. Birbirleriyle bağlantılı olsalar da aynı şeyi ifade etmezler.

## Epoch Nedir?

Bir **epoch**, modelin eğitim veri setinin tamamını bir kez işlemesidir. Yani eğitimdeki bütün örnekler model tarafından bir defa görülünce bir epoch tamamlanmış olur.

Bu süreçte model:

1. Forward pass yaparak tahmin üretir.
2. Loss function ile tahmin hatasını hesaplar.
3. Backpropagation ile gradientleri bulur.
4. Optimizer yardımıyla ağırlık ve bias değerlerini günceller.

Bir epoch çoğu zaman modelin verilerdeki bütün ilişkileri öğrenmesi için yeterli olmaz. Bu nedenle eğitim birkaç epoch boyunca devam eder. Model aynı veri setini tekrar gördükçe ağırlıklarını yeniden düzenler ve hatasını azaltmaya çalışır.

Örneğin eğitim veri setinde 1.000 örnek varsa:

- **1 epoch:** Model 1.000 örneğin tamamını bir kez görür.
- **3 epoch:** Model aynı eğitim veri setini toplam üç kez işler. Böylece her örnek eğitim boyunca üç kez kullanılmış olur.

Bunu sınava çalışmaya benzetebiliriz. Bütün konuları bir kez tekrar etmek bir epoch, aynı konuların beş kez üzerinden geçmek ise beş epoch gibidir.

Epoch sayısı eğitim başlamadan önce belirlenen bir **hiperparametredir**. Çok az epoch seçilirse model yeterince öğrenemeyebilir. Çok fazla epoch seçilirse eğitim verisini ezberleyerek **overfitting** oluşturabilir. Bu nedenle eğitim ve validation kayıpları takip edilerek uygun epoch sayısı belirlenmelidir.

## Batch Nedir?

Bir **batch**, eğitim verilerinin model tarafından birlikte işlenen küçük bir bölümüdür. Büyük veri setlerinin tamamını aynı anda işlemek fazla bellek gerektirebilir. Bu nedenle veriler daha küçük gruplara ayrılır ve her grup sırayla modele verilir.

Model bir batch üzerinde forward pass ve backpropagation işlemlerini gerçekleştirir. Ardından optimizer, o batch’ten hesaplanan gradientleri kullanarak model parametrelerini günceller.

Örneğin 1.000 eğitim örneği 100’er örnekten oluşan gruplara ayrılırsa toplam 10 batch elde edilir.

## Batch Size Nedir?

**Batch size**, bir batch içerisinde kaç eğitim örneği bulunacağını belirten hiperparametredir.

Örneğin 1.000 örnekten oluşan bir veri setinde batch size 500 seçilirse veri iki batch’e ayrılır:

- Birinci batch: İlk 500 örnek
- İkinci batch: Kalan 500 örnek

İki batch de işlendiğinde veri setinin tamamı görülmüş olur ve bir epoch tamamlanır.

Batch size seçimi eğitim sürecini etkiler:

- **Küçük batch size:** Daha az bellek kullanır ve parametreler daha sık güncellenir. Ancak gradientler daha değişken olabilir.
- **Büyük batch size:** Hesaplamalar daha düzenli olabilir fakat daha fazla bellek gerektirir.

En uygun batch size değeri veri setine, modele ve kullanılan donanıma göre değişebilir.

## Iteration Nedir?

Bir **iteration**, modelin bir batch’i işleyerek parametrelerini bir kez güncellemesidir. Her iteration içinde genel olarak şu işlemler gerçekleşir:

1. Batch modele verilir.
2. Forward pass ile tahminler üretilir.
3. Kayıp değeri hesaplanır.
4. Backpropagation ile gradientler bulunur.
5. Optimizer ağırlık ve bias değerlerini günceller.

Kısaca **bir batch’in işlenmesi bir iteration**, bütün batch’lerin işlenmesi ise bir epoch anlamına gelir.

## Epoch, Batch ve Iteration Arasındaki İlişki

Bir epoch içindeki iteration sayısı şu şekilde hesaplanır:

```text
Bir epochtaki iteration sayısı = Eğitim örneği sayısı / Batch size
```

Bölme işlemi tam sonuç vermiyorsa son kalan örnekler de ayrı bir batch olarak işlenir. Bu nedenle sonuç yukarı yuvarlanır.

Toplam eğitim iteration sayısı ise şöyledir:

```text
Toplam iteration = Epoch sayısı × Bir epochtaki iteration sayısı
```

### Örnek

Eğitim veri setinde **1.000 örnek**, batch size değerinde **100** ve eğitimde **3 epoch** olduğunu düşünelim.

```text
Bir epochtaki batch sayısı = 1.000 / 100 = 10
Bir epochtaki iteration sayısı = 10
Toplam iteration sayısı = 3 × 10 = 30
```

Model her iteration sırasında 100 örneği işler ve parametrelerini günceller. 10 iteration tamamlanınca bütün veri seti bir kez işlenmiş olur ve ilk epoch biter. Bu süreç üç kez tekrarlandığında eğitim toplam 30 iteration sürer.

## Iteration Kullanmanın Önemi

Veriyi batch’lere ayırarak iterationlar hâlinde işlemek bazı avantajlar sağlar:

- Büyük veri setlerinin daha az bellekle eğitilmesini sağlar.
- Model parametreleri her batch sonrasında aşamalı olarak güncellenir.
- Büyük veri setleri ve modeller üzerinde eğitimi daha uygulanabilir hâle getirir.
- Mini-batch kullanımı GPU’ların paralel hesaplama gücünden yararlanmayı kolaylaştırır.

## Kısa Karşılaştırma

| Kavram | Anlamı |
| --- | --- |
| **Epoch** | Eğitim veri setinin tamamının bir kez işlenmesi |
| **Batch** | Birlikte işlenen küçük veri grubu |
| **Batch size** | Bir batch içindeki örnek sayısı |
| **Iteration** | Bir batch’in işlenmesi ve parametrelerin bir kez güncellenmesi |

## Sonuç

Epoch, modelin bütün eğitim verisini kaç kez gördüğünü; batch, verinin hangi küçük gruplara ayrıldığını; batch size, bu gruplarda kaç örnek bulunduğunu; iteration ise modelin kaç defa parametre güncellemesi yaptığını belirtir. Bu kavramlar eğitim süresini, bellek kullanımını ve modelin öğrenme biçimini doğrudan etkiler.
