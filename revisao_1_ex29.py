# revisao_1_ex29.py
distancia = float(input("Distância percorrida (km): "))
litros = float(input("Litros consumidos: "))
consumo = distancia / litros
print(f"Consumo: {consumo:.2f} km/l")
if consumo < 8:
    print("Venda o carro!")
elif consumo <= 14:
    print("Econômico!")
else:
    print("Super econômico!")
