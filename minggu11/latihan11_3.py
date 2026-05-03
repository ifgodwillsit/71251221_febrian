nama_file = input("Masukkan nama file: ")

with open(nama_file, "r") as f:
    teks = f.read()

kata_teks = teks.split()
keyword = []

for kata in kata_teks:
    kata = kata.lower().strip(".,!?\"'")
    if kata not in keyword:
        keyword.append(kata)

print("Kata-kata unik dalam artikel: ")
print(keyword)