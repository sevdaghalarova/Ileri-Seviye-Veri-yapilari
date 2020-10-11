"""Elinizde "mailler.txt" adında , maillerin ve bazı yazıların bulunduğu bir dosya olsun.
Bu dosyanın her bir satırını okuyun ve sadece mail formatına uygun olanları ekrana yazdırın."""



with open("mail.txt","r",encoding="utf-8") as file:
    liste=[]
    for i in file:
        i=i[:-1]
        if i.endswith(".com") and i.find("@")!=-1:
            print(i)





