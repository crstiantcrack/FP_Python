import os
os.system("cls")

pies = int(input("Ingresa la cantidad de pies: "))
pulgadas = int(input("Ingresa la cantidad de pulgadas: "))

estatura_metros = (pies * 0.3048) + (pulgadas * 0.0254)


print(f"La estatura en metros es: {estatura_metros:.2f} m")