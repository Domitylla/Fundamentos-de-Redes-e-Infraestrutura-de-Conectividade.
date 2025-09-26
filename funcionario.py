from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, telefone, matricula, comissao):
        super().__init__(nome, cpf, telefone)
        self.matricula = matricula
        self.comissao = comissao

    def getSalario(self):
        salario_fixo = 2000.0
        return salario_fixo + self.comissao