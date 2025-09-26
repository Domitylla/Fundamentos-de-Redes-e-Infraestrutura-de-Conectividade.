# revisao_1_ex21.py
n = int(input("Digite um número de 1 a 7: "))
dias = ["Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", 
        "Quinta-feira", "Sexta-feira", "Sábado"]
if 1 <= n <= 7:
    print("Dia da semana:", dias[n - 1])
else:
    print("Número inválido")
