def tampilkan_menu():
    print("=== Aplikasi Belanja Modular ===")
    print("1. Tambah Barang")
    print("2. Lihat Keranjang")
    print("3. Simpan Belanjaan")
    print("4. Reset")
    print("5. Hapus Barang")
    print("6. Edit Barang")
    print("7. Keluar")

def lihat_keranjang(keranjang):
    if not keranjang:
        print("Keranjang kosong.")
    else:
        for i, item in enumerate(keranjang):
            print(f"{i+1}. {item['nama']} - Rp{item['harga']}")

import os

def reset_riwayat(keranjang, file_name):
    keranjang.clear()  # atau keranjang = [] jika tidak return
    if os.path.exists(file_name):
        os.remove(file_name)
    print("Keranjang & riwayat transaksi berhasil dihapus.")

def hapus_barang(keranjang):
    if not keranjang:
        print("Keranjang kosong.")
        return
    for i, item in enumerate(keranjang):
        print(f"{i+1}. {item['nama']} - Rp{item['harga']}")
    try:
        index = int(input("Masukkan nomor barang yang ingin dihapus: ")) - 1
        if 0 <= index < len(keranjang):
            deleted = keranjang.pop(index)
            print(f"{deleted['nama']} telah dihapus dari keranjang.")
        else:
            print("Nomor tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")

def edit_barang(keranjang):
    if not keranjang:
        print("Keranjang kosong.")
        return
    for i, item in enumerate(keranjang):
        print(f"{i+1}. {item['nama']} - Rp{item['harga']}")
    try:
        index = int(input("Pilih barang yang ingin diedit: ")) - 1
        if 0 <= index < len(keranjang):
            nama_baru = input("Nama baru: ")
            while True:
                try:
                    harga_baru = int(input("Harga baru: "))
                    break
                except ValueError:
                    print("Harga harus berupa angka.")
            keranjang[index] = {"nama": nama_baru, "harga": harga_baru}
            print("Barang berhasil diedit.")
        else:
            print("Nomor tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")