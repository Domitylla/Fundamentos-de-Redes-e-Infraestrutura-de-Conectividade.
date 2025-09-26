class AlunoAcademia:
    def __init__(self, nome, idade, peso, altura, mensalidade=120):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.mensalidade = mensalidade

    def calcular_IMC(self):
        return self.peso / (self.altura ** 2)

    def obter_valor_mensalidade(self):
        if self.idade < 18:
            return self.mensalidade * 0.9
        return self.mensalidade