nama_hewan_benar = 'kucing'
tebakan = ''
attempts = 3  

print("Selamat datang di permainan tebak nama hewan!")
print("Coba tebak nama hewan yang saya pikirkan.")

while tebakan != nama_hewan_benar and attempts > 0:
    tebakan = input("Masukkan tebakan Anda: ")
    
    if tebakan == nama_hewan_benar:
        print("Selamat! Anda berhasil menebak nama hewan.")
    else:
        attempts -= 1
        print(f"Salah! Anda masih memiliki {attempts} percobaan tersisa.")
        if attempts == 0:
            print(f"Permainan selesai! Nama hewan yang benar adalah '{nama_hewan_benar}'.")
