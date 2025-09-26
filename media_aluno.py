def media_aluno(n1, n2, n3, tipo):
    if tipo.upper() == 'A':
        return (n1 + n2 + n3) / 3
    elif tipo.upper() == 'P':
        return (n1 * 5 + n2 * 3 + n3 * 2) / 10
    return None