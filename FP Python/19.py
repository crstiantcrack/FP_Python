v_total = int(input("ingresa el monto vendido: "))
sueldo_basico = 500

comision = v_total * 0.09

sueldo_bruto = sueldo_basico + comision

descuento = sueldo_bruto * 0.11

sueldo_neto = sueldo_bruto - descuento

print(f"Comision: S/.{comision:.2f} ")
print(f"Sueldo bruto: S/.{sueldo_bruto:.2f}")
print(f"Descuento: S/.{descuento:.2f}")
print(f"Sueldo neto: S/.{sueldo_neto:.2f}")

 
