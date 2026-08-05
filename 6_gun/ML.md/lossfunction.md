# LOSS FUNCTION (L)
Loss Function ve Cost Function

Makine öğrenmesi modelinin amacı, yaptığı tahminlerle gerçek sonuçlar arasındaki farkı mümkün olduğunca azaltmaktır. Ancak modelin ne kadar hata yaptığını ölçmeden iyi mi kötü mü çalıştığını anlayamayız. Bu nedenle loss function (kayıp fonksiyonu) ve cost function (maliyet fonksiyonu) kullanılır.

Neden Gereklidir?

Bir model eğitim sırasında verileri kullanarak tahmin üretir. Bu tahminler her zaman gerçek sonuçla aynı olmayabilir. Loss function, tahminle gerçek sonuç arasındaki hatayı sayısal olarak gösterir.

Bu hata ölçülmezse:

Modelin ne kadar başarılı olduğunu anlayamayız.

Modelin ağırlıklarının hangi yönde güncellenmesi gerektiğini bilemeyiz.

Modelin eğitim sırasında gelişip gelişmediğini takip edemeyiz.

Kayıp değeri yüksekse modelin tahmini kötüdür. Kayıp değeri azaldıkça modelin tahmini gerçek sonuca yaklaşır. Model eğitiminin temel amaçlarından biri bu değeri mümkün olduğunca küçültmektir.

Eğitim Sürecindeki Yeri

Loss function model eğitiminde şu şekilde kullanılır:

Model verileri girdi olarak alır.

Forward propagation ile bir tahmin üretir.

Tahmin edilen sonuç gerçek sonuçla karşılaştırılır.

Loss function modelin hatasını hesaplar.

Backpropagation, hatanın hangi ağırlıklardan kaynaklandığını belirler.

Optimizer, modelin ağırlıklarını hatayı azaltacak yönde günceller.

Bu işlemler eğitim boyunca tekrarlanır.

Kısaca süreç şu şekildedir:

Model tahmin yapar -> loss function hatayı ölçer -> backpropagation hatanın kaynağını belirler -> optimizer ağırlıkları günceller.

Loss ve Cost Arasındaki Fark

Kavramsal olarak loss, tek bir veri örneğinde yapılan hatayı; cost ise birden fazla örnekteki hataların ortalamasını ifade eder.

Örneğin model üç ev için tahmin yaptıysa her ev için ayrı bir loss değeri hesaplanabilir. Bu üç loss değerinin ortalaması ise cost değerini verir.

Loss Function

Cost Function

Tek bir veri örneğindeki hatayı ölçer.

Veri seti veya batch üzerindeki ortalama hatayı ölçer.

Bir tahmin için hesaplanır.

Birden fazla tahmin için hesaplanır.

Tek örneğe bağlı olduğu için daha fazla değişebilir.

Verilerin genelindeki hatayı gösterir.

TensorFlow ve PyTorch gibi modern kütüphanelerde loss ve cost kelimeleri çoğu zaman birbirinin yerine kullanılabilir. Ancak temel mantığı anlamak için bu ayrımı bilmek faydalıdır.

Regresyon Problemlerinde Loss Function

Regresyon problemlerinde model sayısal bir değer tahmin etmeye çalışır.

Örnekler:

Ev fiyatının tahmin edilmesi

Hava sıcaklığının tahmin edilmesi

Bir ürünün satış miktarının tahmin edilmesi

Bu problemlerde amaç, tahmin edilen sayı ile gerçek sayı arasındaki farkı azaltmaktır.

Mean Squared Error (MSE)

MSE, gerçek değerle tahmin arasındaki farkın karesini alır.

MSE = (Gerçek değer - Tahmin)²

Örneğin gerçek değer 100, modelin tahmini 90 ise:

(100 - 90)² = 100

Hatanın karesi alındığı için büyük hatalar daha sert cezalandırılır. MSE, kolay optimize edilebildiği için makine öğrenmesinde sık kullanılır. Ancak aykırı değerlerden fazla etkilenebilir.

Örneğin normal ev fiyatlarının arasında yanlışlıkla çok yüksek bir fiyat bulunuyorsa MSE bu değere fazla önem verebilir ve model bundan ciddi şekilde etkilenebilir.

Mean Absolute Error (MAE)

MAE, gerçek değerle tahmin arasındaki farkın mutlak değerini alır.

MAE = |Gerçek değer - Tahmin|

Gerçek değer 100, tahmin 90 ise:

|100 - 90| = 10

MAE hatanın karesini almadığı için büyük hataları MSE kadar büyütmez. Bu nedenle aykırı değerlere karşı daha dayanıklıdır. Ancak bazı durumlarda modelin öğrenmesi MSE'ye göre daha yavaş olabilir.

Huber Loss

Huber Loss, MSE ve MAE'nin özelliklerini birleştiren dengeli bir yöntemdir.

Küçük hatalarda MSE gibi davranır.

Büyük hatalarda MAE gibi davranır.

Böylece model küçük hataları düzgün şekilde azaltırken aykırı değerlerden MSE kadar fazla etkilenmez. MSE'nin fazla hassas, MAE'nin ise yavaş kaldığı durumlarda tercih edilebilir.

Root Mean Squared Error (RMSE)

RMSE, MSE değerinin karekökünün alınmış hâlidir.

RMSE = √MSE

