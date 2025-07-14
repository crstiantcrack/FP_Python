import math
import os
os.system("cls")

a = float(input("Ingrese el primer cateto: "))
b = float(input("Ingrese el segundo cateto: "))

hipotenusa = math.sqrt(a**2 + b**2)

print(f"La hipotenusa es: {hipotenusa:.2f}")