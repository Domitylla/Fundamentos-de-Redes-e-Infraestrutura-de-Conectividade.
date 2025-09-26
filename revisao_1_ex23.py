# revisao_1_ex23.py
base_maior = float(input("Base maior: "))
base_menor = float(input("Base menor: "))
altura = float(input("Altura: "))

if base_maior > 0 and base_menor > 0 and altura > 0:
    area = (base_maior + base_menor) * altura / 2
    print("Área do trapézio:", area)
else:
    print("Valores inválidos")
