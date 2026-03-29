def hasil(n):
    for i in range(n, 0, -1):
        faktorial = 1
        baris = ""
        for j in range(i, 0, -1):
            faktorial *= j
            baris += f"{j} "
        print(f"{faktorial} {baris}")

n = int(input("Masukkan nilai n: "))
hasil(n)
