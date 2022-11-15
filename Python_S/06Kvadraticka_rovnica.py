# Program na výpočet koreňov kvadratickej rovnice 
# Pomocou diskriminanta
import math 
print('ax\u00b2+bx+c=0')
a = int(input("Zadajte a: "))
b = int(input("Zadajte b: "))
c = int(input('Zadajte c: '))


d= b*b-(4*a*c)
print(d)
if d<0:
    print('Rovnica nemá riešenie')
elif d==0:
    x1=-b/2*a
    print('Rovnica má iba jedno riešenie a to je: ',round(x1,2))
else:
    x1=(-b+math.sqrt(d))/(2*a)
    x2=(-b-math.sqrt(d))/(2*a)
    print('Rovnica má dva korene: ',round(x1,2),' a ',round(x2,2))