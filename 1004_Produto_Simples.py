"""
Leia dois valores inteiros. A seguir, calcule o produto entre estes dois valores e atribua esta operação à variável PROD. A seguir mostre a variável PROD com mensagem correspondente.   

Entrada
O arquivo de entrada contém 2 valores inteiros.

Saída
Imprima a mensagem "PROD" e a variável PROD conforme exemplo abaixo, com um espaço em branco antes e depois da igualdade. Não esqueça de imprimir o fim de linha após o produto, caso contrário seu programa apresentará a mensagem: “Presentation Error”.

Exemplos de Entrada:

3
9

-30
10

0
9


Exemplos de Saída:

PROD = 27

PROD = -300

PROD = 0

"""

## Code: ##

a, b = int(input()), int(input())

def prod(a, b):
    soma = int(a) * int(b)
    return f"PROD = {soma}"

print(prod(a,b))

