alunos = [('Plautz', 9), ('Gabriela', 10), ('Linda', 8)]

alunos.sort(key=lambda aluno: aluno[1])

print(alunos)


def por_nome(aluno):
    return aluno[0]


print(sorted(alunos, key=por_nome))
