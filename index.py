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
            ...
        case 4:
            ...
        case 5:
            print('')
            break

print("Obrigado por usar a Libery-Cadi! ")
print('')
