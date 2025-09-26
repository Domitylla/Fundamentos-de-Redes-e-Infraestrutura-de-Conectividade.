def reverso_numero(n):
    return int(str(abs(n))[::-1]) * (1 if n >= 0 else -1)