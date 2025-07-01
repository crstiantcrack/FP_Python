num1 = float(input("el numero a convertir a es: "))

cm = num1 * 100
pulg = cm / 2.54
pies = pulg / 12
yarda = pies / 3

print(f"{num1} metros equivale a:")
print(f"centimetros {cm:}")
print(f"pulgadas {pulg:.2f}")
print(f"pies {pies:.2f}")
print(f"yardas {yarda:.2f}")
