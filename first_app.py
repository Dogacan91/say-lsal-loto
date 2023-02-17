import random

sLotoNumaraları = range(1,50) #1 den 49 a kadar olan sayıları aldık.

lotoSonuc = random.sample(sLotoNumaraları, 6) #6 tane numune aldık

sonuc = set(lotoSonuc)

kSayi1 = int(input("Birinci sayıyı gir:(1-49 arasında) "))  #ksayi = kullaniciSayi
kSayi2 = int(input("İkinci  sayıyı gir:(1-49 arasında) "))
kSayi3 = int(input("Üçüncü  sayıyı gir:(1-49 arasında) "))
kSayi4 = int(input("Dördüncü  sayıyı gir:(1-49 arasında) "))
kSayi5 = int(input("Beşinci  sayıyı gir:(1-49 arasında) "))
kSayi6 = int(input("Altıncı  sayıyı gir:(1-49 arasında) "))
kListe = [kSayi1,kSayi2,kSayi3,kSayi4,kSayi5,kSayi6]

kSonuc = set(kListe)  # liste kümeye dönüştürüldü, kesişim bulmak için
sonuc = set(lotoSonuc)
bilinenSayilar1 = kSonuc.intersection(sonuc) #kesişimi alındı

print("Loto Sonuçları", lotoSonuc)
if bilinenSayilar1 == set ():
   print("Hiç sayı bilemediniz")
else:
    print(f" Bildiğiniz Sayılar: {bilinenSayilar1}")

if  len(bilinenSayilar1) >= 3 :
   print (f"{len(bilinenSayilar1)} bildiniz ikramiye kazandınız")    
