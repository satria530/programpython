#list angka 
angka = [1,2,3,4,5]

#menggunakan list comprehensif untuk membuat list baru dengan kuarad dari variable angka
kuarad = [i**2 for i in angka]

kubik = [x**3 for x in angka]


print("kuarad dari anga : ", kuarad)  # [1, 4, 9, 16,25]
print("kubik dari angka : ", kubik)  # [1,8,9,64,125]