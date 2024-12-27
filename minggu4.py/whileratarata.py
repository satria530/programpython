total = 0
jumlah_angka = 0

while True:
    angka = float(input("Masukkan angka positif (atau angka negatif untuk berhenti): "))
    if angka < 0:
        break  # Keluar dari loop jika angka negatif
    total += angka  # Menambahkan angka ke total
    jumlah_angka += 1  # Menambahkan jumlah angka

if jumlah_angka > 0:
    rata_rata = total / jumlah_angka
    print("Rata-rata dari angka yang dimasukkan adalah:", rata_rata)
else:
    print("Tidak ada angka yang dimasukkan.")