# Se citesc numere de la tastatură până la introducerea unui număr impar divizibil cu 3. 
# Să se afişeze suma tuturor numerelor pare introduse.  
# Exemplu: Date de intrare  7  4   6   2   1   9   Date de ieşire 12.  
n = 0
suma = 0
while (n % 2 == 0) or (n % 3 != 0):
    n = eval(input("n ="))
    if n % 2 == 0:
         suma += n
print("Suma =", suma) 