# revisao_2_ex33.py
medias = []
for i in range(10):
    notas = []
    for j in range(4):
        nota = float(input(f"Aluno {i+1} - Nota {j+1}: "))
        notas.append(nota)
    media = sum(notas) / 4
    medias.append(media)

aprovados = [m for m in medias if m >= 7.0]
print("Alunos com média >= 7.0:", len(aprovados))
