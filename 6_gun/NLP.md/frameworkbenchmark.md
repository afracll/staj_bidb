# Yapay Zekâda Kullanılan Framework, Kütüphane ve SDK'ler

## Framework, Kütüphane ve SDK Nedir?

Yapay zekâ projeleri geliştirirken her işlemi sıfırdan yazmak yerine hazır araçlardan yararlanırız. Bu araçlar kütüphane, framework veya SDK olarak karşımıza çıkabilir.

- **Kütüphane**, belirli işlemleri yapmamızı sağlayan hazır kodların bulunduğu yapıdır. NumPy ve scikit-learn buna örnek verilebilir.
- **Framework**, model oluşturma, eğitme ve test etme sürecinin genel yapısını sağlar. PyTorch ve TensorFlow birer yapay zekâ framework'üdür.
- **SDK**, belirli bir sistem veya donanım için geliştirme yapmayı sağlayan araçların bütünüdür. İçinde kütüphaneler ve yardımcı geliştirme araçları bulunabilir. NVIDIA TensorRT buna örnek olarak verilebilir.

Bu kavramlar birbirine yakın olsa da aynı anlama gelmez. Örneğin PyTorch ile bir model eğitilebilirken TensorRT daha çok eğitilmiş bir modeli NVIDIA ekran kartında hızlı çalıştırmak için kullanılır.

## Yapay Zekâda Sık Kullanılan Araçlar

### PyTorch

PyTorch, sinir ağları geliştirmek ve eğitmek için kullanılan açık kaynaklı bir derin öğrenme framework'üdür. Python ile uyumlu ve esnek bir yapıya sahiptir. Modelin eğitim adımlarını daha açık biçimde görebildiğimiz için özellikle araştırmalarda, özel model geliştirmede ve NLP çalışmalarında sık kullanılır.

### TensorFlow

TensorFlow, Google tarafından geliştirilen açık kaynaklı bir makine öğrenmesi framework'üdür. Model oluşturma ve eğitmenin yanında modeli sunucuda, mobil cihazda veya farklı ortamlarda çalıştırmak için de çeşitli araçlar sunar.

### Keras

Keras, derin öğrenme modellerini daha kolay ve daha az kodla oluşturmayı sağlayan üst seviye bir API'dir. Özellikle yeni başlayanlar için kullanımı daha kolaydır. Güncel Keras 3; TensorFlow, PyTorch veya JAX üzerinde çalışabilir. Keras ve TensorFlow aynı şey değildir; Keras model yazmayı kolaylaştıran bir arayüzdür.

### JAX

JAX, sayısal hesaplamalar ve otomatik türev alma işlemleri için kullanılan bir kütüphanedir. Özellikle yüksek performans gerektiren araştırmalarda ve TPU kullanılan projelerde tercih edilebilir. Başlangıçta PyTorch ve Keras'a göre öğrenilmesi biraz daha zor olabilir.

### scikit-learn

scikit-learn, klasik makine öğrenmesi projelerinde kullanılan bir Python kütüphanesidir. Doğrusal regresyon, karar ağaçları, kümeleme, veri ön işleme ve model değerlendirme gibi işlemler için uygundur. Her problemde derin öğrenme kullanmak gerekmediği için tablo verilerinde çoğu zaman scikit-learn ile başlamak daha mantıklıdır.

### Hugging Face Transformers

Hugging Face Transformers; BERT gibi Transformer modellerini hazır olarak kullanmayı ve eğitmeyi kolaylaştıran bir kütüphanedir. Metin sınıflandırma, soru cevaplama, çeviri ve büyük dil modeli çalışmalarında kullanılır.

## PyTorch ve TensorFlow/Keras Karşılaştırması

| Özellik | PyTorch | TensorFlow/Keras |
|---|---|---|
| Kullanım kolaylığı | Python'a yakın ve anlaşılırdır ancak özel eğitim döngülerinde daha fazla kod yazılabilir. | Keras sayesinde daha az kodla hızlı model kurulabilir. |
| Esneklik | Özel modeller ve deneysel çalışmalar için oldukça esnektir. | Standart modelleri hızlı geliştirmek için uygundur. |
| Hata ayıklama | Modelin adımları açık olduğu için hataları takip etmek genellikle kolaydır. | Keras kullanıldığında birçok işlem arka planda yapılır. |
| NLP ve büyük dil modelleri | Hugging Face ile birlikte çok sık kullanılır. | NLP modellerinde kullanılabilir fakat güncel açık kaynak örneklerde PyTorch daha yaygındır. |
| Üretime alma | Sunucu, ONNX, TensorRT ve ExecuTorch gibi seçenekleri vardır. | TensorFlow Serving, LiteRT ve TensorFlow.js gibi araçlar sunar. |
| Başlangıç için | Temel eğitim mantığını ayrıntılı öğrenmek isteyenler için uygundur. | Kısa sürede çalışan bir model oluşturmak isteyenler için uygundur. |

