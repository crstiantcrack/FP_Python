km, pies, millas = float(input("km: ")), float(input("pies: ")), float(input("millas: "))
m = km*1000 + pies/3.2808 + millas*1609
print(f"\nTotal: {m:.2f} metros = {m*1.0936:.2f} yardas")