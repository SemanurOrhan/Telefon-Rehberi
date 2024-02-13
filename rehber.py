import sqlite3


class rehber_kaydi(object):
    def __init__(self, isim, soyisim, telefon_numarasi, yas, arama_sayisi):
        self.isim = isim
        self.soyisim = soyisim
        self.telefon_numarasi = telefon_numarasi
        self.yas = yas
        self.arama_sayisi = arama_sayisi

    def __str__(self):
        return "İsim:{}\nSoyisim:{}\nTelefon Numarası:{}\nYas:{}\nArama Sayısı:{}".format(self.isim, self.soyisim, self.telefon_numarasi, self.yas, self.arama_sayisi) 
    

class Rehber():
    def __init__(self):
        self.connect_database()

    def connect_database(self):
        self.connect = sqlite3.connect("telefon_rehberi.db")
        self.cursor = sqlite3.connect.cursor()
        table_query = "CREATE TABLE IF NOT EXISTS rehbers(İsim TEXT, soyisim TEXT, telefon_numarasi TEXT, yas TEXT, arama_sayisi INT)"
        self.cursor.execute(table_query)
        self.connect.commit()

    def cut_connection(self):
        self.connect.close()

    def show_rehber(self):
        query= "SELECT * FROM rehbers"
        self.cursor.execute(query)
        rehber_listesi= self.cursor.fetchall()

        if(len(rehber_listesi)== 0):
            print("Rehberde kişi yok.")
        else:
            for i in rehber_listesi:
                kisi= rehber_kaydi(i[0], i[1], i[2], i[3], i[4])
                print(kisi)

    def search_person(self,isim):
        sorgu="SELECT *FROM rehbers WHERE isim = ?"
        self.cursor.execute(sorgu,(isim,))
        kisi_listesi =self.cursor.fetchall()

        if (len(kisi_listesi)== 0):
            print("Böyle bir kişi yoktur.")
        else:
            kisi= rehber_kaydi(  kisi_listesi[0][0], kisi_listesi[0][1], kisi_listesi[0][2], kisi_listesi[0][3], kisi_listesi[0][4])
            print(kisi)


    def kisi_ekle(self, kisi):
        sorgu= "INSERT INTO rehbers values(?,?,?,?,?)"
        self.cursor.execute(sorgu,( kisi.isim, kisi.soyisim, kisi.telefon_numarasi, kisi.yas, kisi.arama_sayisi ))
        self.connect.commit()

    def kisi_sil(self, isim):
        sorgu= "DELETE FROM rehbers WHERE isim = ?"
        self.cursor.execute(sorgu,( isim ))
        self.connect.commit()

    def arama_sayisi_artma(self, isim):
        sorgu= "SELECT * FROM rehbers WHERE isim = ?"
        self.cursor.execute(sorgu,(isim,))
        kisiler= self.cursor.fethall()

        if(len(kisiler)==0):
            print("Bulunmuyor...")
        else:
            kisi = kisiler[0][4]
            arama_sayisi += 1

            sorgu2="UPDATE rehbers SET arama_sayisi = ? WHERE isim = ?"
            self.cursor.execute(sorgu2,(arama_sayisi, isim))
            self.connect.commit()


