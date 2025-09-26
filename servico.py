class Servico:
    def __init__(self, carro, data, descricao, valor_pecas, valor_mao_obra):
        self.carro = carro  # composição
        self.data = data
        self.descricao = descricao
        self.valor_pecas = valor_pecas
        self.valor_mao_obra = valor_mao_obra

    def calcular_total(self):
        return self.valor_pecas + self.valor_mao_obra