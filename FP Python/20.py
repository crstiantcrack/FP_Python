num = int(input("Ingresa un número: "))

billetes = [200, 100, 50, 20, 10, 5, 2, 1]

print("DESCOMPOSICIÓN DE BILLETES Y MONEDAS")
for valor in billetes:
    cantidad = num // valor
    if cantidad > 0:
        tipo = "billetes" if valor >= 10 else "monedas"
        print(f"{cantidad} {tipo} de S/. {valor}")
        num = num % valor