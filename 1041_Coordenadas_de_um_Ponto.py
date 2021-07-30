"""

Leia 2 valores com uma casa decimal (x e y), que devem representar as coordenadas de um ponto em um plano. A seguir, determine qual o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos cartesianos ou na origem (x = y = 0).

        Y
  Q2   |   Q1
       |
_______|________X
       |
       |
  Q3   |   Q4

Se o ponto estiver na origem, escreva a mensagem “Origem”.

Se o ponto estiver sobre um dos eixos escreva “Eixo X” ou “Eixo Y”, conforme for a situação.

Entrada
A entrada contem as coordenadas de um ponto.

Saída
A saída deve apresentar o quadrante em que o ponto se encontra.

Exemplo de Entrada:	

4.5 -2.2
0.1 0.1
0.0 0.0

Exemplo de Saída:

Q4
Q1
Origem

"""
## Code: ##

def coordenadas_ponto(x: float, y: float) -> str:
    # Origem 
    if x == 0.0:
        if y == 0:
            return'Origem'
        if y != 0:
            return'Eixo Y'
    if y == 0:
        if x != 0:
            return'Eixo X'

    # Q1
    elif x > 0.0 and y > 0:
        return f"Q1"
    # Q2
    elif x < 0.0 and y > 0:
        return f"Q2"
    # Q3
    elif x < 0.0 and y < 0:
        return f"Q3"
    # Q4
    elif x > 0.0 and y < 0:
        return f"Q4"

x, y = map(float, input().split())
print(coordenadas_ponto(x, y))