import json
import os
import datetime

#Checking is there basket.json or not
if os.path.exists("basket.json"):
    with open("basket.json","r") as file:
        basket = json.load(file)
else :
    basket =[]

def tampilkan_menu():
    print("=== Toko Mini ===")
    print("1. Tambah Barang")
    print("2. Lihat Keranjang")
    print("3. Total Belanja")
    print("4. Simpan & Keluar")
    print("5. Reset Keranjang")

perkakas = [
    {"nama": "Sapu", "harga": 25000},
    {"nama": "Ember", "harga": 15000}
]

elektronik = [
    {"nama": "TV", "harga": 2500000},
    {"nama": "Kipas Angin", "harga": 500000}
]

obat = [
    {"nama": "Panadol", "harga": 2500},
    {"nama": "Oskadon", "harga": 3000}
]

def tambah_barang():
    print("Pilih kategori:")
    print("1. Perkakas")
    print("2. Elektronik")
    print("3. Obat")
    kategori = input("Masukkan pilihan: ")
    
    if kategori == "1":
        for i, item in enumerate(perkakas):
            print(f"{i+1}. {item['nama']} - Rp{item['harga']}")
        pilih = int(input("Pilih nomor barang: ")) - 1
        basket.append(perkakas[pilih])
        print("Barang ditambahkan ke keranjang!")

    elif kategori == "2":
        for i, item in enumerate(elektronik):
            print(f"{i+1}. {item['nama']} - Rp{item['harga']}")
        pilih = int(input("Pilih nomor barang: ")) - 1
        basket.append(elektronik[pilih])
        print("Barang ditambahkan ke keranjang!")

    elif kategori == "3":
        for i, item in enumerate(obat):
            print(f"{i+1}. {item['nama']} - Rp{item['harga']}")
        pilih = int(input("Pilih nomor barang: ")) - 1
        basket.append(obat[pilih])
        print("Barang ditambahkan ke keranjang!")

    else:
        print("Kategori tidak valid.")
    
def lihat_keranjang():
    if not basket:
        print("Keranjang masih kosong.")
    else:
        for i, item in enumerate(basket):
            print(f"{i+1}. {item['nama']} - Rp{item['harga']}")

def total_belanja():
    total = sum(item["harga"] for item in basket)
    print(f"Total Belanja : Rp{total}")

def simpan_dan_keluar():
    # Simpan ke basket.json
    with open("basket.json", "w") as file:
        json.dump(basket, file)
    
    # Buat Struk belanja
    with open("struk.txt", "w") as struk:
        struk.write("=== STRUK BELANJA ===\n")
        struk.write(f"Tanggal:{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        total = 0

        for i, item in enumerate(basket):
            struk.write(f"{i+1}.{item['nama']} - Rp{item['harga']}\n")
            total += item["harga"]

        struk.write("\n--------------------------\n")
        struk.write(f"TOTAL BELANJA : Rp{total}\n")
        struk.write("Terima kasih telah belanja!\n")

    print("Keranjang berhasil disimpan.")
    print("Struk telah dicetak di file struk.txt")
    print("Sampai jumpa!")
    exit()

def reset_keranjang():
    global basket
    konfirmasi = input("Yakin ingin mereset keranjang? (y/n): ")
    if konfirmasi.lower() == "y":
        basket = []
        if os.path.exists("basket.json"):
            os.remove("basket.json")
        print("Keranjang berhasil dikosongkan.")
    else:
        print("Reset dibatalkan.")

# Program utama
while True:
    tampilkan_menu()
    pilih = input("Pilih menu (1-5): ")

    if pilih == "1":
        tambah_barang()
    elif pilih == "2":
        lihat_keranjang()
    elif pilih == "3":
        total_belanja()
    elif pilih == "4":
        simpan_dan_keluar()
    elif pilih == "5":
        reset_keranjang()
    else:
        print("Pilihan tidak valid.")
