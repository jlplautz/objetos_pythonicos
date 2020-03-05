alunos = [('Plautz', 9), ('Gabriela', 10), ('Linda', 8)]

# filtragem
# print([(nome, nota) for nome, nota in alunos if nota > 8])
# mapeamento


print([nome for nome, nota in alunos if nota > 8])


def nota_maior_que_8(aluno):
    # _, nao estamos interesssado no nome
    _, nota = aluno
    return nota > 8


# nao esquecer que estamos passado a funnção como parametro sem os ()
# segundp elemento que será o iteravel que queremos aplicar esta regra
print(list(filter(nota_maior_que_8, alunos)))


def extrair_nome(aluno):
    nome, _ = aluno
    return nome


print(list(map(extrair_nome, filter(nota_maior_que_8, alunos))))
