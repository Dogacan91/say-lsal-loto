import random

sLotoNumaraları = range(1,50) #1 den 49 a kadar olan sayıları aldık.

lotoSonuc = random.sample(sLotoNumaraları, 6) #6 tane numune aldık

sonuc = set(lotoSonuc)

kSayi11 = int(input("Birinci sayıyı gir:(1-49) "))  #ksayi = kullaniciSayi
kSayi21 = int(input("İkinci  sayıyı gir: "))
kSayi31 = int(input("Üçüncü  sayıyı gir: "))
kSayi41 = int(input("Dördüncü  sayıyı gir: "))
kSayi51 = int(input("Beşinci  sayıyı gir: "))
kSayi61 = int(input("Altıncı  sayıyı gir: "))
kListe = [kSayi11,kSayi21,kSayi31,kSayi41,kSayi51,kSayi61]

kSonuc = set(kListe)  # liste kümeye dönüştürüldü, kesişim bulmak için
sonuc = set(lotoSonuc)
bilinenSayilar1 = kSonuc.intersection(sonuc) #kesişimi alındı

print("Loto Sonuçları", lotoSonuc)
if bilinenSayilar1 == set():
   print("Hiç sayı bilemediniz")
else:
    print(f" a kolonunda Bildiğiniz Sayılar: {bilinenSayilar1}")