class Paciente:
    def __init__(self, nome, idade, genero, data_nascimento, cpf, telefone, email, endereco):
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def __str__(self):
        return (
            f"Nome: {self.nome}\n"
            f"Idade: {self.idade} anos\n"
            f"Gênero: {self.genero}\n"
            f"Nascimento: {self.data_nascimento}\n"
            f"CPF: {self.cpf}\n"
            f"Telefone: {self.telefone}\n"
            f"E-mail: {self.email}\n"
            f"Endereço: {self.endereco}"
        )

    def exportar_csv(self):
        return f"{self.nome};{self.idade};{self.genero};{self.data_nascimento};{self.cpf};{self.telefone};{self.email};{self.endereco}"