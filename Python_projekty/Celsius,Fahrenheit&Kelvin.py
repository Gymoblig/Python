# A python script that converts Celsius to Fahrenheit or the opposite

#FAHRENHEIT
def from_fahrenheit_to_celsius(temperature): # definition for celsius conversion from fahrenheit
    celsius = (temperature-32)/1.8 
    print(str(temperature)+'°F =',str(celsius)+'°C')
def from_fahrenheit_to_kelvin(temperature): # definition for kelvin conversion from fahrenheit
    kelvin = (temperature+459.67)*(5/9) 
    print(str(temperature)+'°F =',str(round(kelvin,2))+'K')

#CELSIUS
def from_celsius_to_fahrenheit(temperature): # definition for fahrenheit conversion from celsius
    fahrenheit = temperature*1.8+32 
    print(str(temperature)+'°C =',str(fahrenheit)+'°F')
def from_celsius_to_kelvin(temperature): # definition for kelvin conversion from celsius
    kelvin = temperature+273.15 
    print(str(temperature)+'°C =',str(kelvin)+'K')

#KELVIN
def from_kelvin_to_celsius(temperature): # definition for celsius conversion from kelvin
    celsius = temperature-273.15 
    print(str(temperature)+'K =',str(celsius)+'°C')
def from_kelvin_to_fahrenheit(temperature): # definition for fahrenheit conversion from kelvin
    fahrenheit = (temperature/(5/9))-459.67 
    print(str(temperature)+'K =',str(round(fahrenheit,2))+'°F')

print('Celcius, Fahrenheit and Kelvin')
print('---------------------------------------------------------------')

temperature = float(input('What is the temperature?: ')) # Getting the value of the tempertaure
from_value = str(input('What is the unit of your temperature? (°C,°F or K): ')) # Getting the default temperature unit we want to convert
to_value = str(input('What is the desired unit? (°C,°F or K): '))

from_value = from_value.upper()
to_value = to_value.upper()


if from_value == 'C' and to_value == 'F':                            
    from_celsius_to_fahrenheit(temperature)
elif from_value =='C' and to_value == 'K':
    from_celsius_to_kelvin(temperature)

elif from_value == 'F' and to_value=='C':                       
    from_fahrenheit_to_celsius(temperature)
elif from_value == 'F' and to_value == 'K':
    from_fahrenheit_to_kelvin(temperature)

elif from_value == 'K' and to_value == 'C':
    from_kelvin_to_celsius(temperature)
elif from_value == 'K' and to_value == 'F':
    from_kelvin_to_fahrenheit(temperature)
else:
    print("You didn't provide valid units!")      # If we didn't provide valid unit then the program tells us that 
