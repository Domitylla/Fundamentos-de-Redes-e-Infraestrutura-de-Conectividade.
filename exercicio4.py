# Exercício 4 - Cabos de Rede
a = float(input("Digite o primeiro termo (a): "))
n = int(input("Digite o número de termos (n): "))
r = float(input("Digite a razão (r): "))

pa = [a + i*r for i in range(n)]
print(pa)

print("O quinto termo é:", pa[4] if n >= 5 else "Não existe quinto termo")

termo_central = (pa[0] + pa[-1]) / 2
print("O termo central é:", termo_central)

soma = sum(pa)
print(f"Total: {soma} metros")
