from clinica import Clinica
from paciente import Paciente
from consulta import Consulta
from utils.arquivos import salvar_em_arquivo

def cadastrar_paciente(clinica):
    try:
        nome = input("Nome completo: ")
        idade = int(input("Idade: "))
        genero = input("Gênero: ")
        data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")
        cpf = input("CPF: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        endereco = input("Endereço: ")
        paciente = Paciente(nome, idade, genero, data_nascimento, cpf, telefone, email, endereco)
        if clinica.adicionar_paciente(paciente):
            salvar_em_arquivo('dados/pacientes.txt', paciente.exportar_csv())
            print("✅ Paciente cadastrado!")
        else:
            print("Paciente já existe no sistema.")
    except Exception as e:
        print(f"Erro: {e}")

def registrar_consulta(clinica):
    cpf = input("CPF do paciente: ")
    paciente = clinica.buscar_paciente_por_cpf(cpf)
    if not paciente:
        print("Paciente não encontrado.")
        return

    data = input("Data da consulta (DD/MM/AAAA): ")
    medico = input("Nome do médico: ")
    consulta = Consulta(paciente, data, medico)

    while True:
        med = input("Medicamento (vazio p/ sair): ")
        if not med:
            break
        dose = input("Dose: ")
        consulta.prescricao.adicionar_medicamento(med, dose)

    clinica.adicionar_consulta(consulta)
    salvar_em_arquivo('dados/consultas.txt', consulta.resumo())
    print("✅ Consulta registrada!")

def menu():
    clinica = Clinica("Clínica Saúde e Vida")

    while True:
        print("\n--- Menu ---")
        print("1. Cadastrar paciente")
        print("2. Registrar consulta")
        print("3. Buscar paciente por CPF")
        print("4. Consultas por data")
        print("5. Prescrições por CPF")
        print("6. Listar pacientes")
        print("7. Listar consultas")
        print("8. Sair")

        op = input("Escolha: ")
        if op == "1":
            cadastrar_paciente(clinica)
        elif op == "2":
            registrar_consulta(clinica)
        elif op == "3":
            cpf = input("CPF: ")
            p = clinica.buscar_paciente_por_cpf(cpf)
            print(p if p else "Não encontrado.")
        elif op == "4":
            data = input("Data: ")
            for c in clinica.listar_consultas_por_data(data):
                print(c)
        elif op == "5":
            cpf = input("CPF: ")
            prescricoes = clinica.listar_prescricoes_do_paciente(cpf)
            if not prescricoes:
                print("Nenhuma prescrição encontrada para este paciente.")
            for i, p in enumerate(prescricoes, 1):
                print(f"Prescrição {i}:\n{p}\n")
        elif op == "6":
            for p in clinica.listar_pacientes():
                print(p)
        elif op == "7":
            for c in clinica.listar_consultas():
                print(c)
        elif op == "8":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()