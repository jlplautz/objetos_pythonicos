# objetos_pythonicos
Estudo de objetos pythonicos- segundo orientação do Python Pro

Procedimento 

<b>1- criar o ambiente virtual para o projeto</b>
```
objetos_pythonicos $ pipenv shell
(objetos_pythonicos) objetos_pythonicos $ pyenv local 3.8.0
(objetos_pythonicos) objetos_pythonicos $ deactivate
objetos_pythonicos $ pipenv install --dev flake8
```
<b>2- Criar o file .flake8 na raiz do projeto</b>
```
[flake8]
max-line-length = 120
exclude = .venv
```
<b>3- Criar file .pyup.yml</b>
```
requirements:
  - Pipfile
  - Pipfile.lock 
```
<b>3- Instalar pytest</b>
```
objetos_pythonicos $ pipenv install --dev pytest
```

<b>1.1.2- Namespaces </b>
```
- criar o python package 'namespaces' e python file 'namespace_global'
├── LICENSE
├── namespaces
│   ├── __init__.py
│   └── namespace_global.py
├── Pipfile
├── Pipfile.lock
└── README.md

O escopo global no python é limitado ao modulo.

Portanto não existe o escopo global no python. 
Que vai transbordar variaveis para todos os modulos que existam e sejam criados
Os argumentos de uma função pertence ao escopo local desta função.
```

<b>1.1.3- Função e Atributos </b>
```
 A função é um objeto como outro qualquer. 
 E portanto outras operações que fazemos com outros tipos de objetos (como string, numeros, etc), 
 podemos fazer com as funçoes.

dobro.__name__
'dobro'

dobro.__module__
'programacao_funcional.funcao_como_objeto.atributos'

dobro.__code__.co_code
b'|\x00d\x01\x14\x00S\x00'

from dis import dis
dis(dobro.__code__.co_code)
          0 LOAD_FAST                0 (0)
          2 LOAD_CONST               1 (1)
          4 BINARY_MULTIPLY
          6 RETURN_VALUE
```

<b>1.1.4- Função Anônima </b>
```
Função lambda,  => nada mais é do que uma função anômina
Toda função lambda sempre retorna uma valor e nem precisamos inserir o return, pois esta é a natureza.
```

