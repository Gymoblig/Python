# Auto sa pohybuje rýchlosťou 60km/h
#---------------------------------------------------------------
# 1. Vypočítajte, za koľko sekúmd prejde rovnomerným pohybom
#    z mesta A do mesta B, ak táto vzialensť je v metroch
#---------------------------------------------------------------
# 2. Vypočítajte, koľko ml benzínu spotrebuje auto...
#    ak jeho priemerná spotreba je 7,2l/100km
#---------------------------------------------------------------


rychlost = 60 #int(input('Zadajte rýchlosť (km/h): '))
spotreba = 0.072 #int(input('Zadajte spotrebu (l/100km): '))
vzdialenost = int(input('Zadajte vzdialenosť (m): '))

rychlost2 = rychlost/3.6
cas= vzdialenost/rychlost2
#spotreba2= spotreba/1000 --> toto je v prípade, že spotrebu zadávame tiež
nadrz = vzdialenost*spotreba #spotreba2


print('Auto prejde vzialenosť ',vzdialenost,' metrov za ',int(cas),'s a minie ',int(nadrz),'ml paliva za tento čas')