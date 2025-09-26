# revisao_1_ex19.py
nota1 = float(input("Nota 1 (peso 1): "))
nota2 = float(input("Nota 2 (peso 1): "))
nota3 = float(input("Nota 3 (peso 2): "))
media = (nota1 + nota2 + 2 * nota3) / 4
print("Média ponderada:", media)
if media >= 60:
    print("Aprovado")
else:
    print("Reprovado")
