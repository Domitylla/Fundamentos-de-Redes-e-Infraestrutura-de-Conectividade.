# revisao_2_ex27.py
maior = float('-inf')
menor = float('inf')
while True:
    n = int(input("Digite um número (negativo para sair): "))
    if n < 0:
        break
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print("Maior:", maior)
print("Menor:", menor)
