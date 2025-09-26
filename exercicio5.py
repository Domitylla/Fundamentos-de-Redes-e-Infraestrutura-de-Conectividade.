# Exercício 5 - Semáforo
vermelho = int(input("Digite o valor (Vermelho): "))
amarelo = int(input("Digite o valor (Amarelo): "))
verde = int(input("Digite o valor (Verde): "))

soma = vermelho + amarelo + verde

if soma == 0:
    print("Semáforo desligado!!")
    print("Status: 0 0 0")
elif soma > 1:
    print("Entrada inválida!")
else:
    if vermelho == 1:
        print("Vermelho ON")
    elif amarelo == 1:
        print("Amarelo ON")
    elif verde == 1:
        print("Verde ON")
    print(f"Status: {vermelho} {amarelo} {verde}")
