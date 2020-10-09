yazi="***Ben Python'u seviyorum***"
print(yazi.upper()) # tum karakterleri buyuk harfe cevirir
print(yazi.lower()) # tum karakterleri kucuk harfe ceviriyor
print(yazi.replace("e","a")) # e harfini , a ile degistirdi( karakterlerin yerlerini degismek icin kullanilir)
print(yazi.startswith("Ben")) # stringin ne ile basladigina gore True veya False deger dondurur
print(yazi.endswith("sum")) # stringin ne ile bitdigine gore True veya False deger dondurur
print(yazi.split(" ")) # stringi , ile ayirip listeye atiyor
print(yazi.strip("*")) # stringin basinda ve sonundaki * karakterini siler
print(yazi.lstrip("*")) # stringin basindaki * karakterini siler
print(yazi.rstrip("*")) #stringin sonundaki * karakterini siler
print("//".join(yazi)) # yazilan karakteri stringle birlestirir
print(yazi.count("e")) # "e" karakteri string icinde kac defa gecer
print(yazi.count("e",7)) # 7'ci index'ten baslayarak "e" karakteri bu stringde kac defa geciyor
print(yazi.find("e")) # "e" karakterinin bu stringde bulundugu ilk indexi dondurur
print(yazi.rfind("e")) # "e" karakterinin bu stringde bulundugu son indexi dondurur