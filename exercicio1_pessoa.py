
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
        return f"Endereço: {self.endereco}"

# Teste
p = Pessoa("João", 25, "Rua A")
assert p.getNome() == "João"
p.setIdade(26)
assert p.idade == 26
assert p.imprimeEndereco() == "Endereço: Rua A"
