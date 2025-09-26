
from pessoa import Pessoa

class Veterinario(Pessoa):
    def __init__(self, nome, cpf, telefone, crmv):
        super().__init__(nome, cpf, telefone)
        self.crmv = crmv

    def __str__(self):
        return super().__str__() + f", CRMV: {self.crmv}"
