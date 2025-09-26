#include <stdio.h>

#define TAM 15

void lerNumeros(float vetor[], int tamanho) {
    for (int i = 0; i < tamanho; i++) {
        printf("Digite o %dº número real: ", i + 1);
        scanf("%f", &vetor[i]);
    }
}

void salvarEmArquivo(float vetor[], int tamanho, const char *nomeArquivo) {
    FILE *arquivo = fopen(nomeArquivo, "w");
    if (arquivo == NULL) {
        printf("Erro ao abrir o arquivo.\n");
        return;
    }

    for (int i = 0; i < tamanho; i++) {
        fprintf(arquivo, "%.2f\n", vetor[i]);
    }

    fclose(arquivo);
    printf("Dados salvos em '%s'\n", nomeArquivo);
}

int main() {
    float vetor[TAM];
    lerNumeros(vetor, TAM);
    salvarEmArquivo(vetor, TAM, "dados.txt");
    return 0;
}