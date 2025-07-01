horas = float(input("Ingrese el número de horas trabajadas: "))
tarifa = float(input("Ingrese la tarifa por hora: "))

sueldo_basico = horas * tarifa
sueldo_bruto = sueldo_basico + sueldo_basico * 0.20
sueldo_neto = sueldo_bruto - sueldo_bruto * 0.10

print(f"Sueldo básico: {sueldo_basico:.2f}")
print(f"Sueldo bruto: {sueldo_bruto:.2f}")
print(f"Sueldo neto: {sueldo_neto:.2f}")