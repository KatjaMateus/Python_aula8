nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + (nota3*2))/4

if media >= 6:
    print(f"Sua média é {media:.1f}, e você está aprovado.")
else:
    print(f"Sua média é {media:.1f}, e você está reprovado.")