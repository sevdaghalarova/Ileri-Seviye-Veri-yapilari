class Dosya():
    def __init__(self):
        with open ("gogol.txt", "r", encoding="utf-8") as file:
            dosya_icerigi=file.read() #burada dosyamizi okuyoruz
            kelimeler=dosya_icerigi.split() #metni parcalayipliste haline getiriyruz
            self.sade_kelimeler=list() # sadelestirecegimiz kelimeleri bu listeye atacagiz
            for i in kelimeler: # kelimeler uzerinde dolasip
                i=i.strip("/n") # kelimelerdeki bosluk nokta virgul isaretlrini ortadan kaldiriryoruz
                i=i.strip(".")
                i=i.strip(" ")
                i.strip(",")
                self.sade_kelimeler.append(i) # ve bu kelimeleri sade_kelimeler listesine ekliyoruz
    def tum_kelimeler(self):
        kelime_kumesi=set() #yeni kume olusturyouz, her kelimeyi kumeye ekleyecegiz
        for i in self.sade_kelimeler: # sade-kelimeler listesinde gezinip
            kelime_kumesi.add(i) # keimeleri kelime_kumesi setine ekliyoruz. her kelimeden bir tane olacak
    def frekans(self):
        sozluk=dict() # bir sozluk olusturuyoruz
        for i in self.sade_kelimeler: # sade_kelimeler listesinde geziniyouz
            if (i in sozluk): # eger kelime sozlukde varsa
                sozluk[i]+=1 # kelimenin valuesini 1 artiroypruz
            else:
                sozluk[i]=1 # yoksa kelimenin valuesine 1 degerini veriyoruz
        for kelime,sayi in sozluk.items(): # sozlukde dolasip
            print('{} kelimesi {} defa geciyor'.format(kelime,sayi)) # kelime ve sayilarini yazdiriyoruz
            print('_________________________________')
dosya=Dosya()
dosya.frekans()
