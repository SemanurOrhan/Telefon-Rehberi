from rehber import *

print("""********************************
      
      TELEFON REHBERİNE HOŞGELDİNİZ.

      İŞLEMLER;
      1. Rehberi Göster
      2. Kişi Sorgulama
      3. Kİşi Ekle
      4. Kişi Sil
      5. Arama Sayısı
      
      Çıkmak için 'Q' ya basın. 

      ********************************""")

rehber= Rehber()

while True:
    islem = input("Yapacağınız İşlem:")
    if(islem == "Q"):
        print("Program sonlandırılıyor.....")
        break
    elif(islem == "1"):
        rehber.show_rehber()

    elif(islem == "2"):
        isim = input("Aramak istediğiniz kişiyi giriniz: ")
        print("Kişi sorgulanıyor...")
        rehber.search_person(isim)

    elif(islem == "3"):
        isim = input("İsim: ")
        soyisim= input("Soyisim: ")
        telefon_numarasi= input("Telefon Numarası: ")
        yas= input("Yas: ")
        arama_sayisi= input("Arama Sayisi: ")

        yeni_kisi= rehber_kaydi(isim, soyisim, telefon_numarasi, yas, arama_sayisi)
        print("Kişi ekleniyor.....")

        rehber.kisi_ekle(yeni_kisi)
        print("Kişi eklendi.")


    elif(islem == "4"):
        isim= input("Silmek istediğiniz kişiyi giriniz: ")
        cevap=input("Emin misiniz? (E/H) ")
        if (cevap == "E"):
            print("Kişi siliniyor...")
            rehber.kisi_sil(isim)
            print("Kişi silindi.")

    elif(islem == "5"):
        isim= input("Aramak istediğiniz ismi giriniz: ")
        print("Aranıyor...")
        rehber.arma_sayisi_artma(isim)
        print("Arama sayısı arttırıldı.")
    else:
        print("Geçersiz işlem...")
