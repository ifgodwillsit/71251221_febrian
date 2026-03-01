try:
    sisi1 = int(input("Masukkan sisi 1: "))
    sisi2 = int(input("Masukkan sisi 2: "))
    sisi3 = int(input("Masukkan sisi 3: "))

    keterangan = ("3 sisi sama" if sisi1 == sisi2 == sisi3 else "2 sisi sama" if sisi1 == sisi2 or sisi2 == sisi3 or sisi3 == sisi1 else "Tidak ada yang sama")
    print(keterangan)

except ValueError:
    print("Masukkan bilangan bulat!")