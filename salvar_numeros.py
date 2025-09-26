TAM = 15

def ler_numeros(tamanho):
    vetor = []
    for i in range(tamanho):
        while True:
            try:
                num = float(input(f"Digite o {i + 1}º número real: "))
                vetor.append(num)
                break
            except ValueError:
                print("Entrada inválida. Tente novamente.")
    return vetor

def salvar_em_arquivo(vetor, nome_arquivo):
    try:
        with open(nome_arquivo, "w") as f:
            for numero in vetor:
                f.write(f"{numero:.2f}\n")
        print(f"Dados salvos em '{nome_arquivo}'")
    except IOError:
        print("Erro ao salvar o arquivo.")

def main():
    vetor = ler_numeros(TAM)
    salvar_em_arquivo(vetor, "dados.txt")

if __name__ == "__main__":
    main()