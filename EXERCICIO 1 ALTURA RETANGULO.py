import math

base = float(input("A base do triangulo: "))
altura = float(input("A altura do triangulo: "))

area = base * altura
perimetro = 2 * (base + altura)
diagonal = math.sqrt(base * base)

print(f"AREA = {area:.4f}")
print(f"PERIMETRO = {perimetro:.4f}")
print(f"DIAGONAL = {diagonal:.4f}")