# FAÇA UM PROGRAMA DE SORTEIO DE CLIENTES ONDE O PROGRAMA VAI CADASTRANDO CLIENTES ATÉ O PROPRIO USUÁRIO DECIDIR QUE QUER PARAR(LOOP INFINITO)
# OS DADOS PARA CADASTRO SÃO: nome, cpf, valor_compra
# QUANDO O USUÁRIO ENCERRAR O LOOP FAÇA UM SORTEIO ENTRE TODOS OS CLIENTES CADASTRADOS E MOSTRE NA TELA TODOS OS DADOS DO CLIENTE QUE FOI SELECIONADO COM UMA MENSAGEM CUSTOMIZADA TIPO:
# """Parabéns {nome do cliente}, cpf: {cpf do cliente} você foi o sorteado por ter feito uma compra no valor de {valor da compra do cliente}"""

cadastro = []
from random import choice
print("""Digite o nome do cliente, CPF e o valor da compra.""")

while True:
    escolha = int(input("""
    1 - Continuar
    2 - Sair
     """))
    if escolha == 2:
        break
    nome = input("Nome do cliente: ").upper().strip()
    
    cpf = int(input("Digite CPF: "))
    valor = float(input("Valor da compra R$: "))

    cadastro.append({
        "nome": nome,
        "cpf": cpf,
        "valor_compra": valor
        })
    

sorteado = choice(cadastro)

print(sorteado)

print(f"Parabéns {sorteado['nome']}, cpf {sorteado['cpf']} você foi o sorteado por ter feito uma compra no valor de {sorteado['valor_compra']}")