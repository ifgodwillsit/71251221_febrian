import re
import random
import string

def generate_password(username, panjang = 8):
    karakter = string.ascii_letters + string.digits
    return "".join(random.choices(karakter, k = panjang))

def cari_email_buat_password(teks):
    pattern_email = r"\b[\w,+-]+@[\w-]+(?:\.[\w-]+\b)"
    list_email = re.findall(pattern_email, teks)

    if not list_email:
        print("Tidak ada email yang ditemukan dalam teks")
        return
    
    for email in list_email:
        username = email.split('@')[0]
        password = generate_password(username)

        print(f"{email} username: {username}, password: {password}")

teks = input("Masukkan teks: ")
print()
cari_email_buat_password(teks)
