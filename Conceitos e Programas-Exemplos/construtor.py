# Construtor
# Inicializar os nosso atributos

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa("João", 20)
print(p1.nome)
print(p1.idade)

p2 = Pessoa("Maria", 35)
print(p2.nome)
print(p2.idade)