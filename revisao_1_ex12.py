# revisao_1_ex12.py
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
if a == b:
    print("Números iguais.")
else:
    maior = max(a, b)
    menor = min(a, b)
    print("Maior número:", maior)
    print("Diferença:", maior - menor)
