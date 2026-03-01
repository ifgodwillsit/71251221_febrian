try:
    suhu = int(input("Masukkan suhu tubuh: "))
    keterangan = ("Anda demam" if suhu >= 38 else "Anda tidak demam")
    print(keterangan)

except ValueError:
    print("Input hanya bisa dalam bilangan bulat!")