# Python Day 1 

modo de depuração: se conecta a execução do codigo.


install poetry 
install python


identação é o espaçao entre as hieraquias - tab 

muitas biliotecas 

poetry init 


cat - verifica o conteudo dentro do script 

executar script python3 + nome do script

variaveis de ambientes

forma vanila : mkdir project-vanilla 
cd projecto vanilla

python3 -m venv _ modulo vanilla - ele vai criar uma pasta chamada virtual_env 


ls -la

./virtual_env/lib


activate
deactivate


como criar grupos de dependencias : 

poetry add --group dev pytest

cat pyproject.toml 

Variaveis sempre em letras minusculas separadas por underscor

Funçoes sao definições de variaveis, funções retornam coisas
letras minusculas


Definiçao ou atribuição: 


`````python

def func(a: str) -> str:
    return "b"


list_a: list[str] = ["a", "b"]

Declarar um dicionario: coloca as chaves

dict_a = {
    "KeyA": "ValueB"
    "KeyA": "ValueB"
}

dict_b = {
    1: "a"
    2: "b",
}
`````

linter sao helpers sao instalados como biblioteca : 
