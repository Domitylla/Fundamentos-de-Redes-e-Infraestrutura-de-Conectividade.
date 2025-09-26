
from prescricao import Prescricao

class Consulta:
    def __init__(self, tutor, veterinario, nome_animal, prescricao: Prescricao):
        self.tutor = tutor
        self.veterinario = veterinario
        self.nome_animal = nome_animal
        self.prescricao = prescricao

    def __str__(self):
        return (
            f"Animal: {self.nome_animal}\n"
            f"Tutor: {self.tutor}\n"
            f"Veterinário: {self.veterinario}\n"
            f"Prescrição: {self.prescricao}\n"
        )
