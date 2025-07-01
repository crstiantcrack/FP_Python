a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))

d = b**2 - 4*a*c

x1 = (-b + d**0.5) / (2*a)
x2 = (-b - d**0.5) / (2*a)

print(f"x1 = {x1:.2f}")
print(f"x2 = {x2:.2f}")