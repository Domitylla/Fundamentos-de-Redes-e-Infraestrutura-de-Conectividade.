# revisao_2_ex35.py
n = int(input("Digite a quantidade de primos a somar: "))
primos = []
num = 2
while len(primos) < n:
    if all(num % d != 0 for d in range(2, int(num**0.5) + 1)):
        primos.append(num)
    num += 1
print("Soma dos primos:", sum(primos))
