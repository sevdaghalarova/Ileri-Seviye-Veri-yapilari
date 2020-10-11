'''İleri Seviye Veri Yapıları ve Objeler
Problem 1
Elinizde uzunca bir string olsun.

            "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"


Bu string içindeki harflerin frekansını (bir harfin kaç defa geçtiği) bulmaya çalışın.'''


metin=  "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
sozluk=dict()
for i in metin:
   if i in sozluk:
       sozluk[i]+=1
   else:
       sozluk[i]=1

for i,j in sozluk.items():
    print("{} harfi, {} defa keciyor".format(i,j))






