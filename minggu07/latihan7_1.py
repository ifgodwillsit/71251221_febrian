def prima(bilangan):
    if bilangan <= 2:
        return f"Tidak ada bilangan prima di bawah {bilangan}"
    else:
        for i in range(bilangan - 1, 1, -1):
            is_Prima = True
            for j in range(2, int(bilangan / 2 + 1)):
                if i % j == 0:
                    is_Prima = False
                    break
                if is_Prima:
                    return i

bilangan = int(input("Masukkan bilangan: "))
hasil = prima(bilangan)
print(f"Bilangan prima terdekat dari {bilangan} adalah {hasil}")
