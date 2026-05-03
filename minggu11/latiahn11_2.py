bilangan = []

while True:
    masukan = input("Masukkan bilangan (atau 'done' untuk selesai): ")
    if masukan == "done":
        break
    bilangan.append(float(masukan))

rata_rata = sum(bilangan) / len(bilangan)
print("Rata-rata: ", rata_rata)