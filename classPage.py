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
        returnPositiveMessage()
        with open(caminhoArquivo, "w+", encoding="utf8") as arquivo:
            try:
               arquivo.write(json.dumps([livro.__dict__ for livro in biblioteca], indent=4))
            except Exception as error:
                print(error)
        
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
