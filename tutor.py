
from pessoa import Pessoa

class Tutor(Pessoa):
    def __init__(self, nome, cpf, telefone, endereco):
        super().__init__(nome, cpf, telefone)
        self.endereco = endereco

    def __str__(self):
        return super().__str__() + f", Endereço: {self.endereco}"
