
def pocitanie(list):
    pocet = 0
    for meno in list:
        pocet += 1
    return pocet
def procedura():
    arr = []
    ar1 = []
    pismeno = input('Zadajte prosím začiatočné písmeno priezviska: ')

    subor = open("mena.txt", "r")
    riadok = subor.readline()

    while riadok != '':
        arr.append(riadok.strip())
        riadok = subor.readline()
    for j in range (len(arr)):
        if arr[j][0]==pismeno.lower() or arr[j][0]==pismeno.upper():
            ar1.append(arr[j])
    pocitanie(ar1)
    print("V zozname je priezvisko so začinajúcím písmenom ",str(pocitanie(ar1))+"x ->",ar1)
    subor.close()



    otazka = input('Chcete vyhľadávať znova? A/N ').lower()
    if otazka == 'a':
        procedura()
    else:
        input('Stlačte ENTER pre ukončenie')




procedura()
