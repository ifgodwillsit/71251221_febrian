def ganjil(bawah, atas):
    try:
        if bawah <= atas:
            # Urutan naik: dari bawah ke atas
            start = bawah if bawah % 2 != 0 else bawah + 1
            for i in range(start, atas + 1, 2):
                print(i, end=" ")
        else:
            # Urutan turun: dari bawah ke atas (bawah > atas)
            start = bawah if bawah % 2 != 0 else bawah - 1
            for i in range(start, atas - 1, -2):
                print(i, end=" ")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    
bawah = int(input("Masukkan batas bawah: "))
atas = int(input("Masukkan batas atas: "))
ganjil(bawah, atas)