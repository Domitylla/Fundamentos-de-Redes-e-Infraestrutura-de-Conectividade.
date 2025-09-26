class Carro:
    def __init__(self, marca, modelo, cor, ano, valor, consumo, nivel=0):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.valor = valor
        self.consumo = consumo
        self.nivel = nivel

    def abastecer(self, litros):
        self.nivel += litros

    def andar(self, km):
        litros_necessarios = km / self.consumo
        if litros_necessarios <= self.nivel:
            self.nivel -= litros_necessarios
        else:
            print("Combustível insuficiente.")

    def verificar_nivel(self):
        print(f"Nível do tanque: {self.nivel:.2f} litros")

    def calcular_imposto(self):
        return self.valor * 0.035