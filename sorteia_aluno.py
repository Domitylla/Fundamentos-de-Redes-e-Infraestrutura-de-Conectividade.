import random
def sorteia_aluno(qtd, nomes=None):
    if nomes is None:
        nomes = [input("Digite um nome: ") for _ in range(qtd)]
    if nomes:
        sorteado = random.choice(nomes)
        return f"O primeiro aluno(a) a apresentar será: {sorteado}"
    return "Nenhum nome informado."