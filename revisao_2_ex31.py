# revisao_2_ex31.py
valores = []
pares = []
impares = []

for _ in range(20):
    n = int(input("Digite um número: "))
    valores.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print("Todos:", valores)
print("Pares:", pares)
print("Ímpares:", impares)
