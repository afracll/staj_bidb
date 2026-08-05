# MACHINE LEARNING
Amaç geçmiş verilere bakarak yeni örnekler üzerinde tahmin veya karar verebilen modeller
geliştirmektir.

Makine öğrenmesi üç temel türe ayrılıyor:

- Denetimli Öğrenme
Denetimli öğrenmede model, doğru cevapları önceden verilmiş yani etiketlenmiş verilerle eğitilir. Model, girdilerle doğru sonuçlar arasındaki ilişkiyi öğrenerek yeni veriler için tahmin yapar.

- Denetimsiz Öğrenme
Denetimsiz öğrenmede verilerin önceden belirlenmiş etiketleri bulunmaz. Model, verilerdeki benzerlikleri ve gizli ilişkileri kendi başına bulmaya çalışır.

- Pekiştirmeli Öğrenme
Pekiştirmeli öğrenmede sistem, yaptığı eylemler sonucunda ödül veya ceza alır. Zaman içinde hangi davranışların daha iyi sonuç verdiğini öğrenir. Oyun oynayan yapay zekâlar ve bazı robot sistemleri bu yöntemi kullanabilir.

## model nedir?
veriden öğrenilen ve girdi (input) alıp çıktı (output) üreten bir matematiksel fonksiyondur. fonksiyonun tam olarak ne yaptığını veriden öğreniyoruz, biz elle yazmıyoruz.

örnek: fiyat= a x metrekare + b x odasayısı + c
bu ev fiyatı tahmini yapan bir model.
burada a b c sayıları modelin öğrendiği şeyler. model: aslında bu formulun kendisi ve öğrenilmiş katsayılar oluyor.

### model türleri 
- doğrusal regresyon: veriler arasında basit ve doğrusal bir ilişki kurar

- karar ağaçları: bir sonuca ulasmak için veriye art arda sorular sorar. cevaplara göre farklı dallardan ilerleyerek tahmin üretir. doğrusal olmayan ilişkileri de öğrenebilir.

- yapay sinir ağları: insan beyninden esinlenir. birbirine bağlı çok sayıda yapay nörondan oluşur. veriyi katmanlar boyunca işler ve daha karmaşık ilişkileri öğrenir. görüntü tanıma, ses işleme, dil işleme...

- transformer: bir tür yapay sinir ağı mimarisidir. özellikle bir veri dizisinin parçaları arasındaki ilişkileri anlamakta başarılı. bir cümledeki kelimeleri incelerken hangi kelimenin diğer kelimelerle daha yakından ilişkili olduğuna 'attention' mekanizmasıyla dikkat eder. GPT gibi büyük dil modelleri Transformer mimarisini kullanır. Önceki kelimelere veya token’lara bakarak sıradaki token’ın olasılığını tahmin eder.

### Model karmaşıklaştıkça:
Daha zor ilişkileri öğrenebilir.
Görüntü ve metin gibi karmaşık verileri işleyebilir.
Daha fazla veriye ve işlem gücüne ihtiyaç duyar.
Nasıl karar verdiğini açıklamak zorlaşabilir.
Aşırı öğrenme riski artabilir.

Bu nedenle en karmaşık model her zaman en iyi model değildir. Basit bir problemde doğrusal regresyon yeterliyse transformer kullanmak gereksizdir. Model, problemin ve verinin yapısına göre seçilir.


# PARAMETRELER

bir model, model parametreleri ile tanımlanır/temsil edilir. bir modeli eğitme süreci, öğrenme algoritmasının girdi özelliklerini (bağımsız değişkenler) etiketlere veya hedeflere (bağımlı değişken) doğru şekilde eşleştiren en uygun parametreleri öğrenmek için kullanacağı en uygun hiperparametrelerin seçilmesini içerir, böylece bir tür zeka elde edilir.

## Hiperparametreler

- makine öğrenimi ve derin öğrenmede eğitim başlamadan önce değerlerini belirlediğiniz veya yapılandırmasını seçtiğiniz ve eğitim bittiğinde değerleri veya yapılandırması aynı kalan her şey bir hiperparametredir.

