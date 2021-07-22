"""
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.

Exemplo de Entrada:	
576
11257
503

Exemplo de Saída:

576
5 nota(s) de R$ 100,00
1 nota(s) de R$ 50,00
1 nota(s) de R$ 20,00
0 nota(s) de R$ 10,00
1 nota(s) de R$ 5,00
0 nota(s) de R$ 2,00
1 nota(s) de R$ 1,00

11257
112 nota(s) de R$ 100,00
1 nota(s) de R$ 50,00
0 nota(s) de R$ 20,00
0 nota(s) de R$ 10,00
1 nota(s) de R$ 5,00
1 nota(s) de R$ 2,00
0 nota(s) de R$ 1,00

503
5 nota(s) de R$ 100,00
0 nota(s) de R$ 50,00
0 nota(s) de R$ 20,00
0 nota(s) de R$ 10,00
0 nota(s) de R$ 5,00
1 nota(s) de R$ 2,00
1 nota(s) de R$ 1,00
"""
## Code: ##

################### OPÇÂO 01

valor = int(input())
cedulas = [100,50,20,10,5,2,1]

print(valor)
for cedula in cedulas:
    qtd_cedulas = int(valor/cedula)
    print(f"{qtd_cedulas} nota(s) de R$ {cedula},00")
    valor -= qtd_cedulas * cedula

################### OPÇÂO 02

valor = int(input())
                       # 576             
nt100 = valor//100 # 576/100=5.76 576//100=5 // (Divisão inteira, retira a parte decimal).
resto = valor%100  # 576%100=76 % traz o rosto da divisão.

nt50 = resto//50   # 76/50=1.52 76//50=1
resto = resto%50   # 76%50 = 26

nt20 = resto//20   # 26/20=1.3 26//20=1
resto = resto%20   # 26%20 = 6

nt10 = resto//10   # 6/10=0.6 6//10=0
resto = resto%10   # 0%10=0

nt5 = resto//5     # 6/5=1.2 6//5=1  
resto = resto%5    # 6%5=1

nt2 = resto//2     # 1/2=0.5 1//2=0
resto = resto%2    # 0%2=0

nt1 = resto//1     # 1/1=1 1//1=1
resto = resto%1    # 1%1 = 0

print(f"{nt100} nota(s) de R$ 100,00")
print(f"{nt50} nota(s) de R$ 50,00")
print(f"{nt20} nota(s) de R$ 20,00")
print(f"{nt10} nota(s) de R$ 10,00")
print(f"{nt5} nota(s) de R$ 5,00")
print(f"{nt2} nota(s) de R$ 2,00")
print(f"{nt1} nota(s) de R$ 1,00")











