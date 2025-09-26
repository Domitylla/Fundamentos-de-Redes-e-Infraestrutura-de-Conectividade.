class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def getNome(self):
        return self.nome

    def setIdade(self, nova_idade):
        self.idade = nova_idade

    def imprimeEndereco(self):
        print(f"Endereço: {self.endereco}")