#main.py
from sistema import *

while True:
    menu = menu_interface()
    
    match menu:
        case 1:
            adicionar_aluno()
        case 2:
            visualizar_alunos()
        case 3:
            deletar_aluno()
        case 0:
            break
        case _:
            print("Opção Inválida")