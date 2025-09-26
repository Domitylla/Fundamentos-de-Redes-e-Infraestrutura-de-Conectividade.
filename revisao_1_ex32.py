# revisao_1_ex32.py
preco = float(input("Digite o preço antigo: "))
if preco <= 50:
    novo = preco * 1.05
elif preco <= 100:
    novo = preco * 1.10
else:
    novo = preco * 1.15

print(f"Novo preço: R$ {novo:.2f}")

if novo < 80:
    print("Barato")
elif novo <= 120:
    print("Normal")
elif novo <= 200:
    print("Caro")
else:
    print("Muito caro")
