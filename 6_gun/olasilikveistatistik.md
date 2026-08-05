# Olasılık ve İstatistik Konularının Yapay Zeka ile Bağlantısı

İstatistik, veriden sistemi anlamaya, olasılık ise oluşturulan sistemden gelecekteki sonuçları tahmin etmeye yarar. Yapay zeka da bu iki yaklaşımı bilgisayar bilimi, matematik ve optimizasyonla birleştirir.

Verinin olduğu ve veriden bir sonuç çıkarılmaya çalışıldığı her yerde istatistik ve olasılıktan söz edilebilir. Olasılık ve istatistik birbiriyle bağlantılı iki alan olsa da bir problemi ele alış yönleri farklıdır.

Olasılıkta genellikle sistemi veya sistemi temsil eden matematiksel modeli bildiğimiz kabul edilir. Sistemin hangi kurallarla çalıştığını bildikten sonra ortaya çıkabilecek sonuçları tahmin etmeye çalışırız. yazı tura ihtimali gibi bilinen sistemden muhtemel sonuçlara doğru ilerleriz.

İstatistikte ise problem ters yönden ele alınır. Sistemin tamamını bilmeden, onun ürettiği çıktılara yani gözlem ve verilere bakarız. Bu verilerden yararlanarak sistemin içindeki düzeni ve sistemi açıklayabilecek modeli ortaya çıkarmaya çalışırız. gözlemlenen çıktılardan bilinmeyen sistem hakkında bilgi edinmemizi sağlayan bir bilim dalıdır.

İstatistik kullanılarak bir sistem modeli elde edildikten sonra bu modelin gelecekte üretebileceği sonuçlar olasılık yardımıyla tahmin edilebilir. Dolayısıyla istatistik ve olasılık çoğu zaman arka arkaya kullanılır. İstatistikle geçmiş verilerden bir model kurar, olasılıkla bu modelin gelecekteki sonuçlarını değerlendiririz. Yaklaşımları farklı olsa da yapay zekâ ve makine öğrenmesinde birbirlerini tamamlarlar.

yapay zekada belirsizlik türleri vardır. Modelin eksik bilgiye veya yetersiz veriye sahip olmasından kaynaklanan belirsizliğe epistemik belirsizlik denir. Daha fazla ve daha kaliteli veri toplandıkça bu belirsizlik azaltılabilir. Sistemin doğal değişkenliğinden ve ölçüm gürültüsünden kaynaklanan belirsizlik ise aleatorik belirsizliktir. Bu belirsizlik daha fazla veri toplansa bile tamamen ortadan kaldırılamayabilir

# Doğal ve insan yapımı sistemler

Veri bilimi ve makine öğrenmesi, bilgisayar bilimi, matematik ve istatistikten beslenir. Bilgisayar, yazılım ve algoritmalar insanlar tarafından belirli matematiksel kurallar kullanılarak oluşturulan sistemlerdir. Bu nedenle bir bilgisayar programının komutları ve işlem adımları ayrıntılı biçimde tanımlanabilir. Aynı girdiler ve aynı koşullar verildiğinde deterministik bir programın aynı çıktıyı üretmesi beklenir.

Doğal sistemler ise daha farklıdır. Bütün değişkenleri bilmemiz ve kontrol etmemiz mümkün değildir. Doğayla ilgili kesin ve eksiksiz bilgiye sahip olmadığımız için gözlem yapıp veri toplarız ve anlayabildiğimiz kadarıyla modeller oluştururuz. Kurduğumuz bu modeller gerçek sistemin kendisi değil, sistemin belirli özelliklerini açıklayan yaklaşık temsillerdir. Bu nedenle doğal sistemlerle ilgili modeller çoğunlukla bir belirsizlik üzerine inşa edilir.

# Yapay zeka modeli nasıl öğrenir?

Yapay zekâ modelinin öğrenme süreci, gözlemlenen verilerden sistemdeki örüntüleri ve ilişkileri bulmaya dayanır. Bir e-posta sınıflandırma modelinde geçmişte spam ve spam değil olarak etiketlenmiş e-postalar incelenir. Model, kelimelerle sonuçlar arasındaki istatistiksel ilişkileri öğrenir. Daha sonra yeni bir e-posta geldiğinde bu e-postanın spam olma olasılığını tahmin eder. bir olasılık üretir. Böylece model önce istatistiksel olarak geçmiş verilerden öğrenir, ardından öğrendiği yapı üzerinden olasılıksal tahmin yapar.

Modelin eğitiminde kullanılan hata ölçüleri de olasılık ve istatistikle bağlantılıdır. Regresyon modellerinde kullanılan ortalama karesel hata, belirli varsayımlar altında normal dağılımla ilişkilidir. Sınıflandırma ve dil modellerinde kullanılan cross-entropy ise modelin doğru sonuca ne kadar olasılık verdiğini ölçer. Model doğru sonuca yüksek olasılık verdikçe hata azalır; yanlış sonuca yüksek olasılık verdikçe hata artar.

büyük dil modellerinde de benzer bir yapı bulunur. Dil modeli, kendisinden önce gelen kelime veya token’lara bakarak sıradaki token’ın olasılıklarını tahmin eder. Örneğin “Bugün hava çok...” ifadesinden sonra “güzel”, “sıcak” veya “soğuk” kelimelerinin her birine farklı olasılıklar verebilir. Bu nedenle dil üretimi de temelinde olasılıksal bir tahmin sürecidir.

# Veriler geldikçe modelin iyileştirilmesi

Doğal veya toplumsal bir sistemi modelleyebildiğimiz ve anlayabildiğimiz ölçüde yapay bir sistem oluştururuz. Fakat kurduğumuz model son ve değişmez bir yapı değildir. Zaman içinde yeni veriler geldikçe modelin öğrendiği ilişkiler yeniden değerlendirilir ve gerekirse model güncellenir.

İstatistiksel dağılımlar; verilerin hangi değerler etrafında toplandığını, ne kadar değiştiğini ve zaman içinde nasıl farklılaştığını anlamamıza yardımcı olur. Bu bilgiler modele girdi hazırlama, aykırı değerleri bulma, eksik verileri değerlendirme ve modelin hâlâ doğru veri üzerinde çalışıp çalışmadığını kontrol etme aşamalarında kullanılır. Böylece model, istatistikten ve yeni verilerden sürekli beslenen bir yapıya dönüşür.