# revisao_2_ex36.py
inicio = int(input("Valor inicial: "))
fim = int(input("Valor final: "))

if inicio > fim:
    print("Intervalo de valores inválido")
else:
    soma = sum(i for i in range(inicio, fim+1) if i % 2 == 1)
    print("Soma dos ímpares:", soma)
