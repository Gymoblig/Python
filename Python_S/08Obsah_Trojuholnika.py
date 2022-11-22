# Napíšte program na výpočet obsahu trojuholníka so základňou z, výškou v.
# Doplňte ho prehľadným spôsobom o testovanie, či je obsah zo zadaného intervalu (D,H).
def funkcia():
    if a<S<b:
        slovo = str('')
    else:
        slovo = str('nie')
    print('Zadaný obsah ',S, str(slovo)+' je v intervale <',a,',',b,'>')

print('Obsah Trojuholníka')
print('---------------------------------------------------------------')
z = float(input('Zadajte základňu (\x1B[3m v CM \x1B[0m): '))
v = float(input('Zadajte výšku na základňu (\x1B[3m v CM \x1B[0m): '))

S=(z*v)/2
print('Obsah trojuholníka je:',str(S),"cm\u00b2")

a = float(input('Je zadaný obsah v intervale od:'))
b = float(input('                            do:'))
funkcia()

