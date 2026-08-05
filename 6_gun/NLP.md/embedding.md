# Embedding Nedir?

## Embedding Tanımı

Bilgisayarlar kelime, görüntü veya ses gibi verileri insanlar gibi doğrudan anlamlandıramaz. Bu veriler üzerinde işlem yapabilmeleri için verilerin sayısal biçimde temsil edilmesi gerekir. **Embedding (gömme)**, bir veri parçasını onun önemli özelliklerini ve diğer verilerle ilişkilerini yansıtan sayısal bir vektöre dönüştürme yöntemidir.

Örneğin bir kelime embeddingi şu şekilde görünebilir:

```text
elma → [0.21, -0.46, 0.73, 0.18, ...]
```

Gerçek embeddingler yüzlerce sayıdan oluşabilir. Bu sayıların her biri tek başına açık bir anlam taşımaz; önemli olan vektörün tamamının oluşturduğu sayısal temsildir.

## Embedding Uzayı

Embedding vektörlerinin bulunduğu matematiksel alana **embedding space**, yani embedding uzayı denir. Model eğitilirken benzer anlamlara veya özelliklere sahip verilerin bu uzayda birbirine yakın konumlanması amaçlanır.

Örneğin:

- “Elma” ve “armut” ikisi de meyve olduğu için birbirine yakın olabilir.
- “Kral” ve “kraliçe” arasında belirli bir ilişki bulunabilir.
- “Elma” ve “masa” ise daha uzak konumlarda yer alabilir.

Bu yakınlık, modelin eğitim verilerinde öğrendiği kullanım örüntülerinden oluşur. Model insan gibi anlamaz; verilerde hangi kelimelerin benzer bağlamlarda kullanıldığını öğrenerek matematiksel bir temsil oluşturur.

## Token ID ile Embedding Arasındaki Fark

Bir NLP sisteminde metin önce tokenlara ayrılır. Her tokenın model sözlüğünde bir **token ID** değeri bulunur. Ancak token ID yalnızca sıra numarasıdır ve kelimeler arasındaki anlam ilişkisini göstermez.

Model token ID’yi kullanarak embedding tablosundaki ilgili vektöre ulaşır:

```text
Token → Token ID → Embedding vektörü → Sinir ağı
```

Kısaca:

- **Token:** Metnin tokenizer tarafından oluşturulan parçasıdır.
- **Token ID:** Tokenın model sözlüğündeki sayısal kimliğidir.
- **Embedding:** Tokenın model tarafından işlenebilen, öğrenilmiş vektör temsilidir.

Embedding tablosu sinir ağının öğrenilebilir parametrelerinden biri olabilir. Eğitim sırasında loss değeri hesaplanır ve embedding vektörleri de diğer ağırlıklar gibi backpropagation ve optimizer yardımıyla güncellenir.

## Embedding Neden Kullanılır?

Embeddinglerin temel amacı yalnızca veriyi sayıya çevirmek değildir. Aynı zamanda veriler arasındaki ilişkilerin model tarafından kullanılabilmesini sağlar.

Embeddingler:

- Kelime, cümle, görüntü ve ses gibi verileri sayısal hâle getirir.
- Benzer verilerin matematiksel olarak karşılaştırılmasını sağlar.
- Çok büyük ve çoğu sıfır olan one-hot vektörler yerine daha yoğun temsiller oluşturabilir.
- Modellerin sınıflandırma, tahmin, arama ve öneri gibi görevleri gerçekleştirmesine yardımcı olur.

## Embedding Nasıl Oluşturulur?

Embeddingler çoğunlukla büyük veri setleri üzerinde eğitim yapan makine öğrenmesi veya sinir ağı modelleri tarafından öğrenilir. Başlangıçta rastgele oluşturulan vektörler, modelin yaptığı hatayı azaltmak amacıyla eğitim boyunca güncellenir.

Örneğin bir kelime embedding modeli, bir kelimenin çevresinde hangi kelimelerin bulunduğunu tahmin etmeye çalışabilir. Benzer bağlamlarda kullanılan kelimelerin vektörleri zamanla birbirine yaklaşabilir. Word2Vec ve GloVe klasik kelime embedding yöntemlerine örnektir. FastText ise kelimeleri karakter parçalarıyla da temsil ederek ek alan veya daha önce görülmemiş kelimelerde avantaj sağlayabilir.

## Statik ve Bağlamsal Embeddingler

### Statik Embedding

