cantidad = int(input("ingrese la cantidad de objetos"))

precio = float(input("ingrese el precio del articulo"))

total = cantidad * precio
descuento1 = total * 0.15
importe = total - descuento1
descuento2 = importe * 0.15
descuento_total = descuento1 + descuento2
importe_final = total - descuento_total

print("\n--- RESULTADOS ---")
print(f"Importe de la compra: S/. {total:.2f}")
print(f"Descuento total: S/. {descuento_total:.2f}")
print(f"Importe a pagar: S/. {importe_final:.2f}")