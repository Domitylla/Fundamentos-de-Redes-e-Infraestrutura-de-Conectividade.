# revisao_2_ex19.py
cont = 0
pares = 0
while True:
    n = int(input("Digite um número (0 para sair): "))
    if n == 0:
        break
    cont += 1
    if n % 2 == 0:
        pares += 1
print("Total de números lidos:", cont)
print("Total de pares:", pares)
