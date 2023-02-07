
rok = 0
x = int(input('Koľko je ročný úrok? '))
ciastka = int(input('Zadajte čiastku:'))
x = (x/100)+1
suma = 0
for i in range(10):
    
    suma = (suma*x)+500
    print(suma)
suma = 0
while suma <=ciastka:
    suma = (suma*x)+500
    rok = rok+1
print(f'Úspory prekročia čiastku {ciastka}€ za {rok} rokov')
    


