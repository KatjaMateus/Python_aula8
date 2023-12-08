def visualizar_alunos():
    for aluno in cadastro:
            print(f"""
            Nome : {aluno['nome']}
            CPF : {aluno['cpf']}
            Turma : {aluno['turma']}
            Nota 1 : {aluno['notas'][0]}
            Nota 2 : {aluno['notas'][1]}
            Nota 3 : {aluno['notas'][2]}
            Nota 4 : {aluno['notas'][3]}
            """)

cadastro = []
print("""Digite o nome do aluno, CPF, turma e 4 notas.""")

while True:
    escolha = int(input("""
    1 - Cadastrar aluno
    2 - Visualizar alunos cadastrados
    3 - Deletar aluno
    0 - Sair
     """))
    if escolha == 1:
        nome = input("Nome do aluno: ").upper().strip()
        cpf = int(input("Digite CPF: "))
        turma = input("Digite a identificação da turma: ")
        for i in range(4):
            notas = float(input("Digite a nota: "))

        cadastro.append({
            "nome": nome,
            "cpf": cpf,
            "turma": turma,
            "notas": [notas]
            })
    elif escolha == 2:
        visualizar_alunos()
    elif escolha == 3:
        visualizar_alunos()
        deletar = input("Digite o nome do cpf a deletar: ")
        deletar.delete()
    elif escolha == 0:
        break
    else:
        print("Opção inválida")