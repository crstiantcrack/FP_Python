import os
os.system("cls")

num1 = int(input("Introduce el primer número de 3 cifras: "))
num2 = int(input("Introduce el segundo número de 3 cifras: "))


u1 = num1 // 100
d2 = (num1 // 10) % 10
c3 = num1 % 10


un1 = num2 // 100
de2 = (num2 // 10) % 10
ce3 = num2 % 10

nuevo_numero = ce3 * 100 + d2 * 10 + un1
nuevo_numero = c3 * 100 + de2 * 10 + u1

print(f"Numeros a intercambiar Cifras: {num1} y {num2}")
print(f"Cifras Intercambiadas: {nuevo_numero} → {nuevo_numero}")
