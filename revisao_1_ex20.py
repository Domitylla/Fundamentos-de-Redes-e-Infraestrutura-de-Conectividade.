# revisao_1_ex20.py
trabalho = float(input("Nota do Trabalho de Laboratório (peso 2): "))
avaliacao = float(input("Nota da Avaliação Semestral (peso 3): "))
exame = float(input("Nota do Exame Final (peso 5): "))

media = (2 * trabalho + 3 * avaliacao + 5 * exame) / 10

print("Média final:", media)
if 0 <= media <= 2.9:
    print("Reprovado")
elif 3 <= media <= 5.9:
    print("Recuperação")
else:
    print("Aprovado")
