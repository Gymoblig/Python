# Naprogramujeme hľadanie najväčšieho spoločného deliteľa dvoch čísel
# na vstupe zadáme dve celé čísla
# ochranou vstupu zabezpečte, aby sa nemohli zadať nuly
# odstráňte záporné znamienka v prípade zadania záporných čísel
# program vypočíta a vypíše ich najväčší spoločný deliteľ.
import math



a = int(input('Zadajte prvé číslo: '))
b = int(input('Zadajte druhé číslo: '))

d = math.gcd(a,b)
print('Najväčší spoločný deliteľ čísel',a,"a",b,'je číslo',d)