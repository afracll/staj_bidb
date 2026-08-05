# Geri Yayılım (Backpropagation) Nedir?

Geri yayılım, yapay sinir ağlarını eğitmek için kullanılan temel algoritmalardan biridir. Modelin yaptığı tahmin hatasını ağın çıkışından girişine doğru geriye taşıyarak her ağırlığın ve bias değerinin hataya ne kadar katkı sağladığını hesaplar.

Bu bilgiler kullanılarak modelin parametreleri güncellenir ve tahmin hatası azaltılmaya çalışılır. Kısaca geri yayılım, sinir ağına **hangi parametreyi ne yönde değiştirmesi gerektiğini** gösterir.

## Geri Yayılıma Neden İhtiyaç Duyulur?

Bir sinir ağı eğitim sırasında tahmin üretir ancak ilk tahminleri genellikle doğru değildir. Loss function, tahminle gerçek sonuç arasındaki hatayı hesaplar. Fakat yalnızca hatanın değerini bilmek yeterli değildir. Bu hatayı azaltmak için ağdaki çok sayıdaki ağırlık ve bias değerinden hangilerinin nasıl değiştirilmesi gerektiğinin de bulunması gerekir.

Geri yayılım:

- Loss değerinin her ağırlığa göre değişimini hesaplar.
- Hatanın hangi katmanlardan ve parametrelerden kaynaklandığını belirler.
- Ağırlıkların ve bias değerlerinin güncellenmesini sağlar.
- Sinir ağının eğitim boyunca hatalarından öğrenmesine yardımcı olur.

## Geri Yayılım Nasıl Çalışır?

Sinir ağının eğitimi genel olarak iki temel geçişten oluşur.

### 1. İleri Yayılım (Forward Pass)

İleri yayılım sırasında giriş verileri ağın katmanlarından geçirilir:

1. Veriler giriş katmanına verilir.
2. Her nöron girdileri ağırlıklarla çarpar ve bias değerini ekler.
3. Elde edilen değer aktivasyon fonksiyonundan geçirilir.
4. Bir katmanın çıktısı sonraki katmanın girdisi olur.
5. Çıkış katmanı modelin tahminini üretir.

Örneğin bir e-postanın spam olup olmadığını tahmin eden model, ileri yayılım sonunda e-postanın spam olma olasılığını üretebilir.

### 2. Geri Yayılım (Backward Pass)

Modelin tahmini üretildikten sonra bu sonuç gerçek cevapla karşılaştırılır ve loss function ile hata hesaplanır. Daha sonra hata çıkış katmanından giriş katmanına doğru geriye taşınır.

Geriye doğru ilerlerken algoritma, **zincir kuralını** kullanarak her ağırlığın loss değerini ne kadar etkilediğini hesaplar. Bu değişim miktarına **gradyan** denir.

Gradyanlar hesaplandıktan sonra optimizer, ağırlıkları ve bias değerlerini hatayı azaltacak yönde günceller. Bu işlem basitçe şöyle gösterilebilir:

```text
Yeni ağırlık = Eski ağırlık - (Öğrenme oranı × Gradyan)
```

Buradaki **öğrenme oranı**, ağırlıkların her güncellemede ne kadar değişeceğini belirleyen bir hiperparametredir.

## Eğitim Sürecinin Tekrarlanması

İleri ve geri yayılım işlemleri eğitim veri seti üzerinde birçok kez tekrarlanır:

1. Model bir tahmin üretir.
2. Loss function hatayı hesaplar.
3. Geri yayılım gradyanları bulur.
4. Optimizer parametreleri günceller.
5. Model yeni parametrelerle tekrar tahmin yapar.

Her tekrarda modelin tahminlerinin gerçek cevaplara biraz daha yaklaşması amaçlanır. Eğitim verisinin tamamının bir kez işlenmesine **epoch** denir. Model genellikle birden fazla epoch boyunca eğitilir.

## Basit Bir Örnek

Bir sinir ağının üretmesi gereken gerçek değer `0.50`, ilk tahmini ise `0.67` olsun. Loss function bu iki değer arasındaki hatayı hesaplar. Geri yayılım, bu hataya hangi ağırlıkların ne kadar katkı sağladığını bulur ve optimizer ağırlıkları günceller.

Yeni ağırlıklarla yapılan tahmin `0.61` değerine düşebilir. Sonuç hâlâ gerçek değere eşit olmadığı için aynı süreç tekrar edilir. Böylece model tahminini zamanla gerçek değere yaklaştırmaya çalışır.

## Geri Yayılımın Avantajları

- Sinir ağındaki çok sayıda parametrenin verimli şekilde güncellenmesini sağlar.
- Basit sinir ağlarından derin ve karmaşık modellere kadar kullanılabilir.
- CNN ve RNN gibi farklı sinir ağı türlerinin eğitilmesini destekler.
- Modelin hatalarından öğrenerek performansını geliştirmesini sağlar.
- Büyük veri setleri ve çok katmanlı ağlarla çalışabilir.

## Geri Yayılımın Karşılaşabileceği Sorunlar

### Kaybolan Gradyan

Derin ağlarda gradyanlar geriye doğru ilerlerken çok küçülebilir. Bu durumda ilk katmanlardaki ağırlıklar yeterince güncellenemez ve öğrenme yavaşlayabilir.

### Patlayan Gradyan

Gradyanlar aşırı büyürse ağırlık güncellemeleri kararsız hâle gelebilir ve modelin eğitimi bozulabilir.

### Overfitting

Model eğitim verilerini öğrenmek yerine ezberleyebilir. Bu durumda eğitim verisinde başarılı olurken daha önce görmediği verilerde kötü sonuç verebilir.

## Sonuç

Geri yayılım, sinir ağının yaptığı hatayı geriye doğru inceleyerek ağırlık ve bias değerlerinin nasıl güncellenmesi gerektiğini belirleyen bir eğitim algoritmasıdır. Forward pass sırasında tahmin üretilir, loss function hatayı hesaplar, backward pass gradyanları bulur ve optimizer parametreleri günceller.

Bu işlemlerin tekrar edilmesi sayesinde sinir ağı hatasını azaltmayı ve daha doğru tahminler üretmeyi öğrenir. Bu nedenle geri yayılım, modern sinir ağlarının eğitilmesindeki en önemli yöntemlerden biridir.
