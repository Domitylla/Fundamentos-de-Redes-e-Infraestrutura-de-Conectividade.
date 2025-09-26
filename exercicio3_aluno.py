
class Aluno:
    def __init__(self, nome, ra, notas):
        self.nome = nome
        self.ra = ra
        self.notas = notas

    def mostrar_situacao(self):
        media = sum(self.notas) / len(self.notas)
        if media >= 7:
            return "APROVADO"
        elif media >= 5:
            return "EXAME"
        else:
            return "REPROVADO"

# Teste
assert Aluno("A", "1", [7, 7, 7, 7]).mostrar_situacao() == "APROVADO"
assert Aluno("B", "2", [5, 6, 5, 6]).mostrar_situacao() == "EXAME"
assert Aluno("C", "3", [3, 4, 5, 4]).mostrar_situacao() == "REPROVADO"
