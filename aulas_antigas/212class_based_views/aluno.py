import functools


@functools.total_ordering
class Aluno:

    def __init__(self, nota):
        self.nota = nota

    # para definir o que é igualdade
    def __eq__(self, other):
        return self.nota == other.nota

    def __gt__(self, other):
        return self.nota > other.nota


if __name__ == '__main__':
    aluno_nota_10 = Aluno(10)
    outro_aluno_nota_10 = Aluno(10)
    aluno_nota_1 = Aluno(1)
    # igualdade semantica (==) compara os IDs dos objetos
    print(aluno_nota_10 == outro_aluno_nota_10)
    print(aluno_nota_10 == aluno_nota_1)
    print(aluno_nota_10 > outro_aluno_nota_10)
    print(aluno_nota_10 > aluno_nota_1)
    print(aluno_nota_10 >= aluno_nota_1)
    print(aluno_nota_10 <= aluno_nota_1)
