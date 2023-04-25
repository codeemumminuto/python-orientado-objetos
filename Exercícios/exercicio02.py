# Parte 6
# Exercício

'''
Crie um programa que defina a classe "Círculo"
com um construtor que recebe um parâmetro, 
o raio do círculo.
O programa deve criar duas instâncias da classe
"Círculo", "c1" e "c2", com diferentes valores
para o parâmetro raio.
Em seguida, o programa deve imprimir o raio e
a área de cada um dos círculos criados.
'''

# Deixa aí nos comentários

class Circulo:
    def __init__(self, raio):
        self.raio = raio
        self.area = raio*raio*3.14

print("Círculo 1:")
c1 = Circulo(3)
print(f"Raio: {c1.raio}\nÁrea: {c1.area}")

print("\nCírculo 2:")
c2 = Circulo(2.50)
print(f"Raio: {c2.raio}\nÁrea: {c2.area}")