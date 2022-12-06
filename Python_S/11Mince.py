#Napíšte program na vyjadrenie zadanej sumy S eur v maximálnom počte postupne 500,200,100,50,20,10,5,2.1€
def rozklad(suma):
#500€
    patsto = suma // 500
    zvpatsto = suma % 500
#200€
    dvesto = zvpatsto // 200
    zvdvesto = zvpatsto % 200
#100€
    sto = zvdvesto // 100
    zvsto = zvdvesto % 100
#50€
    patdesiat = zvsto // 50
    zvpatdesiat = zvsto % 50  
#20€
    dvadsat = zvpatdesiat // 20
    zvdvadsat = zvpatdesiat % 20
#10€
    desat = zvdvadsat // 10
    zvdesat = zvdvadsat % 10
#5€
    pat = zvdesat // 5
    zvpat = zvdesat % 5
#2€
    dva = zvpat // 2
    zvdva = zvpat % 2
#1€
    jeden = zvdva // 1
#Výpis    
    print('Potrebujeme:',str(patsto)+'x500€ (zvyšok je: ',zvpatsto,')' )
    print('Potrebujeme:',str(patsto)+'x500€ (zvyšok je: ',zvpatsto,')' )
    print('            ',str(sto)+'x100€' )
    print('            ',str(patdesiat)+'x50€' )
    print('            ',str(dvadsat)+'x20€' )
    print('            ',str(desat)+'x10€' )
    print('            ',str(pat)+'x5€' )
    print('            ',str(dva)+'x2€' )
    print('            ',str(jeden)+'x1€' )

suma = int(input('Zadajte sumu v eurách: '))
d = rozklad(suma)
print(d)
input('Stlačte ENTER pre ukončenie')


