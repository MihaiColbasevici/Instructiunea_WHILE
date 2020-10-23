nl = 1
tot_poz = 0
tot_neg = 0
nr_poz = 0
nr_neg = 0
while (nl > 0) and (nl <= 12):
    t = int(input("Dati temperatura medie: "))
    if (t > 0):
        t_poz = t
        nr_poz = nr_poz + 1
        tot_poz = tot_poz + t_poz
    elif (t < 0):
        t_neg = t
        nr_neg = nr_neg + 1
        tot_neg = tot_neg + t_neg
    nl = nl + 1
if (nr_neg == 0):
    media_poz = tot_poz / nr_poz
    print(round(media_poz, 2))
elif (nr_poz == 0):
    media_neg = tot_neg / nr_neg
    print(round(media_neg, 2))
else:
    media_poz = tot_poz / nr_poz
    media_neg = tot_neg / nr_neg
    print(round(media_poz, 2))
    print(round(media_neg, 2))