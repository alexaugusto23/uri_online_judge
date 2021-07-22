"""

Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:

MaiorAB = (a+b+abs(a-b))/2

Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".

Exemplos de Entrada:	
7 14 106
217 14 6

Exemplos de Saída:
106 eh o maior
217 eh o maior


"""
## Code: ##

valores = list(input().split())

def o_maior(valores):
    A = int(valores[0])
    B = int(valores[1])
    C = int(valores[2])
    maior = int((A+B+abs(A-B))/2)
    if maior < C:
        maior = int((maior+C+abs(maior-C))/2)
    return f"{maior} eh o maior" 
print(o_maior(valores))

[A, B, C] = list(input().split())
A, B, C = int(A), int(B), int(C)
def o_maior_dois(A, B, C):
    maior = max(A,B,C)
    return f"{maior} eh o maior" 
print(o_maior_dois(A, B, C))

[A, B, C] = list(map(int,list(input().split())))
def o_maior_dois(A, B, C):
    maior = max(A,B,C)
    return f"{maior} eh o maior" 
print(o_maior_dois(A, B, C))