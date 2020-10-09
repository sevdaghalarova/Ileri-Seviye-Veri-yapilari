# setler listeler gibidir fakar bir elemandan sadece 1 tane tutuyor
x={1,3,4,2,4,3}
y={1,2,4}
z={20,90,40}
print(x)

# sirasiz veri tipidir, index'ler ile ulasilamaz
for i in x:
    print(i)

x.add(9) # yeni eleman ekler
print(x.difference(y)) # 2 kumenin farkini alir
(x.difference_update(y)) # 2 kumenin kesisimini alip x'e atar
x.discard(3) # kumeden eleman cikarir
x.intersection(y) # iki kumenin ortak elemanlarini bulur
x.intersection_update(y) # iki kumenin ortak elemanlarini bulup x'e atar
x.isdisjoint(z) #iki kumenin kesisimi bos mu? True veya False doner
x.issubset(y) # x y'nin altkumesi mi? True veya False doner
x.union(y) # iki kumenin birlesimini verir
x.update(y) # x-i yeniler




