def perkalian (a, b):
    print(f"{a} x {b} =", end = " ")
    i = 1
    for i in range(a):
        if i == a - 1:
            print(str(b) + " = ", end = "")
        else:
            print(str(b) + " + ", end = "")
    print(str(a * b))

print("Perkalian")
a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
perkalian(a, b)
