# revisao_1_ex17.py
altura = float(input("Digite a altura (em metros): "))
sexo = input("Digite o sexo (M/F): ").upper()
if sexo == 'M':
    peso = (72.7 * altura) - 58
elif sexo == 'F':
    peso = (62.1 * altura) - 44.7
else:
    peso = None
    print("Sexo inválido")
if peso is not None:
    print("Peso ideal:", round(peso, 2))
