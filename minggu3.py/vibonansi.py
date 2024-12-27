fibonanci = int(input("masukkan bilangan fibonanci : "))

a, b = 1 , 1
print("fibonansi : ", end = "")
for i in range(fibonanci):
    print(a, end = ' ')
    a, b = b, a + b
    #fibonansi (pengulangan penambahan)