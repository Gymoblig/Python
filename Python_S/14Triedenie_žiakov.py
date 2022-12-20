def bubbleSort(n):
    for i in range(len(n)-1):
        for j in range(0, len(n)-i-1):
            if cisla[j] > cisla[j + 1]:
                docasna_premenna = cisla[j]
                cisla[j] = cisla[j + 1] 
                cisla[j + 1] = docasna_premenna
        
 
#Input
cisla = []
pocetZiakov = int(input('Zadajte prosím počet žiakov: '))
for i in range(pocetZiakov):
    ziak = input(str(i+1)+'. Priezvisko: ')
    cisla.append(ziak)
print('======================')
print('Neutriedené Priezviská:',cisla)
bubbleSort(cisla)
print('======================')
print("Utriedené Priezviská:", cisla)