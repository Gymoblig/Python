# Program na výpočet koreňov kvadratickej rovnice 
# Pomocou diskriminanta
import math 
print('ax^2+bx+c=0')
a = int(input("Zadajte a: "))
b = int(input("Zadajte b: "))
c = int(input('Zadajte c: '))


d= b*b-(4*a*c)

if a==0:
    print('a je 0!')
    print('Rovnica vyzerá následovne: bx+c=0')
    x= -c/b
    print('Výsledok takejto lineárnej rovnice je: ',round(x,2))
elif d<0:
    print('Diskriminant je: ',d)
    print('Rovnica nemá riešenie')
elif d==0:
    x1=-b/2*a
    print('Diskriminant je: ',d)
    print('Rovnica má iba jedno riešenie a to je: ',round(x1,2))
else:
    x1=(-b+math.sqrt(d))/(2*a)
    x2=(-b-math.sqrt(d))/(2*a)
    print('Diskriminant je: ',d)
    print('Rovnica má dva korene: ',round(x1,2),' a ',round(x2,2))