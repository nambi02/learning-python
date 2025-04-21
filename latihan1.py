print("Halo, Syarip!")
nama = input("Masukkan nama kamu : ")
umur = int(input("Masukkan umur kamu : "))

if umur >= 25:
    print (f"Hai {nama}, semangat! Umur bukan penghalang belajar")
else:
    print(f"Hai {nama}, semangat! kamu masih muda banget!")

# Perulangan

for i in range(1, 6):
    print(f"Belajar Python ke-{i}")