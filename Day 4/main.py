from logic import tampilkan_menu, lihat_keranjang, reset_riwayat
from data_handler import load_data, save_data

keranjang = []
file_name = "Day 4/belanja.json"

while True:
    tampilkan_menu()
    pilih = input("Pilih menu: ")

    if pilih == "1":
        nama = input("Nama barang: ")
        harga = int(input("Harga barang: "))
        keranjang.append({"nama": nama, "harga": harga})

    elif pilih == "2":
        lihat_keranjang(keranjang)

    elif pilih == "3":
        data = load_data(file_name)
        data.append(keranjang)  # Tambah transaksi baru
        save_data(data, file_name)
        print("Transaksi berhasil disimpan!")
        keranjang = []

    elif pilih == "4":
        keranjang = []
        reset_riwayat(keranjang, file_name)
        print("Keranjang dikosongkan.")

    elif pilih == "5":
        print("Terima kasih, sampai jumpa!")
        break

    else:
        print("Menu tidak valid.")
