total_pembelian = float(input("masukkan total_pembelian"))
if total_pembelian >= 1000000: 
    diskon = 0.20
elif total_pembelian >= 500000:
    diskon = 0.10
else :
    diskon = 0

potongan_harga = total_pembelian * diskon 
total_harga = total_pembelian - potongan_harga 
print(f"total_pembelian: {total_pembelian}")
print(f"diskon{potongan_harga} ({diskon * 100}%)")
print(f"total yang harus di bayar: {total_harga}")