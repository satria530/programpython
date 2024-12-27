usia = int(input("masukkan usia anda: "))
if usia < 12: 
    harga = 30000
elif 12 <= usia <= 59: 
    harga = 50000 
else :
    harga = 25000

print (f"{usia} anda, harga tiket {harga}")
