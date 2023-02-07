import random
kocka = [1,2,3,4,5,6]
pocty = [0]*6
x = int(input('Koľkokrát chcete hodiť kockou? '))
for i in range(x):
    hod = random.randint(1,6)
    pocty[hod-1] += 1

print(kocka)
print(pocty)

for i in range(6):
    print(f'Číslo {kocka[i]} sme hodili {pocty[i]}x')
