# revisao_2_ex44.py
idades = []
alturas = []
pesos = []
sexos = []

for _ in range(25):
    idades.append(int(input("Idade: ")))
    sexos.append(input("Sexo (M/F): ").upper())
    alturas.append(float(input("Altura: ")))
    pesos.append(float(input("Peso: ")))

mais_velho = max(idades)
mais_alto = max(alturas)
maior_peso = max(pesos)
media_altura = sum(alturas) / 25
media_imc = sum(p / (a ** 2) for p, a in zip(pesos, alturas)) / 25
perc_m = sexos.count('M') / 25 * 100
perc_f = sexos.count('F') / 25 * 100

print("Idade mais velha:", mais_velho)
print("Maior altura:", mais_alto)
print("Maior peso:", maior_peso)
print("Média de altura:", round(media_altura, 2))
print("Média de IMC:", round(media_imc, 2))
print("Porcentagem Masculino:", round(perc_m, 1), "%")
print("Porcentagem Feminino:", round(perc_f, 1), "%")
