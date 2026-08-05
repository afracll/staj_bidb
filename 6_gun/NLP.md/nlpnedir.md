# Doğal Dil İşleme (NLP) Nedir?

## NLP’nin Tanımı

**Doğal Dil İşleme (Natural Language Processing – NLP)**, bilgisayarların insanların kullandığı dili işlemesini sağlayan yapay zekâ alanıdır. Yazılı metinlerin yanında konuşma diliyle de ilgilenir. Temel amacı bilgisayarların insan dilini analiz edebilmesi, anlamla ilgili çıkarımlar yapabilmesi ve gerektiğinde yeni metin veya konuşma üretebilmesidir.

NLP; bilgisayar bilimi, yapay zekâ, makine öğrenmesi ve dil biliminin birleşiminden oluşur. İnsan dili bilgisayarlar için doğrudan anlaşılabilir değildir. Bilgisayarlar sayılarla çalıştığı için kelimelerin, cümlelerin ve metinlerin önce sayısal bir biçime dönüştürülmesi gerekir. NLP sistemleri bu sayısal gösterimleri kullanarak dildeki yapı, anlam, bağlam ve ilişkileri öğrenmeye çalışır.

NLP tek bir algoritma veya model değildir. Dil ile ilgili birçok problemi kapsayan geniş bir çalışma alanıdır. Basit bir spam filtresi de gelişmiş bir sohbet modeli de NLP alanına girebilir.

## NLP’nin İki Temel Yönü

NLP genel olarak dili anlama ve dil üretme olmak üzere iki temel yönde incelenebilir.

### Doğal Dil Anlama (NLU)

**Natural Language Understanding (NLU)**, verilen bir metnin veya konuşmanın ne anlatmak istediğini belirlemeye çalışır. Duygu analizi, metin sınıflandırma, kişinin amacını anlama ve metindeki kişi veya yer adlarını bulma gibi görevler NLU kapsamına girer.

### Doğal Dil Üretme (NLG)

**Natural Language Generation (NLG)**, bilgisayarın anlaşılır ve anlamlı dil üretmesidir. Bir soruya cevap verme, metin özetleme, çeviri yapma veya yeni bir içerik oluşturma NLG örnekleridir.

ChatGPT gibi büyük dil modelleri hem kullanıcının yazdığı metni işlediği hem de yeni bir cevap ürettiği için NLU ve NLG özelliklerini birlikte kullanır.

## NLP Ne İşe Yarar?

Günümüzde e-postalar, müşteri yorumları, sosyal medya gönderileri, haberler, sağlık kayıtları ve şirket belgeleri gibi büyük miktarda metin verisi üretilmektedir. Bu verilerin çoğu yapılandırılmamış olduğu için klasik veri tabloları gibi doğrudan analiz edilemez. NLP, metinleri işleyerek bu verilerden anlamlı bilgi çıkarılmasını sağlar.

NLP sayesinde bilgisayarlar:

- Metnin konusunu belirleyebilir.
- Yazının olumlu, olumsuz veya tarafsız olduğunu tahmin edebilir.
- Metindeki kişi, kurum, konum ve tarihleri bulabilir.
- Bir metni başka bir dile çevirebilir.
- Uzun belgeleri özetleyebilir.
- Kullanıcının sorusuna cevap verebilir.
- Benzer anlamdaki metinleri eşleştirebilir.
- İnsan diline benzeyen yeni içerikler oluşturabilir.

Örneğin “Ayşe aldığı yeni telefondan çok memnun” cümlesini inceleyen bir NLP sistemi:

- “Ayşe” kelimesini kişi adı olarak belirleyebilir.
- “Telefon” kelimesinin bir ürün olduğunu anlayabilir.
- Cümlenin olumlu duygu taşıdığını tahmin edebilir.
- Metnin bir ürün değerlendirmesiyle ilgili olduğunu belirleyebilir.

## NLP Nasıl Çalışır?

Bir NLP projesinin çalışma biçimi kullanılan yönteme ve modele göre değişebilir. Ancak genel süreç şu adımlardan oluşur.

### 1. Metin veya Konuşmanın Alınması

Sistem ilk olarak kullanıcı mesajı, belge, sosyal medya paylaşımı veya e-posta gibi yazılı bir veri alır. Girdi ses biçimindeyse önce konuşma tanıma yöntemiyle yazıya çevrilebilir. Böylece sonraki işlemler metin üzerinde gerçekleştirilir.

### 2. Metnin Hazırlanması

Ham metinler model tarafından işlenmeden önce belirli işlemlerden geçirilebilir:

