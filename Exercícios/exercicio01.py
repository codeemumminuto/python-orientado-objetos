# Parte 5
# Exercício

'''
Crie um programa que defina a classe "Carro" 
com um construtor que recebe dois parâmetros, 
a cor e a marca do carro.
O programa deve criar duas instâncias da classe
"Carro", "c1" e "c2", com diferentes valores
para os parâmetros cor e marca.
Em seguida, o programa deve imprimir a cor e
a marca de cada um dos carros criados.
'''

# Deixa aí nos comentários;

class Carro:
    def __init__(self, cor, marca):
        self.cor = cor
        self.marca = marca
    
c1 = Carro("Azul", "Ford")
print("Carro 1:")
print(f"Cor: {c1.cor}\nMarca: {c1.marca}")

print("\nCarro 2:")
c2 = Carro("Vermelho", "Chevrolet")
print(f"Cor: {c2.cor}\nMarca: {c2.marca}")