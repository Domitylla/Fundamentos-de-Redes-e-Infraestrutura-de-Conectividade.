
class Livro:
    def __init__(self, nome, autor, editora, paginas):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas

    def alterar_editora(self, nova_editora):
        self.editora = nova_editora

    def listar_qtde_paginas(self):
        return self.paginas

# Teste
l = Livro("1984", "George Orwell", "Companhia", 300)
assert l.listar_qtde_paginas() == 300
l.alterar_editora("Penguin")
assert l.editora == "Penguin"
