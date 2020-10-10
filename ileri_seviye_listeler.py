# extend() listenin sonun eleman ekler, bu bir liste de olabilir
liste=[1,2,3,4,5,6]
liste1=[1,2,3,3,2]

liste.extend(liste1)
print(liste)

# insert() her hangi bir indexe eleman ekler
liste1.insert(2,10)
print(liste1)

# remove() eleman ismine gore o elemani siliyoruz
liste1.remove(10)
print(liste1)

# index() elemanin oldugu ilk indexi dondurur
print(liste1.index(2))

# count() verilen elemandan kac tane var
print(liste1.count(2))

# sort() sayilari kucukten buyuye, stringleri ise alfabetik siralar
liste1.sort()
print(liste1)
