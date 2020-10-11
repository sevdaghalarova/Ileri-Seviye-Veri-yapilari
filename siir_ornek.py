"""Bu dosyanın herbir satırını okuyun.
Satırların baş harflerini birbirine ekleyerek bir string oluşturun ve bu string'i ekrana yazdırın."""
with open("siir.txt","r",encoding="utf-8") as file:
    bas=" "
    for i in file:
        bas+=i[0]
    print(bas)
