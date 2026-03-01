try:
    bulan = int(input("Masukkan bulan (1-12): "))
    a = (1, 3, 5, 7, 8, 10, 12)
    b = (4, 6, 9, 11)

    keterangan = ("31" if bulan in a else "30" if bulan in b else "28" if bulan == 2 else "Input bukan 1-12!")
    print(f"Jumlah hari: {keterangan}")
except ValueError:
    print("Masukkan bilangan bulat!")
    