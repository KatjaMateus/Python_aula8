salario = float(input("Quanto é o seu salario mensal? "))
prestacao = float(input("Quanto é o valor da prestação do empréstimo? "))
valor_do_salario = (prestacao/salario)*100
if valor_do_salario > 20:
    print("Empréstimo não concedido")
else:
    print("Empréstimo concedido")