Buradan PyTorch yalnızca araştırmada, TensorFlow ise yalnızca üretimde kullanılır sonucu çıkarılmamalıdır. İki framework de farklı alanlarda kullanılabilir. Seçim yaparken projenin ihtiyacına ve ekibin bildiği araçlara bakılır.

## Basit Benchmark Karşılaştırması

Benchmark, araçların aynı görevdeki hızını ve başarısını karşılaştırmak için yapılan ölçümdür. Karşılaştırmanın adil olması için aynı veri seti, model, batch size ve donanım kullanılmalıdır.

Keras ekibinin yayımladığı açık bir çalışmada aynı Keras modelleri; TensorFlow, JAX ve PyTorch backend'leriyle NVIDIA A100 GPU üzerinde çalıştırılmıştır. Aşağıdaki değerler bir adımın kaç milisaniye sürdüğünü göstermektedir. Değer küçüldükçe işlem daha hızlıdır.

| Model ve işlem | TensorFlow | JAX | PyTorch eager |
|---|---:|---:|---:|
| Segment Anything – eğitim | 355,25 ms | 361,69 ms | 1.388,87 ms |
| Stable Diffusion – eğitim | 392,24 ms | 391,21 ms | 823,44 ms |
| BERT – eğitim | 214,49 ms | 222,37 ms | 808,68 ms |

Bu çalışmada TensorFlow ve JAX birbirine yakın sonuçlar verirken PyTorch'un eager çalışma şekli daha yavaş kalmıştır. Ancak bu sonuç, PyTorch'un her projede daha yavaş olduğu anlamına gelmez. Çünkü hız; modele, donanıma, batch size değerine ve kullanılan ayarlara göre değişebilir. Ayrıca burada PyTorch'un derlenmiş hâli değil, eager modu ölçülmüştür. Bu nedenle tek bir benchmark sonucuna bakarak kesin bir framework sıralaması yapmak doğru değildir.

## Hangi Projede Hangisi Kullanılmalıdır?

| Proje türü | Tercih edilebilecek araç | Nedeni |
|---|---|---|
| Regresyon, karar ağacı, kümeleme ve tablo verileri | **scikit-learn** | Klasik makine öğrenmesi için kolay ve yeterlidir. |
| Derin öğrenmeye giriş ve hızlı model oluşturma | **Keras/TensorFlow** | Daha az kodla model oluşturulabilir. |
| Özel sinir ağı ve araştırma projesi | **PyTorch** | Modelin eğitim sürecinde daha fazla kontrol sağlar. |
| NLP ve büyük dil modeli projesi | **PyTorch + Hugging Face** | Çok sayıda hazır Transformer modeli ve örneği bulunur. |
| TPU kullanılan araştırma | **JAX veya TensorFlow** | TPU ve yüksek performanslı hesaplamalar için uygundur. |
| Modeli farklı sistemlerde çalıştırma | **ONNX Runtime** | Farklı framework'lerde oluşturulan modelleri ortak bir biçimde çalıştırabilir. |
| NVIDIA GPU üzerinde hızlı tahmin | **TensorRT** | Eğitilmiş modeli NVIDIA GPU için optimize eder. |
| Mobil ve edge cihazlar | **LiteRT veya ExecuTorch** | Modelleri telefon ve gömülü cihazlarda çalıştırmak için kullanılır. |

## Sonuç

PyTorch ve TensorFlow en sık kullanılan derin öğrenme framework'leri arasındadır. PyTorch esnekliği ve modelin eğitim adımlarını daha açık göstermesiyle öne çıkarken TensorFlow/Keras daha kısa kodla hızlı model geliştirmeyi kolaylaştırır. JAX daha çok performans ve araştırma odaklı çalışmalarda, scikit-learn ise klasik makine öğrenmesi problemlerinde kullanılabilir.

Bir aracın her projede en iyi olması mümkün değildir. Kullanılacak teknoloji; verinin türüne, oluşturulacak modele, kullanılacak donanıma ve modelin nerede çalıştırılacağına göre seçilmelidir. NLP ve büyük dil modelleri üzerinde çalışmak isteyen biri için PyTorch ve Hugging Face öğrenmek uygun bir başlangıç olabilir.
