class Funcionario:
    def __init__(self, nome, sobrenome, horas_trabalhadas, valor_hora):
        self.nome = nome
        self.sobrenome = sobrenome
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def nome_completo(self):
        return f"{self.nome} {self.sobrenome}"

    def calcular_salario(self):
        return self.horas_trabalhadas * self.valor_hora

    def incrementar_horas(self, horas):
        self.horas_trabalhadas += horas