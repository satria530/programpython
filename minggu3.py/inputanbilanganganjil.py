number = int(input('masukkan pengulangan anda'))

for x in range(1 , number + 1): # kalau tidak ada +1 tidak sampai nomer yang kita ketik
    if x % 2 !=0:
        print('bilangan ganjil', x)
    else:
        print('bilangan genap', x)
        
    
    #menentukan bilangan ganjil,genap