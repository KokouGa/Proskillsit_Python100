temperature = input("Entrez la température en C ou F: ")
unit = temperature[-1].upper()
if unit not in ['C', 'F']:
    print("Unité invalide. Veuillez entrer une température se terminant par 'C' ou 'F'.")
else:
    if temperature[-1].upper() == "C":
        celsius = float(temperature[:-1])
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C est égal à {fahrenheit}°F")
    elif temperature[-1].upper() == "F":
        fahrenheit = float(temperature[:-1])
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F est égal à {celsius}°C")