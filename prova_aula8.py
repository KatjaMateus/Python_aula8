carrinho = []
compra1={
    "produto": "camiseta", 
    "valor": 12.60, 
    "quantidade" : 3 
    }
carrinho.append(compra1)

compra2={
    "produto" : "meias",
    "valor" : 5.50,
    "quantidade" : 5
    }
carrinho.append(compra2)

def ver_lista(carrinho):
    for compra in carrinho:
        return("produto:", compra["produto"], 
            "valor:", compra["valor"], 
            "quantidade:", compra["quantidade"], 
            "valor total:", compra["valor"]*compra["quantidade"])
    print(ver_lista(carrinho))

def adicionar(compra):
    compra= {"produto": str(input("Digite nome do produto: ")),
            "valor": float(input("Digite o valor do produto: ")),
            "quantidade": int(input("Digite a quantidade que quer comprar: "))}
    carrinho.append(compra)
    print(ver_lista(carrinho))


def remover(compra):
    chave_procurar=("nome")
    valor_procurar=("Digite o nome do produto que quer remover: ")
    for compra in carrinho:
        if compra.get(chave_procurar)==valor_procurar:
            carrinho.remove(compra)
            break
    print(ver_lista(carrinho))

def atualizar(compra):
    chave_procurar=("nome")
    valor_procurar=("Digite o nome do produto que quer atualizar: ")
    for compra in carrinho:
        if compra.get(chave_procurar)==valor_procurar:
            print(compra)
            compra["nome"]=str(input("Atualize o nome do produto: "))
            compra["valor"]=float(input("Atualize o valor do produto: "))
            compra["quantidade"]=int(input("Atualize a quantidade do produto: "))
    print(ver_lista(carrinho))


while True:
    escolha = int(input("""
        Escolha uma opção:
        1 = ver a lista de produtos
        2 = adicionar produtos
        3 = remover produtos
        4 = atualizar a lista de produtos
        5 = sair
                    
      """))
    
    if escolha == 1:
        print(ver_lista(carrinho))
    elif escolha == 2:
        print(adicionar("compra"))
    elif escolha == 3:
        print(remover("compra"))
    elif escolha == 4:
        print(atualizar("compra"))
    elif escolha == 5:
        print("Programa encerrado")
        break
else:
    print("opção inválida")