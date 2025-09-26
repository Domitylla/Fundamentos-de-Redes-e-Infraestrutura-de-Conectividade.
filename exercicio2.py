# Exercício 2 - Piscina Olímpica
comp = int(input("Digite o comprimento da piscina (em centímetros): "))
larg = int(input("Digite a largura da piscina (em centímetros): "))
prof = int(input("Digite a profundidade da piscina (em centímetros): "))

comp_m = comp / 100
larg_m = larg / 100
prof_m = prof / 100

volume_m3 = comp_m * larg_m * prof_m
volume_litros = volume_m3 * 1000

print(f"Volume = {volume_m3:.1f} m³")
print(f"{volume_litros:,.0f} Litros".replace(",", "."))
