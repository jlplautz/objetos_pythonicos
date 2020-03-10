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
<b>1.1.5- Função como Argumento </b>
```
Então esta caracterista que a função é um cidadão de primeira classe e podemos passar com argumento 
é utilizada em varias bibliotecas embotidas no python
```
<b>1.1.6- Ordenação </b>
```
A classe list do python possui um metodo de alta ordem que recebe como parametro Key uma função 
na qual você pode determinar o criterio de ordenação. Esta função vai receber cada um dos elementos 
da lista e retornar um valor que seja ordenavel indicando o criterio de ordenação

alunos = [('Plautz', 9), ('Gabriela', 10), ('Linda', 8)]
alunos.sort(key=lambda aluno: aluno[1])
print(alunos)

A função sorted() vai criar uma segunda lista baseado neste iteravel. 
E esta segunda lista estará ordenada.
- vamos passar a lista de alunos e
- tambem esta função sorted() tem o parametro Key que pode receber uma função como parametro.

def por_nome(aluno):
    return aluno[0]
print(sorted(alunos, key=por_nome))
```
<b>1.1.7- Flitragem </b>

<b>Usando list comprehension</b>
```
print([]) => usando os colchetes (criação de listas), vamos mencionar o que desejamos no resultado.
print([ Vamos retornar a própria tupla (nome, nota) for nome, nota in alunos])  	
temos que lembrar que podemos colocar um condição boleana aqui no final se  for true o elemento será incluido na lista.
alunos = [('Plautz', 9), ('Gabriela', 10), ('Linda', 8)]
print([(nome, nota) for nome, nota in alunos if nota > 8])

Resultado => [('Plautz', 9), ('Gabriela', 10)]
```

<b>Filter() - versão funcional</b>
```
função de alta ordem ( que como primeiro parametro – recebe uma função que receberá cada um dos elementos 
de um iteravel que deve ser passado como segundo parametro
Escrevendo o codigo 
- imprimir
- transformar em lista o resultado que o filter vai retornar.
- escrever a função
def nota_maior_que_8(aluno):
    # _, nao estamos interesssado no nome
    _, nota = aluno
    return nota > 8
- nao esquecer que estamos passado a funnção como parametro sem os ()
  segundo elemento que será o iteravel que queremos aplicar esta regra
print(list(filter(nota_maior_que_8, alunos)))
```

<b>1.1.8- Mapeamento </b>
```
Trabalhando com a list comprehension e bem simples.
Caso desejarmos retornar somente o nome, não será necessario criar a tupla.
alunos = [('Plautz', 9), ('Gabriela', 10), ('Linda', 8)]
print([nome for nome, nota in alunos if nota > 8])

Resultado => ['Plautz', 'Gabriela']

Podemos usar o mapeamento junto com a filtragem na versão funcional 
  - como parametro iteravel desta segunda função podemos juntar a própria filtragem

def extrair_nome(aluno):
    nota, _ = aluno
    return nome
print(list(map(extrair_nome, filter(nota_maior_que_8, alunos))))

Resultado => ['Plautz', 'Gabriela']
```
<b>1.1.9- Módulo Operator </b>
```
operator.itemgetter  => vai construir uma função em tempo de execução, 
na qual possamos extrair um elemento em determinada posição de um iteravel

print(list(map(operator.itemgetter(0), filter(nota_maior_que_8, alunos))))

Resultado => ['Plautz', 'Gabriela']

Conclusão: 
Toda vez que você precisar usar uma função para fazer um mapeamento ou uma filtragem 
e como esta função já existe no python (operator), possivelemente podemos encontrar 
esta função já definida dentro do modulo operator
```

<b>1.2- Decorator </b>

<b>1.2.1- Função como Retorno de outra Função </b>
```
Portanto estamos criando função em tempo de execução. Cada vez que executamos 
fabrica_de_multiplicadores() estamos criando uma função dobro
 Por isso essa funçoes chamam factory, que servem para construi outros objetos ou outras funçoes.

dobro_externo = fabrica_de_multiplicadores()
dobro_externo2 = fabrica_de_multiplicadores()
print(dobro_externo is dobro_externo2)
print(dobro_externo(3))
Resultado:
False   <= print(dobro_externo is dobro_externo2)
6	    <= print(dobro_externo(3))

Conclusão:

- tudo o que podemos fazer com objeto do tipo int , string tambem podemos com objeto do tipo função.
- incluindo a sua criação em variavel local dentro de escopo de outras funçoes e retornar esta função 
  que foi criada neste escopo local como o resultado da execução de outra função 
```

<b>1.2.2- Closure </b>
```
Clausura (ciência da computação)
Em ciência da computação e na programação uma clausura (do inglês closure) é uma função que referencia variáveis livres 
no contexto léxico. Uma clausura ocorre normalmente quando uma função é declarada dentro do corpo de outra, e a função 
interior referencia variáveis locais da função exterior. Em tempo de execução, quando a função exterior é executada, 
então uma clausura é formada, que consiste do código da função interior e referências para quaisquer variáveis no 
âmbito da função exterior que a...

Closure => é o conjunto de valores existente no escopo da criação de uma função ao qual ela tambem tenha acesso.
```