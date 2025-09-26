def consumo_combustivel(distancia_km, litros):
    consumo = distancia_km / litros
    if consumo < 8:
        return consumo, "Gasta muito!"
    elif consumo <= 15:
        return consumo, "Econômico!"
    return consumo, "Super econômico!"