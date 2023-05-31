import json
from dataclasses import dataclass

@dataclass
class Livro:
    nome:           str
    autor:          str
    anoLancamento:  int
    disponivel:     bool

def criar_livro(nome, autor, ano, disponivel):
    livro = Livro(nome, autor, ano, disponivel)
    return livro

def salvar_livros(livros, caminho):
    with open(caminho, "w+", encoding="utf8") as arquivo:
        try:
            arquivo.write(json.dumps([livro.__dict__ for livro in livros]))
        except Exception as error:
            print(error)
