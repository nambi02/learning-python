import json
import os

# Checking is there keranjang.json or not
if os.path.exists("keranjang.json"):
    with open("keranjang.json","r") as file:
        keranjang = json.load(file)
else :
    keranjang =[]

def tampilkan_menu():
    print("=== Kasir Simpan Data ===")
    print("1. Tambah Barang")
    print("2. Lihat Keranjang")
    print("3. Total Belanja")
    print("4. Simpan & Keluar")
    print("5. Reset Keranjang")

def tambah_barang():
    nama = input("Nama Barang : ")
    harga = int(input("Harga Barang : "))
    keranjang.append({"nama": nama, "harga": harga})
    print("Barang ditambahkan ke keranjang!")

def lihat_keranjang():
    if not keranjang:
        print("Keranjang masih kosong.")
    else:
        for i, item in enumerate(keranjang):
            print(f"{i+1}. {item['nama']} - Rp{item['harga']}")

def total_belanja():
    total = sum(item["harga"] for item in keranjang)
    print(f"Total Belanja: Rp{total}")

def simpan_dan_keluar():
    with open("keranjang.json", "w") as file:
        json.dump(keranjang, file)
    print("Keranjang berhasil disimpan. Sampai jumpa!")
    exit()

def reset_keranjang():
    global keranjang
    konfirmasi = input("Yakin ingin mereset keranjang? (y/n): ")
    if konfirmasi.lower() == "y":
        keranjang = []
        if os.path.exists("keranjang.json"):
            os.remove("keranjang.json")
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

