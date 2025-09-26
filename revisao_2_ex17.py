# revisao_2_ex17.py
quantidade = int(input("Quantidade de números a ler: "))
maior = float('-inf')
for _ in range(quantidade):
    num = int(input("Digite um número: "))
    if num > maior:
        maior = num
print("Maior número lido:", maior)
