# revisao_1_ex34.py
salario = float(input("Digite o salário atual: "))
tempo = int(input("Digite o tempo de serviço (anos): "))

bonus = 0
if salario <= 500:
    salario *= 1.25
    if tempo < 1:
        bonus = 0
    else:
        bonus = 100
elif salario <= 1000:
    salario *= 1.20
    bonus = 100 if 1 <= tempo <= 3 else 0
elif salario <= 1500:
    salario *= 1.15
    bonus = 200 if 4 <= tempo <= 6 else 0
elif salario <= 2000:
    salario *= 1.10
    bonus = 300 if 7 <= tempo <= 10 else 0
else:
    bonus = 500 if tempo > 10 else 0

novo_salario = salario + bonus
print("Salário reajustado: R$", round(novo_salario, 2))