En önemli avantajı, sonuç değerinin tahmin edilen değişkenle aynı birimde olmasıdır. Örneğin ev fiyatı tahmininde RMSE kullanılarak “Model ortalama 200.000 TL hata yapıyor.” şeklinde kolay bir yorum yapılabilir. Bu nedenle model sonuçlarını raporlarken sık kullanılır.

Regresyon İçin Kısa Karşılaştırma

Durum

Tercih Edilebilecek Yöntem

Büyük hataların daha sert cezalandırılması isteniyorsa

MSE

Veride aykırı değerler bulunuyorsa

MAE

MSE ve MAE arasında denge isteniyorsa

Huber Loss

Hatanın gerçek birimiyle yorumlanması isteniyorsa

RMSE

Sınıflandırma Problemlerinde Loss Function

Sınıflandırma problemlerinde model sayısal bir değer tahmin etmek yerine verinin hangi sınıfa ait olduğunu belirlemeye çalışır.

Örnekler:

Spam / spam değil

Hasta / sağlıklı

Dolandırıcılık / normal işlem

Kedi / köpek / at

Sınıflandırmada yalnızca doğru sınıfın seçilmesi değil, modelin doğru sınıfa ne kadar olasılık verdiği de önemlidir.

Örneğin gerçek sınıf “kedi” ise modelin kediye %51 olasılık vermesiyle %99 olasılık vermesi teknik olarak doğru sınıfı seçebilir. Ancak ikinci tahmin doğru sınıfa daha yüksek olasılık vermiştir.

Sınıflandırmada kullanılan cross-entropy fonksiyonları:

Doğru sınıfa yüksek olasılık verilmesini destekler.

Doğru sınıfa düşük olasılık verilmesini cezalandırır.

Yanlış ve çok emin tahminlere daha büyük kayıp değeri verir.

Binary Cross-Entropy

Binary Cross-Entropy, yalnızca iki sınıf bulunan problemlerde kullanılır.

Örnekler:

Spam / spam değil

Hasta / sağlıklı

Dolandırıcılık / normal işlem

Bu problemlerde gerçek etiket genellikle 0 veya 1 olur. Model, sigmoid aktivasyon fonksiyonu yardımıyla 0 ile 1 arasında bir olasılık üretir.

Örneğin gerçek e-posta spam ise:

Model 0.95 tahmini yaparsa loss düşük olur.

Model 0.10 tahmini yaparsa loss yüksek olur.

Çünkü ikinci durumda model gerçek sınıfa düşük olasılık vermiştir. Model yanlış sınıfa ne kadar emin şekilde yaklaşırsa aldığı ceza o kadar büyür.

Categorical Cross-Entropy

Categorical Cross-Entropy, ikiden fazla sınıf bulunan ve etiketlerin one-hot encoding biçiminde gösterildiği problemlerde kullanılır.

Örneğin dört sınıf şöyle gösterilebilir:

Kedi   = [1, 0, 0, 0]
Köpek  = [0, 1, 0, 0]
At     = [0, 0, 1, 0]
Maymun = [0, 0, 0, 1]

Model her sınıf için ayrı bir olasılık üretir:

Kedi:   0.80
Köpek:  0.10
At:     0.07
Maymun: 0.03

Bu olasılıklar genellikle softmax aktivasyon fonksiyonu kullanılarak elde edilir ve toplamları 1 olur. Categorical Cross-Entropy, modelin doğru sınıfa yüksek; diğer sınıflara ise düşük olasılık vermesini sağlamaya çalışır.

Sparse Categorical Cross-Entropy

Sparse Categorical Cross-Entropy de ikiden fazla sınıf bulunan problemlerde kullanılır. Categorical Cross-Entropy'den temel farkı etiketlerin gösterilme biçimidir.

Etiketler one-hot encoding yerine tam sayılarla gösterilir:

Kedi   = 0
Köpek  = 1
At     = 2
Maymun = 3

Bu yöntemde:

One-hot encoding yapılmasına gerek kalmaz.

Daha az bellek kullanılabilir.

Büyük veri setlerinde daha pratik olabilir.

Categorical Cross-Entropy ile Sparse Categorical Cross-Entropy aynı tür problemi çözebilir. Aralarındaki temel fark gerçek etiketlerin hazırlanma biçimidir.

Sınıflandırma İçin Kısa Karşılaştırma

Problem

Aktivasyon

Kayıp Fonksiyonu

İki sınıflı problem

Sigmoid

Binary Cross-Entropy

Çok sınıflı ve one-hot etiketli problem

Softmax

Categorical Cross-Entropy

Çok sınıflı ve tam sayı etiketli problem

Softmax

Sparse Categorical Cross-Entropy

Sonuç

Loss function, modelin yaptığı tahminin gerçek sonuçtan ne kadar farklı olduğunu ölçer. Eğitim sırasında optimizer ve backpropagation, bu kayıp değerinden yararlanarak modelin parametrelerini günceller. Modelin amacı loss değerini mümkün olduğunca azaltmaktır.

Regresyon problemlerinde MSE, MAE, Huber Loss ve RMSE; sınıflandırma problemlerinde ise Binary Cross-Entropy, Categorical Cross-Entropy ve Sparse Categorical Cross-Entropy kullanılabilir. Hangi kayıp fonksiyonunun seçileceği problemin türüne, verilerin yapısına ve etiketlerin nasıl gösterildiğine bağlıdır.