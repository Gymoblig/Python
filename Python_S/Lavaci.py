import random
l=0
for i in range(0,1000):
    m = random.random()
    z = random.random()
    if m<0.04 and z<0.05:
        l=l+1
print(l)