- **Text normalization:** Gereksiz karakterleri düzenlemek ve metni standart hâle getirmek
- **Tokenization:** Metni kelime, alt kelime veya cümle gibi küçük parçalara ayırmak
- **Case folding:** Büyük ve küçük harfleri aynı biçime dönüştürmek
- **Stop word removal:** “ve”, “ile”, “bir” gibi çok sık kullanılan bazı kelimeleri çıkarmak
- **Stemming:** Kelimeyi yaklaşık kök biçimine indirmek
- **Lemmatization:** Kelimeyi dil bilgisine uygun sözlük biçimine çevirmek

Bu işlemlerin hepsi her projede kullanılmaz. Özellikle klasik NLP yöntemlerinde stop word çıkarma, stemming ve lemmatization sık kullanılır. Transformer tabanlı modern modellerde ise cümlenin bağlamını korumak önemli olduğu için kelimeleri doğrudan silmek yerine çoğunlukla alt kelime tabanlı tokenization uygulanır. Yani ön işleme yöntemi kullanılan modele göre seçilmelidir.

### 3. Dilin Yapısının ve Anlamının İncelenmesi

NLP sistemleri metni farklı yönlerden analiz edebilir:

- Kelimelerin isim, fiil veya sıfat gibi görevlerini belirleyebilir.
- Cümledeki kelimelerin birbirleriyle ilişkisini inceleyebilir.
- Bir kelimenin hangi anlamda kullanıldığını bağlamdan tahmin edebilir.
- Kişi, şehir, kurum ve tarih gibi varlıkları tespit edebilir.
- Metnin duygusunu veya kullanıcının amacını belirleyebilir.

Örneğin “yüz” kelimesi “denizde yüz” ve “insan yüzü” ifadelerinde farklı anlamlara gelir. NLP sistemi doğru anlamı çevresindeki kelimelerden çıkarmaya çalışır.

### 4. Metnin Sayısal Olarak Temsil Edilmesi

Bilgisayarlar kelimeleri doğrudan anlayamadığı için metinlerin sayılara dönüştürülmesi gerekir.

Klasik yöntemlerde **Bag of Words** kelimelerin kaç kez geçtiğini, **TF-IDF** ise bir kelimenin belge için ne kadar önemli olduğunu gösterir. Bu yöntemler kullanışlıdır ancak kelimelerin sırasını ve bağlamını sınırlı şekilde temsil eder.

Daha modern yöntemlerde **word embedding** kullanılarak kelimeler yoğun sayısal vektörlerle gösterilir. Benzer anlam taşıyan kelimelerin vektörleri de birbirine yakın olabilir. Transformer modellerindeki **contextual embedding** yaklaşımında ise bir kelimenin sayısal temsili bulunduğu cümleye göre değişir. Böylece aynı kelimenin farklı cümlelerdeki farklı anlamları daha iyi temsil edilebilir.

### 5. Modelin Eğitilmesi

Sayısal hâle getirilen metinler bir makine öğrenmesi veya derin öğrenme modeline verilir. Model, eğitim verilerindeki örüntüleri öğrenerek bir görev gerçekleştirmeye çalışır.

Örneğin duygu analizi modeline olumlu, olumsuz ve tarafsız olarak etiketlenmiş yorumlar verilebilir. Model, eğitim sırasında tahmin yapar; loss function ile hatasını ölçer ve optimizer yardımıyla parametrelerini günceller. Eğitim tamamlandığında daha önce görmediği bir yorumun duygusunu tahmin edebilir.

Modern büyük dil modelleri çok büyük miktarda metin üzerinde genellikle self-supervised learning yöntemiyle önceden eğitilir. Daha sonra belirli bir alan veya görev için daha küçük bir veri setiyle **fine-tuning** yapılabilir. Bu yöntem, sıfırdan büyük bir model eğitmek yerine önceden öğrenilmiş dil bilgisinden yararlanmayı sağlar.

### 6. Değerlendirme ve Çıktı Üretme

Eğitilen model validation ve test verileri üzerinde değerlendirilir. Kullanılan ölçüt göreve göre accuracy, precision, recall, F1-score veya farklı dil üretim metrikleri olabilir. Başarılı bulunan model gerçek bir uygulamaya eklenerek sınıf etiketi, çeviri, özet, arama sonucu, metin veya sesli cevap gibi çıktılar üretebilir.

## NLP Yaklaşımlarının Gelişimi

### Kural Tabanlı NLP

İlk NLP sistemlerinde dil bilgisi kuralları ve “eğer-böyleyse” yapıları insanlar tarafından yazılıyordu. Bu sistemler belirli ve dar görevlerde çalışabilse de dildeki bütün ihtimalleri kurallarla tanımlamak zordu. Yeni durumlara kolayca uyum sağlayamıyorlardı.

### İstatistiksel NLP

İstatistiksel yöntemlerde sistem, metinlerdeki kelime ve yapıların görülme olasılıklarını veriden öğrenmeye başladı. Regresyon, Naive Bayes ve Markov modelleri gibi yöntemler; metin sınıflandırma, yazım denetimi ve kelime tahmini gibi görevlerde kullanıldı.

