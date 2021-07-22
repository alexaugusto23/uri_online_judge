"""
Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno. A seguir, calcule a média do aluno, sabendo que a nota A tem peso 2, a nota B tem peso 3 e a nota C tem peso 5. Considere que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

Entrada
O arquivo de entrada contém 3 valores com uma casa decimal, de dupla precisão (double).

Saída
Imprima a mensagem "MEDIA" e a média do aluno conforme exemplo abaixo, com 1 dígito após o ponto decimal e com um espaço em branco antes e depois da igualdade. Assim como todos os problemas, não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".

Exemplos de Entrada:

5.0
6.0
7.0

5.0
10.0
10.0

10.0
10.0
5.0

Exemplos de Saída:


MEDIA = 6.3

MEDIA = 9.0

MEDIA = 7.5

"""

## Code: ##

try:
    a, b, c = float(input()), float(input()), float(input())
except:
    raise ValueError("Diferente de float")

def media(a: float, b: float, c: float, p1: float = 2, p2: float = 3, p3: float = 5) -> float:
    pesos = p1 + p2 + p3
    media = ((a * p1) + (b * p2) + (c * p3)) / pesos
    return f"MEDIA = {media:.1f}"

print(media(a,b,c))