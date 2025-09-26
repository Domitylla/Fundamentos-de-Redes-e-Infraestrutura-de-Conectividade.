import math
def calcular_tempo(minutos):
    if minutos < 15:
        return 0.0
    horas_adicionais = math.ceil((minutos - 60) / 60) if minutos > 60 else 0
    return 9.0 + horas_adicionais * 1.5