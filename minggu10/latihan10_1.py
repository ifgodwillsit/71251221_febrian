teksA = open("katanyaA.txt").readlines()
teksB = open("yangIniB.txt").readlines()
c = []
for i, (a, b) in enumerate(zip(teksA, teksB), start=1):
    if a != b:
        c.append(i)
        print(f"Baris {i}:")
        print(f"  [A] {a.strip()}")
        print(f"  [B] {b.strip()}")
if c != []:
    print(f"Jadi ada perbedaan di baris {c}")
else:
    print("Tidak ada perbedaan!")
