# Výpočet základných matematických operácií
# Medzi dvoma zadanými celými číslami

cislo1 = int(input('Zadaj 1. číslo: '))
cislo2 = int(input('Zadaj 2. číslo: '))
operacia = input('Akú operáciu mam s týmito číslami? + - * / ')

if operacia == '+':
    vysledok = cislo1 + cislo2
elif operacia == '-':
    vysledok = cislo1 - cislo2
elif operacia == '*':
    vysledok = cislo1 * cislo2
elif operacia == '/':
    vysledok = cislo1 / cislo2
else:
    vysledok = 'Toto neviem vypočítať'

print( 'Výsledok čísel ',cislo1,' a ',cislo2,' je ', vysledok)