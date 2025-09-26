# revisao_2_ex15.py
n = int(input("Digite um número ímpar positivo: "))
if n % 2 == 1 and n > 0:
    for i in range(1, n+1, 2):
        print(i)
else:
    print("Número inválido.")
