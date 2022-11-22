# Pomocou programu zistite, či 3 zadané prirodzené čísla môžu byť stranami trojuholníka. 
# Ak áno, doplňte program o test, či ide o pravouhlý trojuholník.

print('Trojuholník ABC')
print('---------------------------------------------------------------')
a = int(input('Zadajte stranu a: '))
b = int(input('Zadajte stranu b: '))
c = int(input('Zadajte stranu c: '))

if a+b>c and a+c>b and b+c>a:
    print('Tieto strany môžu tvoriť trojuholník :-)')
    pravo = str(input('Chcete otestovať či je to pravouhlý trojuholník? y/n: '))
    if pravo=='y':
        lava = c*c
        prava = a*a+b*b
        if lava==prava:
            print(c,'*',c,'=',a,'*',a,'+',b,'*',b,str(u'\u2713')) #str(u'\u2713') --> je to fajočka
            print('Toto je pravouhlý trojuholník')
            input('Stlačte ENTER pre ukončenie')
        else:
            print(c,'*',c,'=',a,'*',a,'+',b,'*',b)
            print('Toto nie je pravouhlý trojuholník')
    else:
        input('Stlačte ENTER pre ukončenie')
else:
    print('Tieto strany nemôžu tvoriť trojuholník')
    input('Stlačte ENTER pre ukončenie')