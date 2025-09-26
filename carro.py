class Carro:
    def __init__(self, modelo, marca, placa, ano, quilometragem, valor):
        self.modelo = modelo
        self.marca = marca
        self.placa = placa
        self.ano = ano
        self.quilometragem = quilometragem
        self.valor = valor
        self.ipva = 0.0

    def calcular_ipva(self, taxa=0.03):
        self.ipva = self.valor * taxa

    def cadastrarCarro(self):
        try:
            with open("carros.txt", "a", encoding="utf-8") as file:
                file.write(f"{self.modelo},{self.marca},{self.placa},{self.ano},{self.quilometragem},{self.valor},{self.ipva}\n")
        except Exception as e:
            print(f"Erro ao cadastrar carro: {e}")