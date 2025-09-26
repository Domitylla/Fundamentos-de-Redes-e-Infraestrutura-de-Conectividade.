# revisao_1_ex31.py
cardapio = {
    100: ("Hot Dog", 1.20),
    101: ("Bauru", 1.30),
    102: ("X-Salada", 1.50),
    103: ("X-Bacon", 1.20),
    104: ("X-Burguer", 17.00),
    105: ("Suco de Laranja", 9.50),
    106: ("Refrigerante", 6.00)
}

codigo = int(input("Digite o código do produto: "))
quantidade = int(input("Digite a quantidade: "))

if codigo in cardapio:
    produto, preco = cardapio[codigo]
    total = preco * quantidade
    print(f"{produto} x {quantidade} = R$ {total:.2f}")
else:
    print("Código inválido")
