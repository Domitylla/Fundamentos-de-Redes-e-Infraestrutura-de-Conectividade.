# revisao_2_ex18.py
n = input("Digite um número entre 100 e 9999: ")
if 100 <= int(n) <= 9999:
    for d in n:
        print(d)
else:
    print("Número fora do intervalo.")
