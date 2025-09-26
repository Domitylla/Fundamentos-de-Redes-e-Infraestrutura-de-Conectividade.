from prescricao import Prescricao

class Consulta:
    def __init__(self, paciente, data, medico):
        self.paciente = paciente
        self.data = data
        self.medico = medico
        self.prescricao = Prescricao()

    def __str__(self):
        return (
            f"Paciente: {self.paciente.nome}\n"
            f"Data: {self.data}\n"
            f"Médico: {self.medico}\n"
            f"Prescrição:\n{self.prescricao}"
        )

    def resumo(self):
        return f"{self.data} - {self.paciente.nome} - {self.medico}"