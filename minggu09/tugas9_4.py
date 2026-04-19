def max_min_kata(kalimat):
    list_kata = kalimat.split()
    kata_max = max(list_kata, key = len)
    kata_min = min(list_kata, key = len)
    return kata_max, kata_min

kalimat = input("Masukkan kalimat: ")
kata_max, kata_min = max_min_kata(kalimat)
print(f"Kata terpanjang: {kata_max} dengan {len(kata_max)} huruf")
print(f"Kata terpendek: {kata_min} dengan {len(kata_min)} huruf")