# revisao_1_ex26.py
idade = int(input("Digite a idade: "))
tempo = int(input("Digite o tempo de serviço: "))

if idade >= 65 or tempo >= 30 or (idade >= 60 and tempo >= 25):
    print("Pode se aposentar")
else:
    print("Não pode se aposentar")
