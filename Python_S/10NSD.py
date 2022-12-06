# Naprogramujeme hľadanie najväčšieho spoločného deliteľa dvoch čísel
# na vstupe zadáme dve celé čísla
# ochranou vstupu zabezpečte, aby sa nemohli zadať nuly
# odstráňte záporné znamienka v prípade zadania záporných čísel
# program vypočíta a vypíše ich najväčší spoločný deliteľ.
def delitel(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a




a = int(input('Zadajte prvé číslo: '))
b = int(input('Zadajte druhé číslo: '))

d = delitel(a,b)
print('Najväčší spoločný deliteľ čísel',a,"a",b,'je číslo',d)