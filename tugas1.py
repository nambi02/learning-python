import random
# Perulangan
for percobaan in range(3):
    angka_rahasia = random.randint(1, 10)
    tebakan = int(input(f"Tebak angka antara 1 sampai 10 {percobaan + 1} : "))

    if tebakan == angka_rahasia:
            print ("Selamat! Kamu menebak dengan benar")
            break
    else:
        print (f"Yahh, Salah. Angka yang benar adalah {angka_rahasia}")
    if percobaan == 2:
         print (f"Maaf, anda telah menghabiskan kesempatan anda. Angka rahasianya adalah : {angka_rahasia}")