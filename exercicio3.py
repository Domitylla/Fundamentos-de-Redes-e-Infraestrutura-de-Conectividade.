# Exercício 3 - Plano de Internet
x = int(input("Quota mensal (MB): "))
n = int(input("Número de meses: "))

quota_total = x * (n + 1)
consumo_total = 0

for i in range(n):
    c = int(input(f"Consumo do mês {i+1}: "))
    consumo_total += c

print(quota_total - consumo_total)
