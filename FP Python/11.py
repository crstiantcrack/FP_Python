num1 = input("Ingrese el primer número de 3 cifras: ")
num2 = input("Ingrese el segundo número de 3 cifras: ")

nuevo_num1 = num2[0] + num1[1] + num2[2]
nuevo_num2 = num1[0] + num2[1] + num1[2]

print("Resultados:")
print("Primer número transformado:", nuevo_num1)
print("Segundo número transformado:", nuevo_num2)