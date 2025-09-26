class Prescricao:
    def __init__(self):
        self.medicamentos = []

    def adicionar_medicamento(self, nome, dose):
        self.medicamentos.append((nome, dose))

    def __str__(self):
        if not self.medicamentos:
            return "Nenhum medicamento prescrito."
        return "\n".join([f"{nome} - {dose}" for nome, dose in self.medicamentos])