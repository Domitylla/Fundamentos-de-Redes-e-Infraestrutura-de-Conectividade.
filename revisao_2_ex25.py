# revisao_2_ex25.py
x = int(input("Digite a base: "))
y = int(input("Digite o expoente: "))
resultado = 1
for _ in range(y):
    resultado *= x
print(f"{x}^{y} =", resultado)
