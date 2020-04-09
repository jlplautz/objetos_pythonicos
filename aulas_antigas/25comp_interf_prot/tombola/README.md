# TDD da Tombola

Uma tombola pode ser criada da seguinte maneira:
```Python
    >>> from tombola import tombola
    >>> t = tombola.Tombola()
   
```

Apos a criação os itens da tombola são representados por uma lista vazia
```Python
    >>> t.itens
    []

```

uma lista recem criada não possui elementos. Portanto o metodo 'carregada"
retorna false:
```python
    >>> t.carregada()
    False

```

É possivel carregar itens atraves do metodo "carregar"
```Python
    >>> t.carregar([1,2])
    >>> t.itens
    [1, 2]

```

Apos ser carregada  o metodo 'carregada" retorna verdadeiro:
```python
    >>> t.carregada()
    True

```

Uma tombola pode mistruar seus itens
```python
    >>> def embaralhador_mock(lista):
    ...     lista[0], lista[-1] = lista[-1], lista[0]
    >>> tombola.shuffle = embaralhador_mock
    >>> t.itens
    [1, 2]
    >>> t.misturar()
    >>> t.itens
    [2, 1]

```

uma tombola serve para sortear elementos
```python
    >>> t.sortear()
    1
    >>> t.carregada()
    True
    >>> t.sortear()
    2
    >>> t.carregada()
    False

```