# revisao_2_ex29.py
soma = 0
numeros = []
for _ in range(5):
    n = int(input("Digite um número: "))
    soma += n
    numeros.append(n)
print("Soma:", soma)
print("Números digitados:")
for n in numeros:
    print(n)
