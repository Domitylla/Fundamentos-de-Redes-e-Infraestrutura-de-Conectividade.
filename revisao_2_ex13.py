# revisao_2_ex13.py
n = int(input("Digite um número par: "))
if n % 2 == 0:
    for i in range(0, n + 1, 2):
        print(i)
else:
    print("Número não é par.")
