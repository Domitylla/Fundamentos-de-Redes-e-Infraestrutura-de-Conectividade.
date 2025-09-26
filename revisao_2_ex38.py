# revisao_2_ex38.py
import math
while True:
    v = float(input("Digite um valor (0 ou negativo para sair): "))
    if v <= 0:
        break
    print(f"Quadrado: {v**2}")
    print(f"Cubo: {v**3}")
    print(f"Raiz quadrada: {math.sqrt(v):.2f}")
