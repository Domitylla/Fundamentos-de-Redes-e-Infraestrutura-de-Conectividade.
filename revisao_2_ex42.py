# revisao_2_ex42.py
votos = [0] * 7
candidatos = {1: "José", 2: "João", 3: "Maria", 4: "Ana"}
while True:
    v = int(input("Digite o voto (1-6, 0 para sair): "))
    if v == 0:
        break
    if 1 <= v <= 6:
        votos[v] += 1
    else:
        print("Código inválido.")

total = sum(votos)
print("Total de votos:")
for cod, nome in candidatos.items():
    print(f"{nome}: {votos[cod]}")
print("Nulos:", votos[5])
print("Brancos:", votos[6])
if total:
    print("Percentual nulos:", votos[5]/total * 100)
    print("Percentual brancos:", votos[6]/total * 100)
