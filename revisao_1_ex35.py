# revisao_1_ex35.py
custo_fabrica = float(input("Digite o custo de fábrica: "))
if custo_fabrica <= 12000:
    distribuidor = custo_fabrica * 0.05
    impostos = 0
elif custo_fabrica <= 25000:
    distribuidor = custo_fabrica * 0.10
    impostos = custo_fabrica * 0.15
else:
    distribuidor = custo_fabrica * 0.15
    impostos = custo_fabrica * 0.20

total = custo_fabrica + distribuidor + impostos
print("Custo ao consumidor: R$", round(total, 2))
