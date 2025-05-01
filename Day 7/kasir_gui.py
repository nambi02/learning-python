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
    file_name = "Day 7/belanja_gui.json"
    if not os.path.exists("Day 7"):
        os.makedirs("Day 7")
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
root.geometry("335x355") #Atur Ukuran Jendela
root.configure(bg="#9E9E9E")  # background color window

font_settings=("Arial", 12)

label_nama = tk.Label(root, text="Nama Barang:", font=font_settings)
label_nama.grid(row=0, column=0, pady=10, padx=10, sticky="w")
entry_nama = tk.Entry(root, font=font_settings)
entry_nama.grid(row=0, column=1, pady=10, padx=10)

label_harga = tk.Label(root, text="Harga Barang:", font=font_settings)
label_harga.grid(row=1, column=0, pady=10, padx=10, sticky="w")
entry_harga = tk.Entry(root, font=font_settings)
entry_harga.grid(row=1, column=1, pady=10, padx=10)

btn_tambah = tk.Button(root, text="Tambah Barang", font=font_settings, bg="#4CAF50", fg="white", command=tambah_barang)
btn_tambah.grid(row=2, column=0, pady=10, padx=10, columnspan=2, sticky="ew")

btn_lihat = tk.Button(root, text="Lihat Keranjang", font=font_settings, bg="#2196F3", fg="white", command=lihat_keranjang)
btn_lihat.grid(row=3, column=0, pady=10, padx=10, columnspan=2, sticky="ew")

btn_simpan = tk.Button(root, text="Simpan Belanjaan", font=font_settings, bg="#FF9800", fg="white", command=simpan_belanja)
btn_simpan.grid(row=4, column=0, pady=10, padx=10, columnspan=2, sticky="ew")

btn_reset = tk.Button(root, text="Reset Keranjang", font=font_settings, bg="#f44336", fg="white", command=reset_keranjang)
btn_reset.grid(row=5, column=0, pady=10, padx=10, columnspan=2, sticky="ew")

btn_exit = tk.Button(root, text="Exit", font=font_settings, bg="#9E9E9E", fg="white", command=exit_keluar)
btn_exit.grid(row=6, column=0, pady=10, padx=10, columnspan=2, sticky="ew")

root.mainloop()








