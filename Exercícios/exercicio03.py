# Parte 7
# Exercício

'''
Crie um programa que defina a classe "Aluno"
com um construtor que recebe três parâmetros,
o nome, a idade e a nota do aluno. 
O programa deve criar duas instâncias da classe 
"Aluno", "a1" e "a2", com diferentes valores para
os parâmetros nome, idade e nota. 
Em seguida, o programa deve imprimir o nome,
a idade e a nota de cada um dos alunos criados.
E por último, calcular e imprimir a média das 
notas dos dois alunos criados.
'''

# Deixa nos comentários

class Aluno:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota

print("Aluno 1:")
a1 = Aluno("João", 25, 7.5)
print(f"Nome: {a1.nome}\nIdade: {a1.idade}\nNota: {a1.nota}")

print("\nAluno 2:")
a2 = Aluno("Maria", 19, 6.3)
print(f"Nome: {a2.nome}\nIdade: {a2.idade}\nNota: {a2.nota}")

print("\nMédia:")
media = (a1.nota + a2.nota) / 2
print(f"A média é {media}")