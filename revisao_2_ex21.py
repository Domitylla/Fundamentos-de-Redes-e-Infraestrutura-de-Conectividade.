# revisao_2_ex21.py
soma = 0
quant = 0
while True:
    nota = float(input("Digite a nota (0 a 10): "))
    if nota < 0 or nota > 10:
        break
    soma += nota
    quant += 1
if quant > 0:
    print("Média:", soma / quant)
else:
    print("Nenhuma nota válida.")
