# revisao_2_ex22.py
n = int(input("Digite um número: "))
soma = 0
for i in range(1, n):
    if n % i == 0:
        soma += i
print("Soma dos divisores:", soma)
