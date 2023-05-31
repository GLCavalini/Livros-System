from labelsFunctions import masterMenu

from classPage import criar_livro, salvar_livros

options = 0
biblioteca = []
masterMenu()


while options != 5:
    try:
        options = int(input("O que você deseja fazer? "))
        if options not in range(1, 5):
            raise ValueError
    except ValueError:
        print('')
        print("Por favor, digite um número inteiro válido entre 1 e 6!")
        continue

    #VALIDATIONS
    match options:
        case 1:
            nome = input("Digite o nome do livro: ")
            autor = input("Digite o nome do autor: ")
            ano = int(input("Digite o ano de lançamento: "))
            disponivel = input("O livro está disponível? (Digite True ou False): ").lower() == "true"

            livro = criar_livro(nome, autor, ano, disponivel)
            biblioteca.append(livro)
        case 2:
            ...
        case 3:
            ...
        case 4:
            ...
        case 5:
            print('')
            break

# Salvar a biblioteca em um arquivo
caminho_arquivo = "livros.json"
salvar_livros(biblioteca, caminho_arquivo)

print("Obrigado por usar a Libery-Cadi! ")
print('')
