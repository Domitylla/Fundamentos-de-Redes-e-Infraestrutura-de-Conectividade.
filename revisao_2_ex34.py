# revisao_2_ex34.py
n = int(input("Digite um número inteiro maior que 1: "))
if n <= 1:
    print("Número inválido")
else:
    primo = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            primo = False
            break
    print("É primo" if primo else "Não é primo")