### Derin Öğrenme Tabanlı NLP

Derin öğrenmeyle birlikte özelliklerin insanlar tarafından tek tek hazırlanması yerine sinir ağları dildeki örüntüleri veriden öğrenmeye başladı. RNN ve LSTM modelleri metin gibi sıralı verilerde uzun süre kullanıldı. Seq2Seq modelleri özellikle makine çevirisi ve metin üretimi görevlerinde önemli sonuçlar sağladı.

### Transformer ve Büyük Dil Modelleri

Transformer mimarisi, **attention** mekanizması sayesinde bir cümledeki kelimeler arasındaki ilişkileri daha etkili biçimde inceleyebilir. Transformer tabanlı BERT gibi modeller dili anlamaya yönelik görevlerde, GPT ailesi gibi autoregressive modeller ise bir sonraki tokenı tahmin ederek metin üretme görevlerinde kullanılır.

Büyük dil modelleri, çok büyük veri setlerinde eğitilmiş Transformer modelleridir. Aynı model özetleme, soru cevaplama, çeviri, sınıflandırma ve içerik üretme gibi birçok NLP görevini gerçekleştirebilir. Ancak büyük dil modeli ile NLP aynı şey değildir. NLP geniş bir bilim ve mühendislik alanıdır; LLM ise bu alanda kullanılan modern model türlerinden biridir.

## Temel NLP Görevleri

| Görev | Açıklama | Örnek |
| --- | --- | --- |
| Metin sınıflandırma | Metne önceden belirlenmiş bir etiket vermek | Spam veya normal e-posta |
| Duygu analizi | Metnin olumlu, olumsuz veya tarafsız olduğunu belirlemek | Müşteri yorumları |
| Named Entity Recognition | Kişi, kurum, konum ve tarih gibi varlıkları bulmak | “Ankara”yı konum olarak tanımak |
| Part-of-Speech Tagging | Kelimelerin dil bilgisel görevlerini belirlemek | İsim, fiil veya sıfat tespiti |
| Makine çevirisi | Bir dili başka bir dile çevirmek | Türkçeden İngilizceye çeviri |
| Metin özetleme | Uzun metnin ana düşüncelerini daha kısa vermek | Haber veya rapor özeti |
| Soru cevaplama | Soruya metne veya öğrenilen bilgilere göre cevap vermek | Belge üzerinden cevap üretmek |
| Semantik arama | Yalnızca aynı kelimeleri değil, benzer anlamları bulmak | Doküman arama sistemi |
| Metin üretme | Verilen isteğe göre yeni bir metin oluşturmak | E-posta veya açıklama yazmak |
| Konuşma tanıma | İnsan sesini yazılı metne dönüştürmek | Telefonun sesli yazma özelliği |

## Günlük Hayatta ve Sektörlerde NLP

NLP farkında olmasak da günlük hayatta sık kullandığımız sistemlerin içinde yer alır:

- Arama motorları
- Müşteri hizmetleri chatbotları
- Siri ve Alexa gibi sesli asistanlar
- E-posta spam filtreleri
- Otomatik düzeltme ve kelime tamamlama
- Çeviri uygulamaları
- Sosyal medya yorumlarının analizi
- Ürün ve içerik öneri sistemleri
- Belge arama ve özetleme sistemleri

Sağlık alanında hasta kayıtları ve bilimsel makaleler incelenebilir. Finans alanında şirket raporları, haberler ve piyasa yorumları analiz edilebilir. Hukukta çok sayıdaki belge içinde ilgili bilgiler bulunabilir. Sigorta alanında hasar belgeleri sınıflandırılabilir. Müşteri hizmetlerinde sık sorulan sorular otomatik olarak cevaplanabilir ve görüşmeler özetlenebilir.

NLP bu alanlarda tekrarlı işleri otomatikleştirir, büyük metin koleksiyonlarının daha hızlı incelenmesini sağlar ve yapılandırılmamış verilerden bilgi çıkarılmasına yardımcı olur.

## NLP ile Günümüz Yapay Zekâlarının Ortak Yönleri

NLP, günümüz yapay zekâlarından tamamen ayrı bir teknoloji değildir; yapay zekânın alt alanlarından biridir. Bu nedenle günümüzdeki makine öğrenmesi sistemleriyle birçok ortak temele sahiptir.

- İkisi de verilerden örüntü öğrenebilir.
- Makine öğrenmesi ve derin öğrenme algoritmalarından yararlanabilir.
- Sinir ağları, layer, weight, bias ve activation function gibi yapılara sahip olabilir.
- Eğitim sırasında forward pass, loss calculation, backpropagation ve optimizer kullanabilir.
- Eğitim, validation ve test veri setleriyle değerlendirilir.
- Modelin yeni verilere genelleme yapması beklenir.
- Transformer mimarisi ve attention mekanizması kullanılabilir.
- Veri kalitesi, bias, overfitting ve hesaplama maliyeti gibi ortak sorunlara sahiptir.

