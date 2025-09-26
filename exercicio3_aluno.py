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