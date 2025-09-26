# revisao_1_ex25.py
a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        tipo = "Equilátero"
    elif a == b or b == c or a == c:
        tipo = "Isósceles"
    else:
        tipo = "Escaleno"
    print("Triângulo:", tipo)
else:
    print("Não é triângulo")
