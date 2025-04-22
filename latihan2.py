def sapa(nama):                         # Function def Practice
    print(f"Halo, {nama}! Selamat belajar Python!")
sapa("Syarip")

def sapa():                             # Function with input
    nama = input("Masukkan nama: ")
    print(f"Halo, {nama}")

sapa()

buah = ["apel","jeruk","mangga"]        # Listing Practrice
print(buah[1])          #apel
buah.append("pisang")   #tambah item
print(len(buah))
print(buah[3])        #jumlah item

mahasiswa = {                           # Dictionary Practice

    "nama": "Syarip",
    "umur": "25",
    "jurusan": "informatika" 
}

print (mahasiswa["nama"]) # Memangil label "Syarip"
