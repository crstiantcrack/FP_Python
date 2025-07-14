import os
os.system("cls")

donacion = float(input("Ingrese la donación anual: "))

centro_salud = donacion * 0.25
comedor_infantil = donacion * 0.35
escuela_infantil = donacion * 0.25
asilo_ancianos = donacion - (centro_salud + comedor_infantil + escuela_infantil)

print(f"Centro de salud: S/. {centro_salud:.2f}")
print(f"Comedor infantil: S/. {comedor_infantil:.2f}")
print(f"Escuela infantil: S/. {escuela_infantil:.2f}")
print(f"Asilo de ancianos: S/. {asilo_ancianos:.2f}")