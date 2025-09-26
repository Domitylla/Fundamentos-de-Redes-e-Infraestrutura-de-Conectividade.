# revisao_2_ex39.py
import random
numero = random.randint(1, 100)
tentativas = 0
while True:
    chute = int(input("Tente adivinhar o número (1 a 100): "))
    tentativas += 1
    if chute == numero:
        print(f"Parabéns! Acertou em {tentativas} tentativas.")
        break
    elif chute < numero:
        print("Muito baixo.")
    else:
        print("Muito alto.")
