def bubbleSort(premenna,premenna1):
    for i in range(len(premenna)-1):
        for j in range(0, len(premenna)-i-1):
            if premenna[j] > premenna[j + 1]:
                docasna_premenna = premenna[j]
                premenna[j] = premenna[j + 1] 
                premenna[j + 1] = docasna_premenna

                docasna_premenna1 = premenna1[j]
                premenna1[j] = premenna1[j + 1] 
                premenna1[j + 1] = docasna_premenna1
        

priezviska = []
vysky = []

pocetZiakov = int(input('Zadajte prosím počet žiakov: '))
for i in range(pocetZiakov):
    ziak = input(str(i+1)+'. Priezvisko: ')
    priezviska.append(ziak)
    vyska = input('  A výška (cm): ')
    vysky.append(vyska)

print('======================')
print('Neutriedené Priezviská:',priezviska)
bubbleSort(priezviska,vysky)
print('======================')
print("Utriedenie podľa priezviska:", priezviska)
print("                A ich výšky:", vysky)

bubbleSort(vysky,priezviska)
print('======================')
print("Utriedenie podľa výšky:", vysky)
print("      A ich priezviská:", priezviska)