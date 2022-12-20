#def bubbleSort(cisla):
    #n = len(cisla)
    #vymena = False
    #for i in range(n-1):
        #for j in range(0, n-i-1):
            #if cisla[j] > cisla[j + 1]:
                #vymena = True
                #cisla[j], cisla[j + 1] = cisla[j + 1], cisla[j]
        #if not vymena:
            #return
def bubbleSort(n):
    for i in range(len(n)-1):
        for j in range(0, len(n)-i-1):
            if cisla[j] > cisla[j + 1]:
                docasna_premenna = cisla[j]
                cisla[j] = cisla[j + 1] 
                cisla[j + 1] = docasna_premenna
        return n
 
#Input
cisla = []
pocetRezistorov = int(input('Zadajte prosím počet rezistorov: '))
for i in range(pocetRezistorov):
    rezistor = int(input(str(i+1)+'. Rezistor: '))
    cisla.append(rezistor)
print('======================')
print('Neutriedené rezistory:',cisla)
bubbleSort(cisla)
print('======================')
print("Utriedené rezistory:", cisla)
