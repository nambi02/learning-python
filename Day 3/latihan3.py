with open("catatan.txt", "w") as file:              # Writting .txt file
    file.write("Halo, ini baris pertama!\n")
    file.write("Baris kedua juga bisa.")

with open("catatan.txt", "r") as file:               # Reading .txt file
    isi = file.read()
    print(isi)

import json                                          # Writting .json file

data = {"nama": "Syarip", "umur": 25}

with open("data.json", "w") as file:
    json.dump(data, file)

with open("data.json", "r") as file:                 # Reading .json file
    isi = json.load(file)
    print(isi["nama"])  # ➜ Syarip
