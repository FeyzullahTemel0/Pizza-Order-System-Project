

1) Dosya içerisinde yer alan mysql bağlanıtısı için user ve password değiştirilmelidir.

2) Database'in aynısını oluşturabilmek için yeni bir şema oluşturup o şema içerisinde yeni query açarak
   query içerisine bu kodları yapıştırın. Şema isminizin 'projeglobalaıhub' olmasına dikkat edin!!!

3) vs Code kullanıyorsanız pymysql kütüphanesini pip install pymysql şeklinde indirmeyi unutmayın!!!

CREATE TABLE `ordersystem` (
  `id` int NOT NULL AUTO_INCREMENT,
  `credit_card_username` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `userid` int NOT NULL,
  `order_description` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `order_time` datetime NOT NULL,
  `credit_card_number` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `credit_card_last_time` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `cvv` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `credit_cadt_password` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci




#### Yapılan Yenilikler 
    1) Pizza seçiminden sonra pizza boyutu seçimi eklendi
    2) Pizza boyutunun seçimine göre fiyat hesaplaması eklendi
    3) Ödeme ekranı için toplam hesaplama düzenlendi.Güncel
