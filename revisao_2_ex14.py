# revisao_2_ex14.py
n = int(input("Digite um número par: "))
if n % 2 == 0:
    for i in range(n, -1, -2):
        print(i)
else:
    print("Número não é par.")
