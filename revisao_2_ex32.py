# revisao_2_ex32.py
consoantes = []
vogais = 'aeiou'

for _ in range(10):
    c = input("Digite um caractere: ").lower()
    if c.isalpha() and c not in vogais:
        consoantes.append(c)

print("Consoantes:", consoantes)
print("Total:", len(consoantes))
