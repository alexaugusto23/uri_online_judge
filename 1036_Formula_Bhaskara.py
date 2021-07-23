"""

Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.

Entrada
Leia três valores de ponto flutuante (double) A, B e C.

Saída
Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular". Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto, com uma mensagem correspondente conforme exemplo abaixo. Imprima sempre o final de linha após cada mensagem.

Exemplos de Entrada:
10.0 20.1 5.1
0.0 20.0 5.0
10.3 203.0 5.0
10.0 3.0 5.0

Exemplos de Saída:

R1 = -0.29788
R2 = -1.71212

Impossivel calcular

R1 = -0.02466
R2 = -19.68408

Impossivel calcular

"""
## Code: ##

from math import sqrt

A,B,C = list(map(float, input().split()))

# Fórmula de Bhaskara

def bhaskara(A,B,C):
    try:
        x1 = (-B + sqrt(B**2 - 4 * A * C)) / (2 * A)
        x2 = (-B - sqrt(B**2 - 4 * A * C)) / (2 * A)
        return f"R1 = {x1:.5f}\nR2 = {x2:.5f}"

    except ZeroDivisionError: 
        return f"Impossivel calcular"
    except ValueError: return f"Impossivel calcular"
print(bhaskara(A,B,C))