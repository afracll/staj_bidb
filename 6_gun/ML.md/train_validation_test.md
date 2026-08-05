# Training, Validation ve Test Veri Setleri

Makine öğrenmesinde bir modelin yalnızca gördüğü verilerde değil, daha önce görmediği verilerde de başarılı olması beklenir. Modelin yeni veriler üzerinde de doğru tahmin yapabilmesine **genelleme (generalization)** denir.

Modeli eğitmek ve değerlendirmek için aynı verilerin kullanılması doğru değildir. Çünkü model eğitim verilerini ezberleyebilir ve bu verilerde başarılı görünmesine rağmen yeni verilerde başarısız olabilir. Bu duruma **aşırı öğrenme (overfitting)** denir. Modelin gerçek performansını daha doğru değerlendirebilmek için veri seti training, validation ve test olmak üzere üç bölüme ayrılır.

## Training Set - Eğitim Verisi

Training set, modeli eğitmek için kullanılan veri grubudur. Model, bu verilerdeki özelliklerle doğru sonuçlar arasındaki ilişkileri öğrenir ve parametrelerini günceller.

Örneğin kedileri ve köpekleri ayıran bir model geliştirdiğimizi düşünelim. Hayvanların ağırlık ve tüylülük bilgileri modele verilir. Model, training set içindeki örneklerden yararlanarak kedilerle köpekleri ayıran ilişkileri öğrenmeye çalışır.

Eğitim verisinin gerçek hayattaki verileri mümkün olduğunca iyi temsil etmesi gerekir. Çünkü eğitim verisindeki hatalar veya yanlılıklar model tarafından da öğrenilebilir.

## Validation Set - Doğrulama Verisi

Validation set, farklı modelleri ve hiperparametreleri karşılaştırmak için kullanılan veri grubudur. Model doğrudan bu verilerle eğitilmez. Training set ile eğitilen modeller validation set üzerinde denenir ve hangisinin daha başarılı olduğuna karar verilir.

Kedi ve köpek örneğinde farklı modeller oluşturabiliriz:

- Yalnızca ağırlığı kullanan model
- Yalnızca tüylülüğü kullanan model
- Ağırlık ve tüylülüğü birlikte kullanan model

Bu modeller training set ile eğitildikten sonra validation set üzerindeki sonuçları karşılaştırılır. Böylece en uygun model ve hiperparametreler seçilir.

Model seçimini yalnızca training set sonuçlarına göre yapmak doğru değildir. Çünkü model bu verileri daha önce görmüş ve bunlardan öğrenmiştir. Validation set, modelin görmediği ayrı veriler üzerindeki başarısını kontrol etmemizi sağlar.

## Test Set - Test Verisi

Test set, geliştirilmesi tamamlanan modelin son performansını ölçmek için kullanılır. Model eğitim sırasında test verilerini görmez. Bu veri grubu, modelin gerçek hayatta karşılaşabileceği yeni verilerde nasıl çalışabileceğini anlamamıza yardımcı olur.

Test set model seçmek veya hiperparametre ayarlamak için kullanılmamalıdır. Test sonuçlarına model seçilmeden önce bakılır ve model buna göre değiştirilirse test verilerine de uyum sağlanmış olur. Bu durumda test sonucu modelin gerçek performansını güvenilir şekilde göstermez.

Bu nedenle test set yalnızca en uygun model ve hiperparametreler validation set yardımıyla seçildikten sonra, son değerlendirme için kullanılmalıdır.

## Training, Validation ve Test Arasındaki Fark

| Veri Grubu | Kullanım Amacı |
|---|---|
| Training set | Modelin eğitilmesi ve ilişkileri öğrenmesi |
| Validation set | Model ve hiperparametrelerin seçilmesi |
| Test set | Seçilen modelin son performansının ölçülmesi |

Kısaca:

> **Training set ile model öğrenir, validation set ile en uygun model seçilir, test set ile seçilen modelin son performansı ölçülür.**

## Sonuç

Training, validation ve test verilerinin ayrı tutulması, modelin eğitim verilerini ezberlemek yerine daha önce görmediği verilere de doğru tahminler yapabilmesi için önemlidir. Training set modelin öğrenmesini, validation set uygun modelin seçilmesini, test set ise seçilen modelin son kez değerlendirilmesini sağlar.
