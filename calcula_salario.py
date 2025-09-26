def calcula_salario(horas, valor_hora):
    if horas <= 40:
        return horas * valor_hora
    extra = horas - 40
    return 40 * valor_hora + extra * valor_hora * 1.5