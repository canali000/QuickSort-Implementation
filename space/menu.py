# menü işlemleri
def kullaniciMenu():
    print("-----------------")
    print("Kullanıcı Menüsü")
    print("-----------------")
    print("1- Kitap Görüntüleme")
    print("2- Kitap Ödünç Alma")
    print("3- Kitap İade Etme")
    print()
    secim = input("Seçim: ").lower().rstrip()
    print()

    if secim == "1":
        kitapGoruntule()
    elif secim == "2":
        oduncAl(secim)        
    elif secim == "3":
        oduncAl(secim)        
    else:
        kullaniciMenu()
 
def kitapGoruntule():
    pass

def oduncAl(secim):
    pass