def calculadora(a, b, simbolo):
    operacoes = {
        '+': a + b,
        '-': a - b,
        '*': a * b,
        '/': a / b if b != 0 else None
    }
    return operacoes.get(simbolo, None)