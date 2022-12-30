# Program na zistenie MAC adresy počítača a následného zisťovania počtu znakov
from getmac import get_mac_address as gma #najskôr pridáme balík, ktorý nám uľahčí postup (pri prvom použití treba cez terminál zadať pip install get-mac)
adresa = gma()
print('MAC adresa tohoto počítača je:',adresa.upper()) #upper je tam preto aby mac adresa bola napísaná veľkým písmom

znak = str(input('Zadajte znak, ktorý chcete nájsť v MAC adrese: ')) # Získame znak, ktorý chceme nájsť


if znak in adresa:
    pocet = adresa.count(znak) # použitím count() si môžeme uľahčiť postup a je to v podstate jediné čo nám stačí urobiť
    print('V adrese MAC sa znak nachádza',str(pocet)+'x') # Ak sa znak nachádza v adrese dostaneme odpoveď s množstovm 
else:
    print('Znak sa nenachádza v MAC adrese') # Ak sa znak nenachádza v adrese dostaneme na to odpoveď
