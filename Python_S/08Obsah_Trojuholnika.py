# Napíšte program na výpočet obsahu trojuholníka so základňou z, výškou v.
# Doplňte ho prehľadným spôsobom o testovanie, či je obsah zo zadaného intervalu (D,H).
def test():
    if a<S<b:
        print('Zadaný obsah ',S,' je v intervale <',a,',',b,'>')
    else:
        print('Zadaný obsah ',S,' nie je v intervale <',a,',',b,'>')

print('Obsah Trojuholníka')
print('---------------------------------------------------------------')
z = float(input('Zadajte základňu (\x1B[3m v CM \x1B[0m): '))
v = float(input('Zadajte výšku na základňu (\x1B[3m v CM \x1B[0m): '))

S=(z*v)/2
print('Obsah trojuholníka je:',str(S),"cm\u00b2")

a = float(input('Je zadaný obsah v intervale od:'))
b = float(input('                            do:'))
test()

