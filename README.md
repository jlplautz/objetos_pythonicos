# objetos_pythonicos
Estudo de objetos pythonicos- segundo orientação do Python Pro

Procedimento 

<b>1- criar o ambiente virtual para o projeto</b>
objetos_pythonicos $ pipenv shell
(objetos_pythonicos) objetos_pythonicos $ pyenv local 3.8.0
(objetos_pythonicos) objetos_pythonicos $ deactivate
objetos_pythonicos $ pipenv install --dev flake8

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