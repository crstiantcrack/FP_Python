import os
os.system("cls")

numero = int(input("Numeros a invertir (4): "))

unidad = numero % 10
decena = numero // 10 % 10
centena = numero // 100 % 10
millar = numero // 1000

numero_invertido = unidad*1000 + decena*100 + centena*10 + millar

print(numero_invertido)