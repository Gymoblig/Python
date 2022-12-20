# Napíšte program na zistenie, či dané prirodzené číslo n je prvočíslom.
# Zabezpečte, aby bolo možné zadávať na testovanie iba prirodzené čísla
# väčšie ako 1.
# Ošetrite program tak, aby číslo 2 bolo správne otestované.
# Zabezpečte vypísanie informácie, či ide o prvočíslo alebo zložené číslo.

def je_prvocislo(x):
    je= x > 1

    for delitel in range(2,x):
        if x % delitel ==  0:
            je= False
            break
    return je


cislo = int(input('Zadajte číslo: '))
if je_prvocislo(cislo):
    print('Číslo', cislo,'je prvočíslo')
else:
    print('Číslo', cislo,'nie je prvočíslo')
