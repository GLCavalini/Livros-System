def menuDefault():
        print("")
        print("Bem vindo a Libery-Cady - Livros sempre transformando o futuro!  ")
    


def masterMenu(bool=False):
    if(bool == True):
        menuDefault()
        print('''    
            [1] - Cadastrar Livro  
            [2] - Listar Livros
            [3] - Editar Livros
            [4] - Gerar Relatórios
            [5] - Sair
        ''')
    else:
        print('''    
            [1] - Cadastrar Livro  
            [2] - Listar Livros
            [3] - Editar Livros
            [4] - Gerar Relatórios
            [5] - Sair
        ''')
         

def returnPositiveMessage():
    print("")
    print("Livro cadastrado com sucesso na Libery-Cady!  ")