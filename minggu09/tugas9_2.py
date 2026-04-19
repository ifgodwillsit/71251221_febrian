import re

def hitung_frekuensi(kalimat, keyword):
    pattern = r"\b" + re.escape(keyword) + r"\b"
    frekuensi = re.findall(pattern, kalimat, flags=re.IGNORECASE)
    return len(frekuensi)

kalimat = input("Masukkan kalimat: ")
keyword = input("Masukkan keyword yang ingin dicari: ")
hasil = hitung_frekuensi(kalimat, keyword)
print(f"Kata ''{keyword}'' ada {hasil}")