from programacao_funcional.decorator.registrador import marcar, get_marcadas


def primeira():
    pass


primeira = marcar(primeira)


@marcar
def segunda():
    pass


if __name__ == '__main__':
    for f in get_marcadas():
        print(f.__name__)
    primeira
    segunda
