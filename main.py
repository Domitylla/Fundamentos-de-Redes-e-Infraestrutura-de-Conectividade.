from cliente import Cliente
from carro import Carro
from funcionario import Funcionario
from servico import Servico

def main():
    while True:
        print("\n--- Sistema de Oficina ---")
        print("1. Cadastrar Cliente")
        print("2. Listar Clientes")
        print("3. Cadastrar Carro")
        print("4. Calcular IPVA")
        print("5. Calcular Salário Funcionário")
        print("6. Calcular Serviço")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            cpf = input("CPF: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            cliente = Cliente(nome, cpf, telefone, email)
            cliente.cadastrarCliente()
            print("Cliente cadastrado.")

        elif opcao == "2":
            Cliente.listarClientes()

        elif opcao == "3":
            modelo = input("Modelo: ")
            marca = input("Marca: ")
            placa = input("Placa: ")
            ano = int(input("Ano: "))
            km = float(input("Quilometragem: "))
            valor = float(input("Valor do carro: "))
            carro = Carro(modelo, marca, placa, ano, km, valor)
            carro.calcular_ipva()
            carro.cadastrarCarro()
            print(f"Carro cadastrado com IPVA: R$ {carro.ipva:.2f}")

        elif opcao == "4":
            valor = float(input("Valor do carro: "))
            carro = Carro("modelo", "marca", "placa", 2020, 0, valor)
            carro.calcular_ipva()
            print(f"IPVA calculado: R$ {carro.ipva:.2f}")

        elif opcao == "5":
            nome = input("Nome: ")
            cpf = input("CPF: ")
            telefone = input("Telefone: ")
            matricula = input("Matrícula: ")
            comissao = float(input("Comissão: "))
            funcionario = Funcionario(nome, cpf, telefone, matricula, comissao)
            print(f"Salário: R$ {funcionario.getSalario():.2f}")

        elif opcao == "6":
            modelo = input("Modelo do carro: ")
            carro = Carro(modelo, "", "", 0, 0, 0)
            data = input("Data do serviço: ")
            descricao = input("Descrição do serviço: ")
            pecas = float(input("Valor das peças: "))
            mao_obra = float(input("Valor da mão de obra: "))
            servico = Servico(carro, data, descricao, pecas, mao_obra)
            print(f"Total do serviço: R$ {servico.calcular_total():.2f}")

        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()