- değerleri öğrenme sürecini kontrol eden ve bir öğrenme algoritmasının sonunda öğrendiği model parametrelerinin değerlerini belirleyen parametrelerdir. Hyper_ ön eki, bunların öğrenme sürecini ve bunun sonucunda ortaya çıkan model parametrelerini kontrol eden üst düzey parametreler olduğunu gösterir.

- bir model tasarlarken, modelin eğitimi başlamadan önce öğrenme algoritmanızın kullanacağı hiperparametre değerlerini seçer ve ayarlarız. hiperparametreler modelin dışındadır, çünkü model öğrenme/eğitim sırasında değerlerini değiştiremez.

- öğrenme algoritması öğrenme sürecinde kullanılır ancak ortaya çıkan modelin bir parçası değildir. öğrenme sürecinin sonunda eğitilmiş model parametrelerine sahip oluruz ve buna model diyoruz. örneğin, bir modeli eğitmek için hangi hiperparametre değerlerinin kullanıldığını modelin kendisinden bilemeyiz, sadece öğrenilen model parametrelerini biliriz.

örnekler:
- Öğrenme oranı (learning rate): Modelin eğitim sırasında ağırlıklarını ne kadar değiştireceğini belirler. Örneğin 0.01.
- Epoch sayısı: Modelin eğitim verisinin tamamını kaç kez göreceğini belirler. Örneğin 20 epoch, bütün eğitim verisinin 20 kez işlenmesi anlamına gelir.

## Parametreler

- makine öğrenimi ve derin öğrenmedeki parametreler, öğrenme algoritmanızın öğrenme sürecinde bağımsız olarak değiştirebileceği değerlerdir ve bu değerler, sağladığınız hiperparametrelerin seçiminden etkilenir. eğitim başlamadan önce hiperparametreleri ayarlarsınız ve öğrenme algoritması bu parametreleri öğrenmek için bunları kullanır.

- parametreler modelin içsel bileşenleridir. kullanılan algoritma, girdi özellikleriyle etiketler veya hedefler arasındaki eşlemeyi öğrenmeye çalışırken parametreler eğitim sırasında tamamen verilerden öğrenilir veya tahmin edilir.

- model eğitimi genellikle parametrelerin bazı değerlere (rastgele değerler veya sıfıra ayarlanmış) başlatılmasıyla başlar. eğitim/öğrenme ilerledikçe başlangıç değerleri bir optimizasyon algoritması (örneğin gradyan inişi) kullanılarak sürekli olarak güncellenir.

- öğrenme sürecinin sonunda model parametreleri, modelin kendisini oluşturur.

- bu nedenle doğru hiperparametre değerlerini ayarlamak çok önemlidir çünkü bu değerler model eğitimi sırasında kullanılır ve modelin performansını doğrudan etkiler. modeliniz için en iyi hiperparametreleri seçme işlemine hiperparametre ayarlaması denir.

# EĞİTİM (TRAINING)

## Eğitim (Training) Nedir?

- Makine öğrenmesinde eğitim, modelin kendisine verilen verilerden ilişkileri ve örüntüleri öğrenme sürecidir. Eğitim başlamadan önce modelin parametreleri genellikle rastgele değerlerle başlatılır. Model eğitim verilerini kullanarak bir tahmin yapar ve yaptığı tahmin gerçek sonuçla karşılaştırılır.

- Tahmin ile gerçek sonuç arasındaki fark, kayıp fonksiyonu kullanılarak hesaplanır. Daha sonra optimizasyon algoritması bu hatayı azaltmak için modelin parametrelerini günceller. Bu işlem eğitim verileri üzerinde birçok kez tekrarlanır.

Örneğin bir modele evlerin büyüklükleri ve fiyatları verildiğinde model, evin büyüklüğüyle fiyatı arasındaki ilişkiyi öğrenmeye çalışır. Eğitim tamamlandığında model, daha önce görmediği bir evin fiyatını tahmin edebilir.

- Kısaca eğitim, modelin verilerden öğrenerek parametrelerini en uygun değerlere getirmeye çalıştığı süreçtir. Eğitimden sonra modelin gerçekten öğrenip öğrenmediği, daha önce görmediği test verileri kullanılarak değerlendirilir.
