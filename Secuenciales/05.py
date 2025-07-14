import os
os.system("cls")

gb = int(input("Ingresa la cantidad de memoria del disco duro: "))

MB = gb * 1024
KB = MB * 1024
B = KB * 1024

print(f"la cantidad de memoria del disco duro es: {gb} GB ")
print(f"En Megabytes es: {MB} mb")
print(f"En Kylobytes es: {KB} kb")
print(f"En Bytes es: {B} b")