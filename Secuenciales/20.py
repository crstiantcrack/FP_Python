import os
os.system("cls")

cantidad = int(input("Ingrese la cantidad de dinero en soles: "))

billetes200 = cantidad // 200
cantidad %= 200

billetes100 = cantidad // 100
cantidad %= 100

billetes50 = cantidad // 50
cantidad %= 50

billetes20 = cantidad // 20
cantidad %= 20

billetes10 = cantidad // 10
cantidad %= 10

moneda5 = cantidad // 5
cantidad %= 5

moneda2 = cantidad // 2
cantidad %= 2

moneda1 = cantidad

print("\n---Descomposición---")
print(f"Billetes de S/.200: {billetes200}")
print(f"Billetes de S/.100: {billetes100}")
print(f"Billetes de S/.50: {billetes50}")
print(f"Billetes de S/.20: {billetes20}")
print(f"Billetes de S/.10: {billetes10}")
print(f"Monedas de S/.5: {moneda5}")
print(f"Monedas de S/.2: {moneda2}")
print(f"Monedas de S/.1: {moneda1}")