# revisao_1_ex33.py
venda = float(input("Digite o valor da venda mensal: "))
if venda >= 100000:
    comissao = 700 + 0.16 * venda
elif venda >= 80000:
    comissao = 650 + 0.14 * venda
elif venda >= 60000:
    comissao = 600 + 0.14 * venda
elif venda >= 40000:
    comissao = 550 + 0.14 * venda
elif venda >= 20000:
    comissao = 500 + 0.14 * venda
else:
    comissao = 400 + 0.14 * venda
print(f"Comissão: R$ {comissao:.2f}")
