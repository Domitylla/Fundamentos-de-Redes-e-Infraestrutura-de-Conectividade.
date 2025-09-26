from paciente import Paciente
from consulta import Consulta

p1 = Paciente("João Silva", 30, "M", "01/01/1995", "12345678900", "99999-0000", "joao@email.com", "Rua A, 123")
p2 = Paciente("Maria Souza", 28, "F", "15/05/1997", "98765432100", "98888-1111", "maria@email.com", "Av. B, 456")
print(p1)
print(p2)

consulta1 = Consulta(p1, "01/06/2025", "Dr. Silva")
consulta1.prescricao.adicionar_medicamento("Paracetamol", "500mg")
consulta1.prescricao.adicionar_medicamento("Ibuprofeno", "200mg")
print(consulta1)

consulta2 = Consulta(p2, "02/06/2025", "Dra. Paula")
consulta2.prescricao.adicionar_medicamento("Dipirona", "1g")
print(consulta2)