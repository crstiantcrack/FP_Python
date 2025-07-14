import math
import os
os.system("cls")

print("Ingrese los coeficientes:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

discriminante = b**2 - 4*a*c

raiz_cuadrada = math.sqrt(abs(discriminante))

x1 = (-b + raiz_cuadrada) / (2*a)
x2 = (-b - raiz_cuadrada) / (2*a)

print("\nResultados calculados:")
print(f"x₁ = {x1}")
print(f"x₂ = {x2}")
