import random

sazlik= "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

soru = int (input ("Şifren ne kadar uzun olsun?"))

password = ""

for i in range(soru):
    sozluk = random.choice(sazlik)

    password += sozluk

print("Şifreniz:",password)
