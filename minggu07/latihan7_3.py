tinggi = int(input("Masukkan tinggi: "))
lebar  = int(input("Masukkan lebar : "))

for i in range(tinggi):
    for j in range(1, lebar + 1):
        angka = i * lebar + j
        print(angka, end=" ")
    print()
    