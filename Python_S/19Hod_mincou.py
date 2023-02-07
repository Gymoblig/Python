import random
arr = []
orol = 0
panna =0
for i in range(100):
    cislo = random.randint(0,1)
    if cislo == 0:
        orol = orol + 1
        arr.append('Orol')
    else:
        panna = panna + 1
        arr.append('Panna')
print(arr)
print(f'Panna padla {panna}x a Orol padol {orol}x')