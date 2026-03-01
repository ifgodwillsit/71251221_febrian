try:
    number = int(input("Masukkan bilangan: "))
    keterangan = ("Positif" if number > 0 else "Negatif" if number < 0 else "Nol")
    print(keterangan)

except ValueError:
    print("Masukkan bilangan bulat!")