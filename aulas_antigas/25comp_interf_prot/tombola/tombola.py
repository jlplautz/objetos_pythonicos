from random import shuffle


class Tombola():
    def __init__(self):
        self.itens = []

    def carregada(self):
        # no caso dos container (lista) se
        # transformar em um booleano a logica é a seguinte
        # se itens não tem elemento retorna False caso controrio retorna True
        return bool(self.itens)

    def carregar(self, lista):
        self.itens = lista

    def misturar(self):
        # para misturar usar o metodo shuffle
        shuffle(self.itens)

    def sortear(self):
        # metodo pop retorna o ultimo elemento
        return self.itens.pop()
