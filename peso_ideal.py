sexo = input("""Digite seu sexo: 
             M = mulher
             H = homem
             """)
altura = float(input("Qual é a sua altura? "))

if sexo == "H":
    peso = (72.7 * altura) - 58
    print(f"Seu peso ideal é {peso:.1f}")
elif sexo == "M":
    peso = (62.1 * altura) - 44.7
    print(f"Seu peso ideal é {peso:.1f}")