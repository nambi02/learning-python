def tampilkan_menu():
    print("=== Aplikasi Belanja Modular ===")
    print("1. Tambah Barang")
    print("2. Lihat Keranjang")
    print("3. Simpan Belanjaan")
    print("4. Reset")
    print("5. Keluar")

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
