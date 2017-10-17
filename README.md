SCROLL DOWN FOR ENGLISH DESCRIPTION !

! index.html, login.html and log.py öğrenme amaçlı kodlandı,pratik çözüm için değil. 

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
 #######################################################################################################################################

! index.html, login.html and log.py coded to learn, not for practical solution. 

# Gardrop 

An intelligent wardrobe application where users can create their own virtual gardroplines and get combinatorial recommendations on the application, plus access to the statistics of the garments they use and do not use.

1.) Create user

a.) User information to be kept in the database [e-mail, password, name, user-id] b.) Log-in [login with e-mail and password]

2.) Uploading and saving photos (by features)

a.) Uploading Photos [Interface]: Importing and adding photos with camera, selecting from gallery. These attachments will be made by selecting the properties from the drop-down menu. These items in the drop-down menu will be selected statically in the interface. [Backend-API: Site name / photo]: The function related to the photo loading event will be written in the form of color, fabric, season, concept, climate, genre (underwear, topwear, outerwear, This function will be taken as a parameter: see [Flask File Upload]): Userid, color, fabric, season, concept, type, weather, photo. These parameters will be saved in the table of clothing in the database. During the save, automatic clothes will also be created (mysql auto increment)

Photo upload with QRCode: The features listed above will be in the square, the phone will convert it to a date and send it via API.

3.) Like the Combine

Will choose the concept and according to this concept other information will be automatically selected and suggested. Weather and season will be automatically received at backend, so you will get one from the species at once and combine them. These combos will be displayed as sliders in the interface. a.) Interface Concepts will be displayed in the form of icons. The screen will be divided into pieces and will write concepts in the form of icons. The user will select one (when the user selects one of the concepts, send the concept name to the backend in the form of the site name / combination combination), then go to the combine page. On the combine page, there will be a combination on each page and page transitions will be made as a slider. In this way the combos will be listed.

b.) The function that proposes the combination according to the combination id from the backend sitename / combinationinfo combination name will work. This function will send a list of the combined id, altgiyimid, ustgiyimid, disgiyimid, ayakkabiid, and tekparcid properties as a JSON list.

-Working logic of this function: At first, a variable will be recorded using python libraries for weather and seasonal information. These variables (havadurumuid, seasonid, conceptid) will be suggested in the WHERE part of the sql query which will give suggestions. -Working logic of this query: In the beginning, the WHERE command will filter the data of the concept, weather and season table according to the dress code. Then we will create the columns for each type with the clothes, color, type, fabric data, rank function we have obtained. In this case, you'll have to get genids, clothes, colors, fabric. The algorithm will be derived according to the relationship between fabric and color properties. As a result, the combination of idiosis, altgimide, supergymide, dysgiumide, shakebird, tekparcaid output will be.

4.) LIKE (selection) Below the combination suggestions presented in the interface, the button will be selected. This button will select the selected combination. If you click this button, the combination of the current combination (kombin id, altgimid, ustgiyimid, userid in the favorites table, the weather forecast, the season, the concept (backend) data. This information will be used on the history page.

5.) HISTORY - DONATE Site name / history will be given in the table of likes. After the liking process, clothes that are not in the favorites tab will be listed on the new page under the name of donate. -Backend: sitename / bagisla api will be given as a parameter to the function at the price.






















