# revisao_2_ex40.py
def menu():
    print("\nMenu:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

while True:
    menu()
    opcao = int(input("Escolha a opção: "))
    if opcao == 5:
        break
    a = float(input("Valor 1: "))
    b = float(input("Valor 2: "))
    if opcao == 1:
        print("Resultado:", a + b)
    elif opcao == 2:
        print("Resultado:", a - b)
    elif opcao == 3:
        print("Resultado:", a * b)
    elif opcao == 4:
        if b != 0:
            print("Resultado:", a / b)
        else:
            print("Divisão por zero!")
    else:
        print("Opção inválida.")
