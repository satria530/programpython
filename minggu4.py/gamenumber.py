angka_benar = 10
tebakan = 0

while tebakan != angka_benar:
    tebakan = int(input("pilih angka antara 1 dan 10:"))
    if tebakan < 1 or tebakan > 10:
        print("tebakan harus antaa 1 dan 10, coba lagi. ")
    elif tebakan == angka_benar:
        print("anda menang")
    else: 
        print("tebakan salah, coba lagi.")