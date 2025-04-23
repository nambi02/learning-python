import random

angka_rahasia = random.randint(1, 10)
tebakan = int(input("Tebak angka antara 1 sampai 10 : "))


if tebakan == angka_rahasia:
    print ("Selamat! Kamu menebak dengan benar.")
else:
    print (f" Yahh, Salah. Angka yang benar adalah {angka_rahasia}")



