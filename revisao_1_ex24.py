# revisao_1_ex24.py
print("Operações:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão")
op = int(input("Escolha a operação (1-4): "))
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

if op == 1:
    print("Resultado:", a + b)
elif op == 2:
    print("Resultado:", a - b)
elif op == 3:
    print("Resultado:", a * b)
elif op == 4:
    if b != 0:
        print("Resultado:", a / b)
    else:
        print("Divisão por zero!")
else:
    print("Opção inválida")