Word2Vec ve GloVe gibi klasik yöntemlerde bir kelimenin genellikle tek bir embedding vektörü vardır. Kelime farklı cümlelerde kullanılsa da vektörü değişmez. Bu durum birden fazla anlamı bulunan kelimelerde sorun oluşturabilir.

Örneğin “banka” kelimesi hem para işlemlerinin yapıldığı kurumu hem de bazı kullanımlarda oturulan bir nesneyi ifade edebilir. Statik embedding bu farklı anlamları tek vektörde birleştirebilir.

### Bağlamsal Embedding

BERT ve diğer Transformer tabanlı modeller, bir tokenın embeddingini çevresindeki kelimelere göre oluşturabilir. Böylece aynı kelime farklı cümlelerde farklı vektörlerle temsil edilebilir. Buna **contextual embedding**, yani bağlamsal embedding denir.

Bağlamsal embeddingler kelimenin cümlede hangi anlamda kullanıldığını daha iyi yansıtabilir. Günümüzdeki büyük dil modellerinde tokenların temsili, modelin katmanları boyunca bağlama göre değişir.

## Embedding Benzerliği

İki embedding arasındaki benzerliği ölçmek için sıklıkla **cosine similarity (kosinüs benzerliği)** kullanılır. Bu yöntem vektörlerin yönlerinin ne kadar benzer olduğunu ölçer. Sonuç birbirine yakınsa verilerin model açısından benzer özellikler taşıdığı düşünülebilir.

Ancak embedding yakınlığı mutlak bir gerçek değildir. Sonuç, embedding modelinin hangi veriyle ve hangi amaçla eğitildiğine bağlıdır. Farklı modeller aynı kelime veya belge için farklı vektörler oluşturabilir. Bu nedenle karşılaştırılacak veriler genellikle aynı embedding modeliyle vektöre dönüştürülmelidir.

## Embeddinglerin Kullanım Alanları

### NLP ve Büyük Dil Modelleri

Tokenlar embedding vektörlerine dönüştürülerek sinir ağına verilir. Bu temsiller çeviri, duygu analizi, metin sınıflandırma, özetleme ve soru cevaplama gibi görevlerde kullanılır.

### Semantik Arama ve RAG

Semantik aramada kullanıcı sorusu ve belgeler embeddinge çevrilir. Soru vektörüne en yakın belge vektörleri bulunarak aynı kelimeleri içermese bile anlam bakımından ilgili sonuçlara ulaşılabilir.

RAG sistemlerinde belgeler küçük parçalara ayrılır ve embeddingleri bir vektör veritabanında saklanır. Kullanıcı soru sorduğunda sorunun embeddingine benzeyen belge parçaları bulunur ve cevap üretmesi için büyük dil modeline gönderilir.

### Öneri Sistemleri

Kullanıcılar, filmler, şarkılar veya ürünler embeddinglerle temsil edilebilir. Birbirine yakın kullanıcı ve içerik vektörleri kullanılarak kişiselleştirilmiş öneriler üretilebilir.

### Görüntü ve Ses İşleme

Embedding yalnızca metinde kullanılmaz. Görseller vektörlere dönüştürülerek benzer resimler veya yüzler bulunabilir. Ses embeddingleri ise konuşmacı tanıma ve ses benzerliği gibi görevlerde kullanılabilir.

## Avantajları ve Sınırlamaları

Embeddingler karmaşık verileri daha yoğun sayısal temsillere dönüştürür, benzerlik hesaplamayı mümkün kılar ve farklı yapay zekâ projelerinde tekrar kullanılabilir. Ancak oluşturulan ilişkiler eğitim verisine bağlıdır. Verideki hatalar veya toplumsal önyargılar embeddinglere yansıyabilir. Ayrıca vektörlerdeki her boyutun insanlar için açıklanması genellikle zordur.

Embedding boyutunun büyük olması da her zaman daha iyi sonuç anlamına gelmez. Daha büyük vektörler daha fazla bellek ve hesaplama gerektirir. Uygun embedding modeli ve boyutu kullanılacak projeye göre seçilmelidir.

## Sonuç

Embedding; kelime, cümle, belge, görüntü veya ses gibi karmaşık verileri sayısal vektörlerle temsil eden bir yöntemdir. Benzer veriler embedding uzayında birbirine yakın konumlanabildiği için modeller benzerlik ve ilişki hesaplayabilir. Embeddingler NLP, büyük dil modelleri, semantik arama, RAG, öneri sistemleri, görüntü ve ses işleme gibi birçok alanda kullanılır. Kısaca embedding, gerçek dünyadaki veriler ile yapay zekâ modellerinin matematiksel işlemleri arasında bir köprü görevi görür.
