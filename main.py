
from tutor import Tutor
from veterinario import Veterinario
from prescricao import Prescricao
from consulta import Consulta

def salvar_consulta_em_txt(consulta, caminho='dados/consultas.txt'):
    try:
        with open(caminho, 'a', encoding='utf-8') as arquivo:
            arquivo.write(str(consulta) + "\n" + "-"*40 + "\n")
        print("Consulta salva com sucesso.")
    except Exception as e:
        print(f"Erro ao salvar consulta: {e}")

def cadastrar_consulta():
    print("\n--- Cadastro de Consulta ---")
    try:
        nome_tutor = input("Nome do Tutor: ")
        cpf_tutor = input("CPF do Tutor: ")
        tel_tutor = input("Telefone do Tutor: ")
        endereco = input("Endereço do Tutor: ")

        tutor = Tutor(nome_tutor, cpf_tutor, tel_tutor, endereco)

        nome_vet = input("Nome do Veterinário: ")
        cpf_vet = input("CPF do Veterinário: ")
        tel_vet = input("Telefone do Veterinário: ")
        crmv = input("CRMV do Veterinário: ")

        vet = Veterinario(nome_vet, cpf_vet, tel_vet, crmv)

        nome_animal = input("Nome do Animal: ")
        descricao = input("Descrição da Consulta: ")
        medicamentos = input("Medicamentos Prescritos: ")

        prescricao = Prescricao(descricao, medicamentos)
        consulta = Consulta(tutor, vet, nome_animal, prescricao)

        salvar_consulta_em_txt(consulta)

    except Exception as erro:
        print(f"Erro durante o cadastro: {erro}")

def listar_consultas():
    try:
        with open('dados/consultas.txt', 'r', encoding='utf-8') as arquivo:
            print("\n--- Listagem de Consultas ---\n")
            print(arquivo.read())
    except FileNotFoundError:
        print("Arquivo de consultas não encontrado.")
    except Exception as erro:
        print(f"Erro ao ler arquivo: {erro}")

def menu():
    while True:
        print("\n---- Sistema PetCare ----")
        print("1 - Cadastrar Consulta")
        print("2 - Listar Consultas")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_consulta()
        elif opcao == '2':
            listar_consultas()
        elif opcao == '3':
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
