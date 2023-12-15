#sistema.py
lista_de_alunos = []

def adicionar_aluno():
    nome = str(input("Digite seu Nome: "))
    cpf = str(input("Digite seu CPF: "))
    turma = str(input("Digite seu Turma: "))
    notas = []
    for i in range(4):
        nota = float(input("Digite uma nota: "))
        notas.append(nota)
    
    aluno = {
        "Nome" : nome,
        "CPF": cpf,
        "Turma": turma,
        "Notas": notas
    }

    lista_de_alunos.append(aluno)
    print("Aluno cadastrado com sucesso")


def visualizar_alunos():
    for aluno_atual in lista_de_alunos:
        print(f"""
        Nome do aluno: {aluno_atual["Nome"]}
        CPF do aluno: {aluno_atual["CPF"]}
        Turma do aluno: {aluno_atual["Turma"]}
        Notas do aluno: {aluno_atual["Notas"]}
""")  
        
def deletar_aluno():
    visualizar_alunos()
    escolha = str(input("Digite o cpf do aluno que você quer deletar:"))
    for aluno_atual in lista_de_alunos:
        if aluno_atual["CPF"] == escolha:
            posicao_na_lista = lista_de_alunos.index(aluno_atual)
            lista_de_alunos.pop(posicao_na_lista)
    print("Aluno excluído com sucesso")
    
def menu_interface():
        menu = int(input("""
    Escolha uma opção
    1 - Adicionar Aluno
    2 - Visualizar alunos cadastrados
    3 - Deletar Aluno
    0 - Sair
"""))
        return menu