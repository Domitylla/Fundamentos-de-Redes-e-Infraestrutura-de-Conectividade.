# revisao_1_ex38.py
import math

a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

if a == 0:
    print("Não é equação de segundo grau.")
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Não existe raiz.")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"Raiz única: {x}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Duas raízes reais: {x1:.2f} e {x2:.2f}")
