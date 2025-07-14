import os
os.system("cls")

numero = int(input("Ingrese 4 numeros: "))

unidad = numero % 10
decena = numero // 10 % 10
centena = numero // 100 % 10
millar = numero // 1000

suma = unidad + decena + centena + millar

print(suma)