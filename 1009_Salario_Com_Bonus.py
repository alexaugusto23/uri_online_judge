"""

Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais.

Entrada
O arquivo de entrada contém um texto (primeiro nome do vendedor) e 2 valores de dupla precisão (double) com duas casas decimais, representando o salário fixo do vendedor e montante total das vendas efetuadas por este vendedor, respectivamente.

Saída
Imprima o total que o funcionário deverá receber, conforme exemplo fornecido.


Exemplos de Entrada:
JOAO
500.00
1230.30	

PEDRO
700.00
0.00

MANGOJATA
1700.00
1230.50

Exemplos de Saída:

TOTAL = R$ 684.54
TOTAL = R$ 700.00
TOTAL = R$ 1884.58

"""
## Code: ##

nome_vendedor, sal_fixo, total_vendas = str(input()), float(input()), float(input())

def calcula_salario_com_bonus(nome_vendedor, sal_fixo, total_vendas, comissao=15):
    comissao = comissao / 100
    comissão_valor = total_vendas * comissao 
    total = sal_fixo + comissão_valor
    return f"TOTAL = R$  {total:.2f}"

print(calcula_salario_com_bonus(nome_vendedor, sal_fixo, total_vendas))

