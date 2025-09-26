# revisao_1_ex36.py
peso = float(input("Digite o peso (kg): "))
altura = float(input("Digite a altura (m): "))
imc = peso / (altura ** 2)

print(f"IMC: {imc:.2f}")
if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Saudável")
elif imc < 30:
    print("Peso em excesso")
elif imc < 35:
    print("Obesidade Grau I")
elif imc < 40:
    print("Obesidade Grau II (severa)")
else:
    print("Obesidade Grau III (mórbida)")
