total = 0
while True:
    angka = int(input("Masukkan angka positif (atau angka negatif untuk berhenti): "))
    if angka < 0:
        break  # Keluar dari loop jika angka negatif
    total += angka  # Menambahkan angka ke total
print("Jumlah total:", total)