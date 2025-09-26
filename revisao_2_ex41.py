# revisao_2_ex41.py
soma_quadrados = sum(i**2 for i in range(1, 101))
quadrado_soma = sum(range(1, 101)) ** 2
print("Diferença:", quadrado_soma - soma_quadrados)
