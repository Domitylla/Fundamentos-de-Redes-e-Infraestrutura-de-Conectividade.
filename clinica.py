class Clinica:
    def __init__(self, nome):
        self.nome = nome
        self.pacientes = []
        self.consultas = []

    def adicionar_paciente(self, paciente):
        if self.buscar_paciente_por_cpf(paciente.cpf):
            print("Paciente já cadastrado.")
            return False
        self.pacientes.append(paciente)
        return True

    def buscar_paciente_por_cpf(self, cpf):
        for paciente in self.pacientes:
            if paciente.cpf == cpf:
                return paciente
        return None

    def listar_pacientes(self):
        return self.pacientes

    def adicionar_consulta(self, consulta):
        self.consultas.append(consulta)

    def listar_consultas(self):
        return self.consultas

    def listar_consultas_por_data(self, data):
        return [c for c in self.consultas if c.data == data]

    def listar_prescricoes_do_paciente(self, cpf):
        return [
            c.prescricao for c in self.consultas
            if c.paciente.cpf == cpf
        ]