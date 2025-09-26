# revisao_1_ex22.py
n = int(input("Digite um número de 1 a 12: "))
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
if 1 <= n <= 12:
    print("Mês correspondente:", meses[n - 1])
else:
    print("Número inválido")
