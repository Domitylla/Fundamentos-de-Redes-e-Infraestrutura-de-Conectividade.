# revisao_1_ex07.py
preco = float(input("Digite o valor de aquisição do produto: "))
if preco < 50:
    venda = preco * 1.45
else:
    venda = preco * 1.30
print("Preço de venda: R$", round(venda, 2))
