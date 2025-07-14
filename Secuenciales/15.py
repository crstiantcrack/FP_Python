import os
os.system("cls")

juan = float(input("Ingrese el aporte de Juan en dólares: "))
rosa = float(input("Ingrese el aporte de Rosa en dólares: "))
daniel_soles = float(input("Ingrese el aporte de Daniel en soles: "))

daniel = daniel_soles / 3

capital_total = juan + rosa + daniel

porcentaje_juan = (juan / capital_total) * 100
porcentaje_rosa = (rosa / capital_total) * 100
porcentaje_daniel = (daniel / capital_total) * 100

print(f"Capital total en dólares: {capital_total:.2f}")
print(f"Porcentaje de Juan: {porcentaje_juan:.2f}%")
print(f"Porcentaje de Rosa: {porcentaje_rosa:.2f}%")
print(f"Porcentaje de Daniel: {porcentaje_daniel:.2f}%")