# revisao_1_ex28.py
valor = float(input("Digite o valor do produto: "))
estado = input("Digite o estado (MG/SP/RJ/MS): ").upper()

if estado == "MG":
    imposto = 0.07
elif estado == "SP":
    imposto = 0.12
elif estado == "RJ":
    imposto = 0.15
elif estado == "MS":
    imposto = 0.08
else:
    print("Estado inválido")
    imposto = None

if imposto is not None:
    total = valor * (1 + imposto)
    print("Valor final:", round(total, 2))
