# revisao_2_ex10.py
n = int(input("Digite a quantidade de ímpares desejada: "))
contador = 0
num = 1
while contador < n:
    if num % 2 == 1:
        print(num)
        contador += 1
    num += 1
