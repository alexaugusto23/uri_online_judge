"""
Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).

Entrada
O arquivo de entrada contém 4 valores inteiros.

Saída
Imprima a mensagem DIFERENCA com todas as letras maiúsculas, conforme exemplo abaixo, com um espaço em branco antes e depois da igualdade.

Exemplos de Entrada:
5
6
7
8

Exemplos de Saída:
DIFERENCA = -26

"""
## Code: ##


try:
    A,B,C,D = int(input()), int(input()), int(input()), int(input())
except:
    raise ValueError("Valor incorreto")

def diferenca(A,B,C,D):
    diferenca = (A*B - C*D)
    return f"DIFERENCA = {diferenca}"

print(diferenca(A,B,C,D))

