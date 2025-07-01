numero = []
print("ingresa 5 Numeros")
for i in range(5):
 hola = int(input(f"NOTA: {i +1} "))
 numero.append(hola)
 
numero.sort(reverse=True)
mayores = numero[:3]
promedio = sum(mayores) / 3
  
print("Los 3 números mayores son:", mayores)
print(f"El promedio de los 3 mayores es: ", int(promedio))