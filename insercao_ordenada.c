#include <stdio.h>

#define TAM 10

void inserirOrdenado(int vetor[], int *n, int valor) {
    if (*n >= TAM) {
        printf("Vetor cheio!\n");
        return;
    }

    int i = *n - 1;
    while (i >= 0 && vetor[i] > valor) {
        vetor[i + 1] = vetor[i];
        i--;
    }
    vetor[i + 1] = valor;
    (*n)++;
}

void imprimirVetor(int vetor[], int n) {
    printf("Vetor ordenado: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", vetor[i]);
    }
    printf("\n");
}

int main() {
    int vetor[TAM];
    int n = 0;
    int valor;

    for (int i = 0; i < TAM; i++) {
        printf("Digite o %dº valor: ", i + 1);
        scanf("%d", &valor);
        inserirOrdenado(vetor, &n, valor);
    }

    imprimirVetor(vetor, n);
    return 0;
}