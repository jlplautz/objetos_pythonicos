from time import sleep, strftime

from decorator import getfullargspec, decorator


@decorator
def logar(f, fmt='%H:%M:%S', *args, **kwargs):
    print(strftime(fmt))
    return f(*args, **kwargs)


@logar()
def mochileiro():
    return 42


@logar(fmt='%d/%m/%Y %H:%M:%S')
def ola(nome):
    return f'Olá {nome}'


if __name__ == '__main__':
    print(getfullargspec(ola))
    print(mochileiro())
    print(mochileiro.__name__)
    print(ola('Plautz'))
    print(ola.__name__)
    sleep(1)
    print(mochileiro())
    print(ola('Linda'))
