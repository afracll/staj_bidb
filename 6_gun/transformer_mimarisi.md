# Transformer Temelleri

## Giriş

Transformer, özellikle metin işleme alanında kullanılan bir sinir ağı mimarisidir. İlk olarak 2017 yılında yayımlanan **Attention Is All You Need** çalışmasında tanıtılmıştır. Daha önce kullanılan bazı modeller metni kelime kelime işlerken Transformer, cümledeki tokenlar arasındaki ilişkilere attention mekanizmasıyla bakar.

## Positional Encoding

Transformer cümledeki tokenları aynı anda işleyebildiği için tokenların sırasını kendiliğinden anlayamaz. Fakat bir cümlede kelimelerin hangi sırada olduğu önemlidir.

- **Ali Ayşe’yi aradı.**
- **Ayşe Ali’yi aradı.**

Bu iki cümlede benzer kelimeler kullanılmasına rağmen kelime sırası değiştiği için anlam da değişmektedir. Modelin bu farkı anlayabilmesi için tokenların cümlede kaçıncı sırada bulunduğunu bilmesi gerekir. Bu bilgiyi modele veren yapıya **positional encoding**, yani konumsal kodlama denir.

Tokenlar modele verilmeden önce sayısal vektörlerle temsil edilir. Positional encoding ile oluşturulan konum bilgisi de bu vektöre eklenir. Böylece model bir tokenın hem neyi temsil ettiğini hem de cümlede nerede bulunduğunu birlikte değerlendirebilir.

İlk Transformer çalışmasında konum bilgisi sinüs ve kosinüs fonksiyonlarıyla oluşturulmuştur. Her pozisyon için farklı sayısal değerler elde edilir. Formülün temel amacı, birinci token ile beşinci tokenın aynı konum bilgisine sahip olmasını engellemektir.

Kısaca positional encoding olmasaydı model, aynı tokenların farklı sıralarda kullanıldığı cümleleri ayırt etmekte zorlanırdı.

## Attention

Attention, modelin bir tokenı işlerken diğer tokenların ne kadar önemli olduğuna karar vermesini sağlar. Yani model cümledeki her kelimeye aynı miktarda dikkat etmek zorunda değildir.

> Ece kitabı masaya bıraktı çünkü ona artık ihtiyacı yoktu.

Model “ona” kelimesinin neyi ifade ettiğini anlamaya çalışırken “kitabı” kelimesine daha fazla dikkat verebilir. Cümledeki başka kelimeler ise bu işlem için daha az önemli olabilir. Attention mekanizması bu önem derecelerini sayısal skorlarla hesaplar.

Bu sayede bir tokenın anlamı yalnızca kendi başına değil, cümlenin geri kalanıyla olan ilişkisine göre değerlendirilir. Transformer’ın bağlamı anlayabilmesinin önemli nedenlerinden biri budur.

## Query, Key ve Value

Attention işlemi sırasında her token için Query, Key ve Value adı verilen üç farklı vektör oluşturulur. Bunlar kısaca Q, K ve V harfleriyle gösterilir.

- **Query (Sorgu):** Tokenın hangi bilgiyi aradığını temsil eder.
- **Key (Anahtar):** Tokenın hangi tür bilgi taşıdığını gösterir.
- **Value (Değer):** Tokenın başka bir tokene aktaracağı asıl bilgidir.

Bunu bir arama işlemi gibi düşünebiliriz. Query aradığımız şeyi, Key elimizdeki bilgilerin etiketlerini, Value ise etiketin arkasında bulunan gerçek bilgiyi temsil eder.

Bir tokenın Query vektörü, cümledeki diğer tokenların Key vektörleriyle karşılaştırılır. Bir Query ile Key birbirine uygunsa aralarındaki attention skoru yüksek çıkar. Daha sonra bu skorlar, hangi Value vektörlerinden ne kadar bilgi alınacağını belirler.

Attention işleminin genel formülü şöyledir:

```text
Attention(Q, K, V) = softmax(QKᵀ / √dₖ) V
```

Burada önce Query ve Key karşılaştırılır. Elde edilen değerler çok büyümesin diye belirli bir sayıya bölünür. Ardından softmax fonksiyonuyla skorlar 0 ile 1 arasında değerlere çevrilir. Son olarak bu değerler Value vektörleriyle birleştirilir.

Query ve Key “hangi tokenlar birbiriyle ilgili?” sorusuna cevap verirken Value, ilgili tokendan alınacak bilgiyi taşır.

## Multi-Head Attention

Bir cümlede tokenlar arasında tek bir ilişki bulunmaz. Kelimeler arasında anlam ilişkisi, özne-yüklem ilişkisi veya bir zamirin hangi kelimeyi gösterdiği gibi farklı bağlantılar olabilir. Tek bir attention işlemi bütün bu bağlantıları aynı şekilde yakalayamayabilir.

Bu nedenle Transformer’da birden fazla attention işlemi paralel olarak çalıştırılır. Buna **multi-head attention** denir. Her bir attention bölümüne **head** adı verilir.

Örneğin bir head özne ile yüklem arasındaki ilişkiye daha fazla dikkat ederken başka bir head, cümlede uzakta bulunan iki token arasındaki bağlantıya odaklanabilir. Her head kendi Query, Key ve Value hesaplamasını yapar. Daha sonra headlerden gelen sonuçlar birleştirilir.

Buradaki amaç aynı cümleyi birkaç farklı açıdan değerlendirmektir. Bu nedenle multi-head attention, modelin metindeki ilişkileri daha ayrıntılı biçimde öğrenmesine yardımcı olur.

## Transformer Block

