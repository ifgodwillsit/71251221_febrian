def tiga_terbaik(data):
    data.sort()
    data.reverse()
    return data[:3]

angka = list(map(int, input().split()))
print("3 bilangan terbaik:", tiga_terbaik(angka))