import os
os.system("cls")

kilometros = float(input("Longitud del primer tramo (KILOMETROS): "))
pies = float(input("Longitud del segundo tramo (PIES): "))
millas = float(input("Longitud del tercer tramo (MILLAS): "))

PRIMER_TRAMO = kilometros * 1000
SEGUNDO_TRAMO = pies / 3.2808
TERCER_TRAMO = millas * 1609

TOTAL_METROS = PRIMER_TRAMO + SEGUNDO_TRAMO + TERCER_TRAMO
TOTAL_YARDAS = (TOTAL_METROS*3.2808) / 3

print(f"Longitud total en metros: {TOTAL_METROS:.2f} Metros")
print(f"Longitud total en yardas: {TOTAL_YARDAS:.2f} Yardas")