
class Prescricao:
    def __init__(self, descricao, medicamentos):
        self.descricao = descricao
        self.medicamentos = medicamentos

    def __str__(self):
        return f"Descrição: {self.descricao}, Medicamentos: {self.medicamentos}"
