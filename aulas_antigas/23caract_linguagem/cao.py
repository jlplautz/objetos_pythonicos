class Mamifero:
    """
    vertebrado dotados de glandulas mamarias
    """


class Cao(Mamifero):
    # tem trez atributos de classe
    qt_patas = 4
    carnivoro = True
    nervoso = False

    def __init__(self, nome):
        self.nome = nome

    def latir(self, vezes=1):
        # quando nervoso, late o dobro
        vezes = vezes + (self.nervoso * vezes)
        print(self.nome + ':' + ' Au!' * vezes)

    def __str__(self):
        return self.nome

    def __repr__(self):
        return 'Cao({0!r})'.format(self.nome)

    def __eq__(self, outro):
        return (isinstance(outro, Cao) and
                self.__dict__ == outro.__dict__)


class Pequines(Cao):
    """
    o pequines esta normalmente nervoso
    """
    nervoso = True


class GrandeMixin:
    """Mixin: muda o latido"""
    def latir(self, vezes=1):
        # faz de conta que caes grandes nao mudam o seu latido qdo nervoso
        print(self.nome + ':' + 'Wuff!' * vezes)


class Mastiff(GrandeMixin, Cao):
    """
    o mastiff late diferente
    """


class SaoBernardo(GrandeMixin, Cao):
    """ O SaoBernardo serve conhaque"""

    def __init__(self, nome):
        Cao.__init__(self, nome)
        self.doses = 10

    def servir(self):
        if self.doses == 0:
            raise ValueError('Acabou o conhaque')
        self.doses -= 1
        msg = '{0} serve o conhaque (restam {1} doses)'
        print(msg.format(self.nome, self.doses))
