from labelsFunctions import masterMenu

from classPage import Livro

options = 0
masterMenu(True)


while options != 5:
    try:
        options = int(input("O que você deseja fazer? "))
        if options not in range(1, 5):
            raise ValueError
    except ValueError:
        print('')
        print("Por favor, digite um número inteiro válido entre 1 e 5!")
        continue

    #VALIDATIONS
    match options:
        case 1:
            nome = input("Digite o nome do livro: ")
            autor = input("Digite o nome do autor: ")
            ano = int(input("Digite o ano de lançamento: "))
            disponivel = input("O livro está disponível? (Digite True ou False): ").lower() == "true"
            
            if (nome, autor, ano, disponivel != ''):
                Livro.criar_livro(nome, autor, ano, disponivel)
                masterMenu()
            else:
                print("Preencha todos os campos para a criação de um livro.")
        case 2:
            Livro.ler_livros()
            masterMenu()
        case 3:
            nome = input("Digite o nome do livro que deseja editar: ")
            if Livro.verificar_livro_existente(nome):
                novo_nome = input("Digite o novo nome do livro: ")
                novo_autor = input("Digite o novo nome do autor: ")
                novo_ano = int(input("Digite o novo ano de lançamento: "))
                nova_disponibilidade = input("Digite a nova disponibilidade! (Digite True ou False): ").lower() == "true"
                Livro.editar_livro(nome, novo_nome, novo_autor, novo_ano, nova_disponibilidade)
                masterMenu()
            else:
                print("O livro não foi encontrado na biblioteca.")
                masterMenu()
        case 4:
            Livro.gerador_relatorio()
            masterMenu()
        case 5:
            print('')
            break

print("Obrigado por usar a Libery-Cadi! ")
print('')
