import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

sifre_uzunlugu = int(input("İstediğiniz şifre uzunluğunu giriniz :"))

sifre = ""

for i in range(sifre_uzunlugu):
    sifre += random.choice(karakterler)

print("şifreniz :", sifre)
