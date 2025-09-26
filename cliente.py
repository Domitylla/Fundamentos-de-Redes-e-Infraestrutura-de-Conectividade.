from pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, cpf, telefone, email):
        super().__init__(nome, cpf, telefone)
        self.email = email
        self.carros = []

    def cadastrarCliente(self):
        try:
            with open("clientes.txt", "a", encoding="utf-8") as file:
                file.write(f"{self.nome},{self.cpf},{self.telefone},{self.email}\n")
        except Exception as e:
            print(f"Erro ao cadastrar cliente: {e}")

    @staticmethod
    def listarClientes():
        try:
            with open("clientes.txt", "r", encoding="utf-8") as file:
                print("\n--- Lista de Clientes ---")
                for linha in file:
                    nome, cpf, telefone, email = linha.strip().split(",")
                    print(f"Nome: {nome}, CPF: {cpf}, Telefone: {telefone}, Email: {email}")
        except FileNotFoundError:
            print("Arquivo de clientes não encontrado.")