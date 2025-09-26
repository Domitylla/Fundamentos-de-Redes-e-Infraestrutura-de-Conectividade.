TAM = 10

def inserir_ordenado(vetor, valor):
    i = len(vetor) - 1
    vetor.append(valor)  # adiciona temporariamente
    while i >= 0 and vetor[i] > valor:
        vetor[i + 1] = vetor[i]
        i -= 1
    vetor[i + 1] = valor

def imprimir_vetor(vetor):
    print("Vetor ordenado:", vetor)

def main():
    vetor = []
    for i in range(TAM):
        valor = int(input(f"Digite o {i + 1}º valor: "))
        inserir_ordenado(vetor, valor)
    imprimir_vetor(vetor)

if __name__ == "__main__":
    main()