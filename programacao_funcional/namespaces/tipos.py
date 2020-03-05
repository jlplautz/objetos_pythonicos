# contexto global no nivel de modulo ou contexto de modulo
a = 5


# existe tambem contexto local qdo criamos um função (escopo local desta função
def f(a=3):
    b = 3
    print(globals())
    print(locals())
    print(a)
    print(b)


class A:
    a = 8
    print(a)
    print(globals())
    print(locals())


# f()
