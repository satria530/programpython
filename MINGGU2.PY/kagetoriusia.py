usia = int(input("masukkan usia anda: "))
if usia < 13:
    print("anda adalah anak anak.")
elif 13 <= usia <= 19: 
    print("anda adalah remaja.")
elif 20 <= usia <= 59:
    print("anda adalah dewasa.")
else :
    print("anda adalah lansia.")
    