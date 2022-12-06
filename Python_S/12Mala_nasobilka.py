#Malá násobilka no
import random

def pocitanie():
    c= random.randint(0,10)
    c1= random.randint(0,10)
    x=c*c1
    print(c,'*',c1,'= ? ')
    vysledok = int(input())
    if vysledok == x:
        print('Výsledok je správny')
    elif vysledok != x:
        print('Výsledok je nesprávny')

    otazka = input('Ďalší príklad? A/N: ').lower()
    if otazka == 'a':
        procedura = pocitanie()
        print(procedura)
    else:
        input('Stlačte ENTER pre ukončenie')


a = int(input('Zadajte dve čísla: '))
b = int(input('                   '))
print(a,'*',b,'= ? ')
d=a*b
vysledok = int(input())
if vysledok == d:
    print('Výsledok je správny')
else:
    print('Výsledok je nesprávny')
        
otazka = input('Ďalší príklad? A/N: ').lower()
if otazka == 'a':
    procedura = pocitanie()
    print(procedura)
else:
    input('Stlačte ENTER pre ukončenie')