NLP modellerinde kullanılan eğitim mantığı, görüntü işleyen bir yapay sinir ağındaki temel eğitim mantığıyla benzerdir. Temel fark, kullanılan verinin ve çözülmek istenen problemin türüdür.

## NLP ile Günümüz Yapay Zekâlarının Farklı Yönleri

NLP’nin uzmanlaştığı veri türü **insan dilidir**. Yapay zekâ ise dilin yanında görüntü, video, ses, sensör verisi, kullanıcı davranışları ve robot hareketleri gibi çok daha geniş bir alanı kapsar.

| Alan | Temel veri veya amaç |
| --- | --- |
| NLP | Metin ve konuşmayı anlamak veya üretmek |
| Computer Vision | Görüntü ve videoları işlemek |
| Öneri sistemleri | Kullanıcı davranışından tercih tahmin etmek |
| Zaman serisi modelleri | Geçmiş ölçümlerden geleceği tahmin etmek |
| Robotik | Sensör verileriyle çevreyi algılamak ve hareket etmek |
| Üretken yapay zekâ | Metin, görüntü, ses, video veya kod gibi yeni içerikler üretmek |

Her NLP sistemi üretken yapay zekâ değildir. Örneğin spam tespiti veya duygu analizi yalnızca bir sınıflandırma sonucu üretir. Benzer şekilde her üretken yapay zekâ da NLP değildir; görüntü üreten bir model üretken yapay zekâdır fakat temel çıktısı dil olmadığı için klasik anlamda bir NLP sistemi sayılmaz.

ChatGPT gibi bir sistemin temelinde büyük bir dil modeli ve NLP yöntemleri bulunur. Ancak günümüzde bazı yapay zekâ sistemleri metnin yanında görüntü, ses ve video da işleyebilir. Bu sistemlere **multimodal yapay zekâ** denir. Multimodal bir modelde NLP, dil bölümünün anlaşılması ve üretilmesinde görev alırken diğer yöntemler görüntü veya ses gibi farklı veri türlerini işler.

## NLP’nin Zorlukları

İnsan dili kurallı görünmesine rağmen bağlama göre sürekli değişebilir. Aynı kelime farklı anlamlarda kullanılabilir; ironi, deyim, argo ve kültürel ifadeler sistemler için zor olabilir.

NLP’de karşılaşılan temel sorunlar şunlardır:

- Birden fazla anlama gelen kelimeler ve belirsiz cümleler
- İroni, mizah ve mecazların anlaşılması
- Aksan, lehçe, argo ve yeni kelimeler
- Yazım hataları ve eksik cümleler
- Ses kayıtlarındaki arka plan gürültüsü
- Eğitim verilerindeki toplumsal önyargıların modele yansıması
- Büyük modellerin yüksek işlem gücü ve enerji gerektirmesi
- Model kararlarının her zaman kolay açıklanamaması
- Özel belgeler kullanıldığında veri güvenliği ve gizlilik sorunları
- Büyük dil modellerinin doğru görünmesine rağmen yanlış bilgi üretebilmesi

Bu nedenle NLP modelinin yalnızca eğitim verisindeki başarısına bakmak yeterli değildir. Model farklı kullanıcılar, dil biçimleri ve gerçek hayat örnekleri üzerinde de test edilmeli; özellikle sağlık, hukuk ve finans gibi önemli alanlarda insan kontrolü korunmalıdır.

## Sonuç

NLP, bilgisayarların yazılı ve sözlü insan dilini işlemesini, anlamla ilgili çıkarımlar yapmasını ve yeni dil üretmesini sağlayan yapay zekâ alanıdır. Metin sınıflandırma, duygu analizi, çeviri, özetleme, soru cevaplama, konuşma tanıma ve semantik arama gibi birçok görevi kapsar.

NLP geçmişte kural tabanlı ve istatistiksel yöntemlerle uygulanırken günümüzde derin öğrenme, Transformer ve büyük dil modelleriyle daha gelişmiş hâle gelmiştir. Günümüz yapay zekâlarıyla aynı makine öğrenmesi temellerini kullanır; ancak özellikle insan dili üzerinde çalışmasıyla diğer alanlardan ayrılır. Büyük dil modelleri NLP’nin tamamı değil, NLP alanında kullanılan modern ve güçlü model türleridir. Kısaca NLP, insanlar ile bilgisayarlar arasındaki iletişim farkını azaltarak makinelerin dil üzerinden daha yararlı görevler gerçekleştirmesini sağlar.
