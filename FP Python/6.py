import math

r = float(input("Ingrese el radio del cilindro: "))
h = float(input("Ingrese la altura del cilindro: "))

area_total = 2 * math.pi * r * (r + h)
volumen = math.pi * r**2 * h

print(f"Área total = {area_total:.2f}")
print(f"Volumen = {volumen:.2f}")