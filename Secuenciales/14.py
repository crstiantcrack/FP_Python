import os
os.system("cls")

print("Ingrese 5 números:")
num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))
num3 = float(input("Número 3: "))
num4 = float(input("Número 4: "))
num5 = float(input("Número 5: "))


numeros = [num1, num2, num3, num4, num5]


numeros.sort(reverse=True)


tres_mayores = numeros[0:3]


promedio = sum(tres_mayores) / 3

print(f"\nLos tres números mayores son: {tres_mayores}")
print(f"El promedio de estos tres números es: {promedio:.2f}")