# revisao_2_ex08.py
soma = 0
cont = 0
while cont < 10:
    n = int(input("Digite um número positivo: "))
    if n > 0:
        soma += n
        cont += 1
print("Média:", soma / 10)
