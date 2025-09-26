# revisao_2_ex43.py
nome = input("Nome do atleta: ")
notas = [float(input("Nota: ")) for _ in range(7)]

melhor = max(notas)
pior = min(notas)
notas.remove(melhor)
notas.remove(pior)

media = sum(notas) / len(notas)

print(f"Atleta: {nome}")
print("Melhor nota:", melhor)
print("Pior nota:", pior)
print("Média:", round(media, 2))
