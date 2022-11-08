# Napíšte program na výpočet N-tej mocniny zo zadaného kladného čísla A.
# Správne nastavte zadávanie vstupného čísla (základ mocniny) pre kladné 
# číslo prostredníctvom ochrany vstupu.
# Vypočítajte N-tú mocninu z daného kladného čísla pre prípad kladného 
# exponenta.
# Doplňte program tak, aby dokázal vypočítať N-tú mocninu z daného 
# kladného čísla aj pre prípad záporného exponenta. 

a = float(input('Zadajte mocnenec: '))
n = int(input('Zadajte exponent: '))

if a <=0:                   #Upozorní na to, že je mocnenec záporný
    print('Číslo je záporné! Zmením ho na kladné')

vysledok = abs(a) ** n      #Vypočíta a všetky podmienky sú obsiahnuté

print(str(n)+'. mocnina čísla ',str(abs(a)),'je',round(vysledok, 2))