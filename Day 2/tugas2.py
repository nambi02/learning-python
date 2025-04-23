def tampilkan_menu():
    print("=== Kasir Mini ===")
    print("1. Tambah Barang")
    print("2. Lihat Keranjang")
    print("3. Total Belanja")
    print("4. Keluar")

keranjang = []

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
        keranjang.append(perkakas[pilih])

    elif kategori == "2":
        for i, item in enumerate(elektronik):
            print(f"{i+1}. {item['nama']} - Rp{item['harga']}")
        pilih = int(input("Pilih nomor barang: ")) - 1
        keranjang.append(elektronik[pilih])

    elif kategori == "3":
        for i, item in enumerate(obat):
            print(f"{i+1}. {item['nama']} - Rp{item['harga']}")
        pilih = int(input("Pilih nomor barang: ")) - 1
        keranjang.append(obat[pilih])

    else:
        print("Kategori tidak valid.")
    
def lihat_keranjang():
    if not keranjang:
        print("Keranjang masih kosong.")
    else:
        for i, item in enumerate(keranjang):
            print(f"{i+1}. {item['nama']} - Rp{item['harga']}")

def total_belanja():
    total = sum(item["harga"] for item in keranjang)
    print(f"Total Belanja : Rp{total}")

while True:
    tampilkan_menu()
    pilih = input("Pilih Menu (1-4) : ")

    if pilih == "1":
        tambah_barang()
    elif pilih == "2":
        lihat_keranjang()
    elif pilih == "3":
        total_belanja()
    elif pilih == "4":
        print("Terimakasih Telah Belanja!")
        break
    else:
        print("Pilihan Tidak Valid")
