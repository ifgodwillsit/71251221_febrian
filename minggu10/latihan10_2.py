nama_file = "soal.txt"
print(f"nama file: {nama_file}\n")
 
for baris in open(nama_file).readlines():
    soal, jawaban_benar = baris.strip().split(" || ")
    print(soal)
    jawaban = input("Jawab: ")
    if jawaban.lower() == jawaban_benar.lower():
        print("Jawaban benar!")
    else:
        print("Jawaban salah!")
        