# """
# Construa um função de ordenação que ordene os alunos por nota.
# Se houver empate em nota, o nome deverá definir a ordem
#
# >>> alunos = [('Jorge', 5), ('Rafaela', 9), ('linda', 9), ('Gabriela', 9)]
# >>> alunos.sort(key=ordenar_por_nota_e_nome())
# >>> alunos
# [('Jorge', 5), ('Gabriela', 9), ('linda', 9), ('Rafaela', 9)]
# """
alunos = [('Jorge', 5), ('Rafaela', 9), ('linda', 9), ('Gabriela', 9)]

alunos.sort(key=lambda aluno: aluno[1])

print(alunos)
alunos.sort(key=lambda aluno: aluno[0])

print(alunos)
