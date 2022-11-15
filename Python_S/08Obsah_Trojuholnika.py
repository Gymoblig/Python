# Napíšte program na výpočet obsahu trojuholníka so základňou z, výškou v.
# Doplňte ho prehľadným spôsobom o testovanie, či je obsah zo zadaného intervalu (D,H).

print('Obsah Trojuholníka')
print('---------------------------------------------------------------')
z = float(input('Zadajte základňu (\x1B[3m v CM \x1B[0m): '))
v = float(input('Zadajte výšku na základňu (\x1B[3m v CM \x1B[0m): '))

S=(z*v)/2
print('Obsah trojuholníka je:',S+"cm\u00b2")