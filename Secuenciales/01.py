import os
os.system("cls")

sum1 = int(input("el numero a sumar es: "))
sum2 = int(input("el numero a sumar es: "))

total = sum1 + sum2

varones = (sum1 / total) * 100
mujeres = (sum2 / total) * 100

print(f"el porcentaje de hombres es: {varones:.2f}%")
print(f"el porcentaje de mujeres es {mujeres:.2f}%")