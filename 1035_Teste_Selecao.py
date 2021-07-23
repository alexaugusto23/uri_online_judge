"""

Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior do que A, e a soma de C com D for maior que a soma de A e B e se C e D, ambos, forem positivos e se a variável A for par escrever a mensagem "Valores aceitos", senão escrever "Valores nao aceitos".

Entrada
Quatro números inteiros A, B, C e D.

Saída
Mostre a respectiva mensagem após a validação dos valores.

Exemplo de Entrada:
5 6 7 8
2 3 2 6

Exemplo de Saída:

Valores nao aceitos
Valores aceitos

"""
## Code: ##

[A,B,C,D] = map(int,input().split())

soma_C_D = C + D
soma_A_B = A + B

if B > C and D > A and soma_C_D > soma_A_B and C >= 0 and D >= 0 and (A % 2) == 0:
    print(f"Valores aceitos")
else: 
    print(f"Valores nao aceitos")
