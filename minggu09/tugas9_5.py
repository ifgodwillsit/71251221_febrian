import re
from datetime import datetime, date

def cari_tanggal(teks):
    pattern = r"\b(\d{4})-(\d{2})-(\d{2})\b"
    hasil = re.findall(pattern, teks)
    hari_ini = date.today()

    for tahun, bulan, hari in hasil:
        tanggal_asli = datetime(int(tahun), int(bulan), int(hari))
        tanggal_format = f"{hari}-{bulan}-{tahun}"
        selisih = abs((hari_ini - tanggal_asli.date()).days)
        print(f"{tanggal_format} selisih {selisih}")

teks = input("Masukkan teks: ")
print()
cari_tanggal(teks)
