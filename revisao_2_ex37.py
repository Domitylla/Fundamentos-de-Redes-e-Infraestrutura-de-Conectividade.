# revisao_2_ex37.py
while True:
    r1 = float(input("Digite R1: "))
    if r1 == 0:
        break
    r2 = float(input("Digite R2: "))
    if r2 == 0:
        break
    r = (r1 * r2) / (r1 + r2)
    print("Resistência equivalente:", r)
