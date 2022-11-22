# Napíšte program na zistenie, či dané prirodzené číslo n je prvočíslom.
# Zabezpečte, aby bolo možné zadávať na testovanie iba prirodzené čísla
# väčšie ako 1.
# Ošetrite program tak, aby číslo 2 bolo správne otestované.
# Zabezpečte vypísanie informácie, či ide o prvočíslo alebo zložené číslo.


cislo = int(input('Zadajte číslo: '))
je_prvocislo = cislo > 1

for delitel in range(2,cislo):
    if cislo % delitel ==  0:
        je_prvocislo = False
        break
if je_prvocislo:
    print('Číslo', cislo,'je prvočíslo')
else:
    print('Číslo', cislo,'nie prvočíslo')
