! index.html, login.html and log.py coded to learn, not for practical solution. 
# Gardrop 
Kullanıcıların kendi sanal gardroplarını oluşturabilecekleri ve uygulamada kombin önerileri alabilecekleri, kullandıkları ve kullanmadıkları kıyafetlerin istatistiklerine ulaşabilecekleri akıllı gardrop uygulaması.

1.)Kullanıcı oluşturma

a.)Database'de tutulacak kullanıcı bilgileri [e-posta, şifre, ad soyad, user-id]
b.)Log-in [e-posta ve şifre ile giriş yapılacak]

2.)Fotoğraf yükleyip kaydetme(özelliklerine göre)

a.)Fotoğraf Yükleme
[Arayüz]:Kamerayla fotoğraf alıp ekleme, galeriden seçip ekleme. Bu eklemeler, özelliklerin açılır menüden seçilmesiyle yapılacak.Açılır menüdeki bu ögeler arayüzde statik olarak seçilecek.
İstenen özellikler: 
Renk, kumaş, sezon, konsept, havadurumu, tür(alt giyim,üst giyim,dış giyim,tek parça,ayakkabı gibi) 
[Backend-API : Site adı/fotografyukle adresinden gerçekleşecek]: Fotoğraf yükleme olayıyla ilgili fonksiyon yazılacak. Bu fonksiyona parametre olarak alınacaklar:bkz:[Flask File Upload]) :Userid, renk, kumaş, sezon, konsept, tür, havadurumu, foto verisi.
Bu parametreler database'de kıyafet tablosunda kaydedilecek.Kaydetme esnasında da otomatik kıyafetid oluşturacak.(mysql auto increment)

QRCode ile foto yükleme: Yukarda sayılan özellikler karekodun içerisinde olacak, telefon bunu veriye dönüştürüp api ile gönderecek.

3.)Kombin Like

Konseptini seçecek ve bu konsepte göre diğer bilgiler otomatik olarak seçilerek öneride bulunacak.
Havadurumu ve sezonu backend'de otomatik olarak alacak, buna göre tek seferde türlerden birer tane alarak kombin yapacak. Bu kombinler arayüzde slider şeklinde gösterilecek.
a.)Arayüz
Konseptler ikonlar şeklinde tuşlarla görüntülenecek. Ekran parçalara bölünecek ve ikonlar şeklinde konseptler yazacak. Kullanıcı bir tanesini seçecek ( konseptlerden birini seçtiğinde konseptin ismini siteadı/kombinöner?kombinismi şeklinde backend e gönder ) , ardından kombin sayfasına gidecek. Kombin sayfasında, her sayfada bir kombin olacak ve sayfa geçişleri slider olarak yapacak. Bu şekilde kombinler listelenecek.

b.)Backend
siteadı/kombinöner?kombinismi adresinden gelen kombin id'sine göre kombin öneren fonksiyon çalışacak. Bu fonksiyon respond olarak kombin id'si, altgiyimid, üstgiyimid, dısgiyimid, ayakkabiid, tekparcaid özelliklerini liste olarak gönderecek.JSON listesi olarak gönderecek.

-Bu fonksiyonun çalışma mantığı: En başta havadurumu ve sezon bilgileri python kütüphaneleri kullanılarak bir değişkene kaydedilecek. Eldeki bu değişkenler( havadurumuid, sezonid, konseptid) öneri verecek olan sql sorgusunun WHERE kısmına yazılarak öneri sorgusu çalışacak. 
-Bu sorgunun çalışma mantığı : 
En başta WHERE komutu ile konsept, havadurumu ve sezona göre kıyafet tablosundaki veriler filtrelenecek. Daha sonra elde ettiğimiz kıyafetid, renk, tür, kumaş verileri, rank fonksiyonu ile her bir tür için sütun oluşturulacak. Bu durumda elimizde türid, kıyafetid, renk, kumaş verileri olacak. Kumaş ve renk özellikleri arasındaki ilişkiye göre algoritma çıkarılacak.
Sonuç olarak kombin id'si, altgiyimid, üstgiyimid, dısgiyimid, ayakkabiid, tekparcaid çıktısı olacak.

4.)LIKE(seçim)
Arayüzde sunulan kombin önerilerinin altında beğenme butonu olacak.Bu buton, seçtiği kombini belirleyecek.Bu butona tıkladığı anda o anki kombinin verileri(kombin id'si, altgiyimid, üstgiyimid, dısgiyimid, ayakkabiid, tekparcaid-arayüzden gelecek) beğenilenler tablosunda userid'si,havadurumu,sezon, konsept (backend den gelecek) verileri eklenerek kaydedilecek. 
Bu bilgiler history sayfasında kullanılacak.

5.)HISTORY - BAĞIŞLA
siteadı/history adresinde, beğenilenler tablosundaki veriler verilecek. Beğenme işleminden sonra, beğenilenler tablosunda olmayan kıyafetid leri yeni bir sayfada bağışla adı altında listelenecek.
-Backend: siteadı/bagısla api adresindeki fonksiyona parametre olarak kiyafetid verilecek.























