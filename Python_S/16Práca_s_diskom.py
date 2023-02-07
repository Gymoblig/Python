premenna = open("priezviska.txt", "w")
for i in range(3):
    priezvisko = str(input('Zadajte priezvisko: '))
    premenna.write(priezvisko+ '\n')
    
premenna.close()

arr = []
ar1 = []
pismeno = input('Zadajte začiatočné písmeno priezviska: ')

subor = open("priezviska.txt", "r")
riadok = subor.readline()

while riadok != '':
    arr.append(riadok.strip())
    riadok = subor.readline()
for j in range (len(arr)):
    if arr[j][0]==pismeno.lower() or arr[j][0]==pismeno.upper():
        ar1.append(arr[j])

print(ar1)
subor.close()
input()