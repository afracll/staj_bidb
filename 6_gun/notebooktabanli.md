# notebook tabanlı programlama

Notebook tabanlı programlamada kodu tek bir dosyada baştan sona yazıp çalıştırmak yerine kodu küçük parçalara (hücre) bölerek her birini ayrı ayrı çalıştırıp sonuçları anında görebiliriz. özellikle veri odaklı ve görselleştirmenin önemli olduğu işler için kodu adım adım yazıp anında sonuç görmeyi sağlayan bir çalışma biçimi.

## hücre yapısı ve önemi
notebook: art arda sıralanamış hücrelerden oluşuyor:
- kod hucreleri: python gibi bir dilde kod içerir.
- md/metin hücreleri: açıklama baslık formül ve not eklemek için.
- her hücre bağımsız olarak çalıştırılabilir.
- bir hücrenin çıktısı hemen o hücrenin altında görünür. grafik, tablo, sayı hata mesajı vb...
- değişkenler bellekte tutulur, bi hücrede tanımladıgımız değişkeni sonraki hücrelerde kullanabiliriz.
- kod çıktı grafikler açıklayıcı metin ve matematiksel formüller aynı belgede bulunabilir.
- anlık geribildirimler sayesinde kodu en baştan yazıp çalıştırmak gerekmez
- veri biliminin standart aracı haline geldi en yaygın çalışma biçimi bu. yapay zeka çalışmalarının büyük kısmı notebooklarda yapılıyor.

## yaygın kullanılan araçlar
- Jupyter Notebook / JupyterLab: en popüler Python ve birçok dille çalışır
- Google Colab: bulut tabanlı, ücretsiz GPU erişimi sunar
- Kaggle Notebooks: veri bilimi yarışmaları için
- VS Code Notebooks: VS Code içinde .ipynb dosyalarını destekler

## ne için kullanılır?
- Veri analizi ve veri bilimi: veriyi keşfetmek, temizlemek, görselleştirmek
- Makine öğrenmesi: model eğitimi, deney sonuçlarını hızlıca gözlemlemek
- Eğitim: kod ile açıklamayı yan yana sunmak
- Prototipleme: fikirleri hızlıca test etmek

## avantajları
- Anında geri bildirim (satır satır test etme)
- Görselleştirmeleri kodla birlikte görme
- Adım adım belgeleme ve paylaşım kolaylığı

## dezavantajları
- Büyük seviyede yazılımlar için uygun değildir
- Hücrelerin sırasız çalıştırılması hatalara yol açabilir
- Versiyon kontrolü (Git ile) geleneksel .py dosyalarına göre daha zordur
