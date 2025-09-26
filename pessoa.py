class Pessoa:
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}, Telefone: {self.telefone}"