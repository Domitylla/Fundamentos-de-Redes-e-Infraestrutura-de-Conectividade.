# revisao_1_ex18.py
n = int(input("Digite um número inteiro maior que zero: "))
if n <= 0:
    print("Número inválido")
else:
    soma = sum(int(digito) for digito in str(n))
    print("Soma dos algarismos:", soma)
