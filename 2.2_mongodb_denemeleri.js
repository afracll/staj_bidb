// temizledim
db.uyeler.drop();
db.kitaplar.drop();
db.odunc_islemleri.drop();

//veri ekle
db.uyeler.insertMany([
  { _id: 1, ad: 'Ahmet', sehir: 'İzmir', uyelik_yili: 2021 },
  { _id: 2, ad: 'Zeynep', sehir: 'Ankara', uyelik_yili: 2020 },
  { _id: 3, ad: 'Mert', sehir: 'İzmir', uyelik_yili: 2022 }
]);

db.kitaplar.insertMany([
  { _id: 1, baslik: 'Kürk Mantolu Madonna', tur: 'Roman', sayfa_sayisi: 160 },
  { _id: 2, baslik: 'Fareler ve İnsanlar', tur: 'Roman', sayfa_sayisi: 120 },
  { _id: 3, baslik: 'Sapiens', tur: 'Tarih', sayfa_sayisi: 400 },
  { _id: 4, baslik: 'Kozmos', tur: 'Bilim', sayfa_sayisi: 380 }
]);

db.odunc_islemleri.insertMany([
  { _id: 1, uye_id: 1, kitap_id: 1, odunc_tarihi: new Date('2024-01-10'), iade_edildi_mi: true },
  { _id: 2, uye_id: 1, kitap_id: 3, odunc_tarihi: new Date('2024-02-05'), iade_edildi_mi: false },
  { _id: 3, uye_id: 2, kitap_id: 2, odunc_tarihi: new Date('2024-01-20'), iade_edildi_mi: true },
  { _id: 4, uye_id: 3, kitap_id: 4, odunc_tarihi: new Date('2024-03-01'), iade_edildi_mi: false }
]);

// güncelle sil
db.uyeler.updateOne({ _id: 1 }, { $set: { sehir: 'İstanbul' } });
db.odunc_islemleri.deleteOne({ _id: 3 });

// liste- sorgu toArray() ekrana bastıracak

print("\n üye-alınan kitap listesi ");
printjson(db.odunc_islemleri.aggregate([
  { $lookup: { from: "uyeler", localField: "uye_id", foreignField: "_id", as: "uye" } },
  { $lookup: { from: "kitaplar", localField: "kitap_id", foreignField: "_id", as: "kitap" } },
  { $unwind: "$uye" },
  { $unwind: "$kitap" },
  { $project: { _id: 0, uye_adi: "$uye.ad", kitap_baslik: "$kitap.baslik" } }
]).toArray());

print("\n iade edilmeyen kitplar ");
printjson(db.odunc_islemleri.aggregate([
  { $match: { iade_edildi_mi: false } },
  { $lookup: { from: "uyeler", localField: "uye_id", foreignField: "_id", as: "uye" } },
  { $lookup: { from: "kitaplar", localField: "kitap_id", foreignField: "_id", as: "kitap" } },
  { $unwind: "$uye" },
  { $unwind: "$kitap" },
  { $project: { _id: 0, uye_adi: "$uye.ad", kitap_baslik: "$kitap.baslik" } }
]).toArray());


print("\n en çok kitap alınan üye");
printjson(db.odunc_islemleri.aggregate([
  { $group: { _id: "$uye_id", toplam_odunc: { $sum: 1 } } },
  { $sort: { toplam_odunc: -1 } },
  { $limit: 1 },
  { $lookup: { from: "uyeler", localField: "_id", foreignField: "_id", as: "uye" } },
  { $unwind: "$uye" },
  { $project: { _id: 0, uye_adi: "$uye.ad", toplam_odunc: 1 } }
]).toArray());