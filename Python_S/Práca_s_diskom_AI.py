# Funkcia na načítanie priezvisk zo súboru
def load_surnames(file_name):
  with open(file_name, 'r') as file:
    return [line.strip() for line in file]

# Funkcia na výpočet počtu priezvisk, ktoré začínajú na zvolené písmeno a výpis priezvisk
def count_surnames(surnames, letter):
  count = 0
  print("Priezviska, ktore zacinaju na", letter, "su:")
  for surname in surnames:
    if surname[0].upper() == letter.upper():
      count += 1
      print("-", surname)
  print("Pocet priezvisk, ktore zacinaju na", letter, "je", count)

# Načítanie priezvisk zo súboru
surnames = load_surnames('priezviska.txt')

# Vstup od používateľa na zadanie písmena
letter = input("Zadajte písmeno: ")

# Výpočet počtu priezvisk a výpis priezvisk
count_surnames(surnames, letter)

# Otázka na opakovanie procedúry
answer = input("Chcete pokracovat? (ano/nie) ")
if answer.lower() == 'a':
  letter = input("Zadajte ďalšie písmeno: ")
  count_surnames(surnames, letter)
else:
  print("Koniec programu")