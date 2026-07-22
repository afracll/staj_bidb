-- kütüphane vt

CREATE DATABASE KutuphaneDB;
GO
USE KutuphaneDB;
GO

CREATE TABLE Uyeler (
    id INT PRIMARY KEY,
    ad VARCHAR(50) NOT NULL,
    sehir VARCHAR(50),
    uyelik_yili INT
);

CREATE TABLE Kitaplar (
    id INT PRIMARY KEY,
    baslik VARCHAR(100) NOT NULL,
    tur VARCHAR(30),
    sayfa_sayisi INT,
    yayin_yili INT
);

CREATE TABLE OduncIslemleri (
    id INT PRIMARY KEY,
    uye_id INT,
    kitap_id INT,
    odunc_tarihi DATE,
    iade_edildi_mi INT DEFAULT 0
);

-- veriler
INSERT INTO Uyeler VALUES (1, 'Ahmet', 'İzmir', 2021);
INSERT INTO Uyeler VALUES (2, 'Zeynep', 'Ankara', 2020);
INSERT INTO Uyeler VALUES (3, 'Mert', 'İzmir', 2022);

INSERT INTO Kitaplar VALUES (1, 'Kürk Mantolu Madonna', 'Roman', 160, 1943);
INSERT INTO Kitaplar VALUES (2, 'Fareler ve İnsanlar', 'Roman', 120, 1937);
INSERT INTO Kitaplar VALUES (3, 'Sapiens', 'Tarih', 400, 2011);
INSERT INTO Kitaplar VALUES (4, 'Kozmos', 'Bilim', 380, 1980);

INSERT INTO OduncIslemleri VALUES (1, 1, 1, '2024-01-10', 1);
INSERT INTO OduncIslemleri VALUES (2, 1, 3, '2024-02-05', 0);
INSERT INTO OduncIslemleri VALUES (3, 2, 2, '2024-01-20', 1);
INSERT INTO OduncIslemleri VALUES (4, 3, 4, '2024-03-01', 0);
GO

--tüm şehirleri tekrarsız listele
SELECT DISTINCT sehir FROM Uyeler;

--300 sayfadan uzun kitapları listele
SELECT baslik, sayfa_sayisi FROM Kitaplar WHERE sayfa_sayisi > 300;

--hangi üye hangi kitabı almış
SELECT u.ad, k.baslik
FROM OduncIslemleri o
JOIN Uyeler u ON o.uye_id = u.id
JOIN Kitaplar k ON o.kitap_id = k.id;

--henüz iade edilmemiş kitaplar kimde
SELECT u.ad, k.baslik
FROM OduncIslemleri o
JOIN Uyeler u ON o.uye_id = u.id
JOIN Kitaplar k ON o.kitap_id = k.id
WHERE o.iade_edildi_mi = 0;

-- türe göre kitap sayısı ve ortalama sayfa sayısı
SELECT tur, COUNT(*) AS kitap_sayisi, AVG(sayfa_sayisi) AS ortalama_sayfa
FROM Kitaplar
GROUP BY tur;

-- şehir başına üye sayısı
SELECT sehir, COUNT(*) AS uye_sayisi
FROM Uyeler
GROUP BY sehir;

-- en eski ve en yeni yayınlanan kitap
SELECT MIN(yayin_yili) AS en_eski, MAX(yayin_yili) AS en_yeni
FROM Kitaplar;

-- bir üyenin şehrini güncelle
UPDATE Uyeler SET sehir = 'İstanbul' WHERE id = 2;

-- iade edilen bir işlemi sil
DELETE FROM OduncIslemleri WHERE id = 3;

-- en çok kitap ödünç alan üyeyi bul
SELECT TOP 1 u.ad, COUNT(*) AS odunc_sayisi
FROM OduncIslemleri o
JOIN Uyeler u ON o.uye_id = u.id
GROUP BY u.ad
ORDER BY odunc_sayisi DESC;
