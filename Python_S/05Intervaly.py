# Napíšte program, ktorým zistite:
#   či prienikom zadaných intervalov je prázdna množina
#   ak to nie je prázdna množina, či je prienikom jeden bod alebo interval


a,b,c,d = input("Zadajte intervaly (\x1B[3m a,b,c,d \x1B[0m): ").split()
if a>b:
    p=a
    a=b
    b=p
if c>d:
    p=c
    c=d
    d=p
if a>c:
    p=a
    a=c
    c=p
    p=b
    b=d
    d=p
if b<c:
    print("Nemajú prienik")
elif b==c:
    print("Prienikom je bod ",b,"-")
elif d<b:
    print("Prienik je interval <"+str(c)+",",str(d),">")
else:
    print("Prienik je interval <"+str(c)+",",str(b)+">")