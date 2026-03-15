matkul = int(input("Berapa jumlah mata kuliah: "))
a = 1
ips = 0
while a <= matkul:
    grade = input(f"Nilai MK {a}: ")
    ip = 4 if grade == "A" else 3 if grade == "B" else 2 if grade == "C" else 1
    ips = ips + ip
    a += 1
ips = ips / matkul
print(f"Nilai IPS anda semester ini: {ips:.2f}")