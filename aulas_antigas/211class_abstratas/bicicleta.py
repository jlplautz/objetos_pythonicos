import abc


class Bicicleta:
    _marca = 'Caloi'

    def __init__(self):
        self._velocidade = 0

    @classmethod
    def marca(cls):
        return cls._marca

    @staticmethod
    def rodas():
        return 2

    @property
    def velocidade(self):
        return self._velocidade

    @velocidade.setter
    def velocidade(self, valor):
        if valor >= 0:
            self._velocidade = valor
        else:
            self._velocidade = 0

    @abc.abstractmethod
    def pedalar(self):
        """Cada classe concreta deve definir o metodo pedalar com seu
        incrementa na velocidade"""

    @abc.abstractmethod
    def frear(self):
        """Cada classe concreta deve definir o metodo frear com seu
                decremento na velocidade"""


class Monark(Bicicleta):
    _marca = 'Monark'

    def pedalar(self):
        # metodo da instancia bicicleta pois tem o self
        self.velocidade += 10

    def frear(self):
        self.velocidade -= 3


if __name__ == '__main__':
    bicicleta = Bicicleta()
    print(Bicicleta.marca())
    bicicleta.pedalar()
    bicicleta.frear()
    bicicleta.frear()
    bicicleta.frear()
    bicicleta.frear()
    bicicleta.velocidade = -4
    print(bicicleta.velocidade)
    print(Monark.marca())
    print(Monark.rodas(), 'rodas')
