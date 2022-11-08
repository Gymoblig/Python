# Napíšte program na súčin čísel od 1 do 10
# Faktorial zadaného prirodzeného čísla
f= 1
for i in range(1,10):
    f = f*i
print('1.2.3.4.5.6.7.8.9.10= ',f)



cislo = 0

while cislo <= 0:
    cislo = int(input('Číslo, ktoré potrebujeme dať na faktoriál: '))
    fact = 1

for i in range(1,cislo+1):
    fact = fact * i

print(str(cislo)+'! = ', fact)