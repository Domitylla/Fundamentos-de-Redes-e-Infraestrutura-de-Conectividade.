# revisao_2_ex30.py
vetor = []
for _ in range(10):
    vetor.append(int(input("Digite um número: ")))
valor = int(input("Digite um número para verificar: "))
if valor in vetor:
    print("O valor está no vetor.")
else:
    print("Valor não encontrado.")
