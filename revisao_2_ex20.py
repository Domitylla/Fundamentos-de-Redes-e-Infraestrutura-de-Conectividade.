# revisao_2_ex20.py
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
if a > b:
    a, b = b, a

soma_pares = 0
mult_impares = 1

for i in range(a, b+1):
    if i % 2 == 0:
        soma_pares += i
    else:
        mult_impares *= i
print("Soma dos pares:", soma_pares)
print("Multiplicação dos ímpares:", mult_impares)
