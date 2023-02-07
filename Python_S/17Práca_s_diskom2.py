premenna = open("priezviska.txt", "r")
arr = []

riadok = premenna.readline()
pocet = 0
while riadok != '':
    pocet = pocet + 1
    arr.append(riadok.strip())
    riadok = premenna.readline()
premenna.close()

nenachadza = False
print("Všetky mená sú: ",arr)

meno = input('Zadajte začiatočné písmeno priezviska, ktoré chcete nájsť: ')
for i in range(len(arr)):
    if meno == arr[i]:
        print(f'Hľadané meno {meno} sa nachádza v zozname.')
        nenachadza = False
        break
    else:
        nenachadza= True
if nenachadza:
    print(f'Hľadané meno {meno} sa bohužiaľ nenachádza v zozname.')
