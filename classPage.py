import json
from dataclasses import dataclass
from labelsFunctions import returnPositiveMessage

biblioteca = []
caminhoArquivo = "livros.json"

@dataclass
class Livro:
    nome:           str
    autor:          str
    anoLancamento:  int
    disponivel:     bool

    @staticmethod
    def criar_livro(nome, autor, ano, disponivel):
        livro = Livro(nome, autor, ano, disponivel)
        biblioteca.append(livro)
        returnPositiveMessage(True)
        with open(caminhoArquivo, "w+", encoding="utf8") as arquivo:
            try:
               arquivo.write(json.dumps([livro.__dict__ for livro in biblioteca], indent=4))
            except Exception as error:
                print(error)

    @staticmethod
    def verificar_livro_existente(nome):
        for livro in biblioteca:
            if livro.nome == nome:
                return True
        return False
        
    @staticmethod
    def ler_livros():
        if (biblioteca):
            for livro in biblioteca:
                print("Nome do Livro: ", livro.nome)
                print("Nome do autor: ", livro.autor)
                print("Ano de Lançamento: ", livro.anoLancamento)
                print("Disponibilidade de compra: ", livro.disponivel)
                print("")
        else:
            ("Não temos livros cadastrados no momento!")

    @staticmethod
    def editar_livro(nome, novo_nome, novo_autor, novo_ano, nova_disponibilidade):
        for livro in biblioteca:
            if livro.nome == nome:
                livro.nome = novo_nome
                livro.autor = novo_autor
                livro.anoLancamento = novo_ano
                livro.disponivel = nova_disponibilidade
                returnPositiveMessage()
                with open(caminhoArquivo, "w+", encoding="utf8") as arquivo:
                    try:
                        arquivo.write(json.dumps([livro.__dict__ for livro in biblioteca], indent=4))
                    except Exception as error:
                        print(error)
                return
