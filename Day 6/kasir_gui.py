import tkinter as tk
from tkinter import messagebox
import json
import os

keranjang = []

def tambah_barang():
    nama = entry_nama.get()
    try:
        harga=int(entry_harga.get())
        keranjang.append({"nama": nama, "harga":harga})
        messagebox.showinfo("Sukses", f"{nama} berhasil ditambahkan!")
        entry_nama.delete(0, tk.END)
        entry_harga.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Erorr", "Harga harus berupa angka!")

def lihat_keranjang():
    if not keranjang:
        messagebox.showinfo("Keranjang", "Keranjang kosong.")
    else:
        isi="\n".join(f"{i+1}. {item['nama']} - Rp{item['harga']}" for i, item in enumerate (keranjang))
        messagebox.showinfo("Keranjang", isi)

def simpan_belanja():
    file_name = "Day 6/belanja_gui.json"
    if not os.path.exists("Day 6"):
        os.makedirs("Day 6")
    data=[]
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            data=json.load(file)
    data.append(keranjang.copy())
    with open(file_name, "w") as file:
        json.dump(data, file)
    messagebox.showinfo("Suksess", "Belanjaan berhasil disimpan!")
    keranjang.clear()

def reset_keranjang():
    keranjang.clear()
    messagebox.showinfo("Reset", "Keranjang dikosongkan.")

def exit_keluar():
    messagebox.showinfo("Keluar.", "Terima kasih, sampai jumpa!")
    root.destroy()

#Gui Setup
root = tk.Tk()
root.title("Kasir GUI Mini")

label_nama = tk.Label(root, text="Nama Barang:")
label_nama.pack()
entry_nama = tk.Entry(root)
entry_nama.pack()

label_harga = tk.Label(root, text="Harga Barang:")
label_harga.pack()
entry_harga = tk.Entry(root)
entry_harga.pack()

btn_tambah = tk.Button(root, text="Tambah Barang", command=tambah_barang)
btn_tambah.pack()

btn_lihat = tk.Button(root, text="Lihat Keranjang", command=lihat_keranjang)
btn_lihat.pack()

btn_simpan = tk.Button(root, text="Simpan Belanjaan", command=simpan_belanja)
btn_simpan.pack()

btn_reset = tk.Button(root, text="Reset Keranjang", command=reset_keranjang)
btn_reset.pack()

btn_exit = tk.Button(root, text="Exit",command=exit_keluar)
btn_exit.pack()

root.mainloop()








