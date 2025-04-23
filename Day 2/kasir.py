def tampilkan_menu():
    print("=== Kasir Mini ===")
    print("1. Tambah Barang")
    print("2. Lihat Keranjang")
    print("3. Total Belanja")
    print("4. Keluar")

keranjang = []

def tambah_barang():
    nama = input("Nama Barang : ")
    harga = int(input("Harga Barang : "))
    keranjang.append({"nama": nama, "harga": harga})
    print("Barang Ditambahkan!")

def lihat_keranjang():
    for i, item in enumerate(keranjang):
        print(f"{i+1}.{item['nama']} - Rp{item['harga']}")

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
