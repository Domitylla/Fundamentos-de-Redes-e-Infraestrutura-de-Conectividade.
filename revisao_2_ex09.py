# revisao_2_ex09.py
menor = float('inf')
maior = float('-inf')
for _ in range(10):
    n = float(input("Digite um número: "))
    if n < menor:
        menor = n
    if n > maior:
        maior = n
print("Menor valor:", menor)
print("Maior valor:", maior)
