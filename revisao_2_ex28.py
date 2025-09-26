# revisao_2_ex28.py
salario = 4000
ano = 2020
aumento = 0.015

while ano <= 2025:
    salario += salario * aumento
    aumento *= 2
    ano += 1
print("Salário atual:", round(salario, 2))
