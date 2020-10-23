n = int(input("n = "))
i = 1
suma = 0
produs = 1
nr_n = 0                          # nr este variabila care va numara cate numere sunt introduse
while i <= n:
    num = int(input("num = "))
    suma = suma + num
    produs = produs * num
    nr_n = nr_n + 1
    i = i + 1
media_ar = suma / nr_n
print("Suma numerelor =", suma)
print("Produsul numerelor =", produs)
print("Media aritmetica a numerelor =", media_ar)