class NotaFiscal:
    def __init__(self, numero, tipo, serie, cnpj, razao_social, data, icms, frete, ipi, valor_produto):
        self.numero = numero
        self.tipo = tipo
        self.serie = serie
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.data = data
        self.icms = icms
        self.frete = frete
        self.ipi = ipi
        self.valor_produto = valor_produto
        self.valor_total = 0

    def obter_numero(self):
        return self.numero

    def obter_data_emissao(self):
        return self.data

    def alterar_razao_social(self, nova_razao):
        self.razao_social = nova_razao

    def calcular_valor_total(self):
        self.valor_total = self.valor_produto + self.frete + self.icms + self.ipi
        return self.valor_total