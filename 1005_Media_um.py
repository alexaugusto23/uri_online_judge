"""
Leia 2 valores de ponto flutuante de dupla precisão A e B, que correspondem a 2 notas de um aluno. A seguir, calcule a média do aluno, sabendo que a nota A tem peso 3.5 e a nota B tem peso 7.5 (A soma dos pesos portanto é 11). Assuma que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

Entrada
O arquivo de entrada contém 2 valores com uma casa decimal cada um.

Saída
Imprima a mensagem "MEDIA" e a média do aluno conforme exemplo abaixo, com 5 dígitos após o ponto decimal e com um espaço em branco antes e depois da igualdade. Utilize variáveis de dupla precisão (double) e como todos os problemas, não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".

Exemplos de Entrada:
5.0
7.1

0.0
7.1

10.0
10.0

Exemplos de Saída:

MEDIA = 6.43182

MEDIA = 4.84091

MEDIA = 10.00000

"""
## Code: ##

# Mp = [(N1 x P1) + (N2 x P2) + (N3 x P3) + ... (Nx x Px)] ÷ (P1 + P2 + P3 + ... Px).

try:
    a, b = float(input()), float(input())
except:
    raise ValueError("Diferente de float")

def media(a: float, b: float, p1: float = 3.5, p2: float = 7.5) -> float:
    pesos = p1 + p2
    media = ((a * p1) + (b * p2)) / pesos
    return f"MEDIA = {media:.5f}"

print(media(a,b))