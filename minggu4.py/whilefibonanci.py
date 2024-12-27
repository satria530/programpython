max_angka = int(input("masukkan angka maximum untuk deret fibonanci"))
a, b = 0, 1

print("deret fibonanci:")
while a <= max_angka:
    print(a, end=" ")
    a, b = b, a + b