Transformer modeli yalnızca attention işleminden oluşmaz. Attention, normalization ve feed-forward işlemlerinin bir araya gelmesiyle bir **Transformer block** meydana gelir. Modelin içinde bu bloklardan birden fazla bulunabilir. Bir bloktan çıkan sonuç sonraki bloğa aktarılır ve bilgi her blokta biraz daha işlenir.

Temel akış şu şekilde düşünülebilir:

```text
Girdi - Multi-Head Attention - Layer Normalization - Feed-Forward Network - Layer Normalization - Çıktı
```

Multi-head attention kısmında tokenlar birbirleriyle olan ilişkilerine göre bilgi alışverişi yapar. Layer normalization değerleri dengeler. Feed-forward bölümü ise ortaya çıkan yeni token temsillerini işler. Bu işlemlerin birlikte çalışması Transformer block’un temelini oluşturur.

## Layer Normalization

Modeldeki sayısal değerler katmanlardan geçerken çok büyüyebilir veya birbirinden oldukça farklı hâle gelebilir. Bu durum eğitimi zorlaştırabilir. **Layer normalization**, değerleri daha dengeli bir ölçeğe getirerek modelin daha kararlı biçimde öğrenmesine yardımcı olur.

Layer normalization, her tokenın vektörü üzerinde ortalama ve dağılım hesaplamaları yapar. Daha sonra bu değerleri düzenler. Modelin öğrenebildiği ölçek ve kaydırma değerleri de sonuca uygulanır.

Burada amaç bütün tokenları birbirinin aynısı yapmak değildir. Tokenların taşıdığı bilgi korunurken sayısal değerlerin kontrol altında tutulması amaçlanır. Bu nedenle layer normalization, derin Transformer modellerinin eğitiminde önemli bir yere sahiptir.

## Feed-Forward Network

Attention bölümünde tokenlar birbirlerinden bilgi alır. Ancak alınan bilginin ayrıca işlenmesi gerekir. Bu işlem Transformer block içindeki **feed-forward network** tarafından yapılır.

Feed-forward network genellikle iki doğrusal katmandan oluşur. Bu iki katmanın arasında ReLU veya GELU gibi bir aktivasyon fonksiyonu bulunabilir. İlk katman tokenın vektörünü daha geniş bir boyuta çıkarır. İkinci katman ise tekrar modelin kullandığı boyuta getirir.

Feed-forward işlemi her tokene ayrı ayrı uygulanır. Yani attention kısmında tokenlar birbiriyle ilişki kurarken feed-forward kısmında her tokenın elde ettiği yeni bilgi kendi içinde işlenir.

- Attention, diğer tokenlardan hangi bilgilerin alınacağını belirler.
- Feed-forward network, alınan bilgiyi işler.

## Token Prediction

GPT gibi metin üreten modellerin temel görevi, verilen tokenlara bakarak sıradaki tokenı tahmin etmektir. Buna **token prediction** denir.

Örneğin modelin girdisi şu olsun:

> Bugün hava çok ...

Model, sözlüğünde bulunan bütün tokenlar için bir skor oluşturur. “Güzel”, “soğuk” ve “sıcak” gibi tokenlar bu cümleye daha uygun oldukları için yüksek skor alabilir. “Kitap” gibi bağlamla ilgisiz bir tokenın skoru ise daha düşük olabilir.

Modelin ürettiği bu ham değerlere **logit** denir. Logitler softmax fonksiyonuyla olasılıklara dönüştürülür. Örneğin sonuç şöyle olabilir:

```text
güzel   → %50
soğuk   → %30
sıcak   → %15
diğer   → %5
```

Bu olasılıklara göre bir token seçilir ve mevcut cümlenin sonuna eklenir. Model daha sonra oluşan yeni cümleyi kullanarak bir sonraki tokenı tahmin eder. Metin oluşturma işlemi bu şekilde tekrar ederek ilerler.

GPT türü modeller sıradaki tokenı tahmin ederken gelecekteki tokenları göremez. Yalnızca kendisinden önce gelen tokenları kullanır. Attention sırasında uygulanan maskeleme, gelecekteki tokenlara bakılmasını engeller.

Eğitim sırasında modelin tahmin ettiği token ile gerçekte gelmesi gereken token karşılaştırılır. Aradaki hata hesaplanır ve modelin ağırlıkları güncellenir. Bu işlem çok fazla metin üzerinde tekrarlandıkça model, belirli bir bağlamdan sonra hangi tokenların gelebileceğini öğrenir.

## Konuların Birbiriyle Bağlantısı

Bu konuların tamamı aslında aynı işlem sırasının parçalarıdır. Önce positional encoding ile tokenların konum bilgisi eklenir. Daha sonra Query, Key ve Value vektörleri oluşturularak attention skorları hesaplanır. Multi-head attention sayesinde bu işlem farklı ilişkiler için birkaç kez gerçekleştirilir.

Attention sonucunda oluşan bilgi Transformer block içinde layer normalization ve feed-forward network tarafından işlenir. Bloklardan geçen son temsil, token prediction aşamasında kullanılır. Model bütün olası tokenlar için bir olasılık oluşturur ve sıradaki tokenı seçer.

## Sonuç

Bu araştırmadan anladığım kadarıyla Transformer’ın en önemli bölümü attention mekanizmasıdır. Positional encoding tokenların sırasını modele bildirirken Query, Key ve Value tokenlar arasındaki ilişkinin hesaplanmasını sağlar. Multi-head attention ise aynı cümledeki farklı bağlantıları aynı anda incelemeye yardımcı olur.

Transformer block içinde bu bilgiler layer normalization ve feed-forward network ile işlenir. Son aşamada model, elde ettiği bağlama göre sıradaki tokenı tahmin eder. ChatGPT gibi metin üreten modellerin cümle oluşturması da temel olarak bu tahmin işleminin tekrar edilmesiyle gerçekleşir.