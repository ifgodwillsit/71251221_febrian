try:
    a = int(input("Masukkan bilangan pertama: "))
    b = int(input("Masukkan bilangan kedua: "))
    c = int(input("Masukkan bilangan ketiga: "))

    modus = a if a > b and a > c else b if b > a and b > c else c
    print(f"Terbesar: {modus}")

except ValueError:
    print("Masukkan bilangan bulat!")