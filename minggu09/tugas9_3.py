def hapus_spasi(kalimat):
    return ' '.join(kalimat.split())

kalimat = input("Sebelum hapus spasi: ")
hasil = hapus_spasi(kalimat)
print(f"Hasil hapus spasi: {hasil}")
