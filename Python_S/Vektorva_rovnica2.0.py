print('VZOR:')
print('x= 1 + u + v')
print('y= 1 + u + v')
print('z= 1 + u + v')
print('---------------------------------------------------------------')
a1 = int(input('Zadajte x: '))
u1 = int(input('         : '))
v1 = int(input('         : '))
print('---------------------------------------------------------------')
a2 = int(input('Zadajte y: '))
u2 = int(input('         : '))
v2 = int(input('         : '))
print('---------------------------------------------------------------')
a3 = int(input('Zadajte z: '))
u3 = int(input('         : '))
v3 = int(input('         : '))
print('---------------------------------------------------------------')

#Vektor u
print('Vektor u = (',u1,';',u2,';',u3,')')
print('---------------------------------------------------------------')


#Vektor v
print('Vektor v = (',v1,';',v2,';',v3,')')
print('---------------------------------------------------------------')


#Vektor n
n1 = (u2*v3)-(v2*u3)
n2 = (u3*v1)-(v3*u1)
n3 = (u1*v2)-(v1*u2)
print('Vektor n (u × v) = (',n1,';',n2,';',n3,')')
print('---------------------------------------------------------------')


print('Vektorova rovnica: ax+by+cz+d=0')
print('Bod A = (',a1,';',a2,';',a3,')')
print(a1,'*',n1,'+',a2,'*',n2,'+',a3,'*',n3,'+ d = 0')
d = -((a1*n1)+(a2*n2)+(a3*n3))
print('d =',d)
print('---------------------------------------------------------------')

print('Rovnica je:',str(n1)+'x +',str(n2)+'y +',str(n3)+'z + ',d,' = 0')
input('Stlačte ENTER pre ukončenie')