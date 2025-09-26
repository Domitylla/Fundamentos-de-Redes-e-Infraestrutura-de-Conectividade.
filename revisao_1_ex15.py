# revisao_1_ex15.py
horas = float(input("Digite o número de horas trabalhadas: "))
salario_bruto = horas * 40.5
if salario_bruto > 2500:
    salario_liquido = salario_bruto * (1 - 0.11)
else:
    salario_liquido = salario_bruto
print("Salário líquido: R$", round(salario_liquido, 2))
