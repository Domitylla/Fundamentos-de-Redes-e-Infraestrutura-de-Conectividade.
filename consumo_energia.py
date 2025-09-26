def consumo_kwh(potencia_w, tempo_h):
    return (potencia_w / 1000) * tempo_h

def conta_energia(consumo, valor_kwh):
    return consumo * valor_kwh