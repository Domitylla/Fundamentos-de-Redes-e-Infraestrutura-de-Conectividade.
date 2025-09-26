# revisao_2_ex24.py
soma = 0
cont = 0
while True:
    idade = int(input("Digite a idade (0 para sair): "))
    if idade == 0:
        break
    soma += idade
    cont += 1
if cont > 0:
    print("Média de idades:", soma / cont)
else:
    print("Nenhuma idade válida.")
