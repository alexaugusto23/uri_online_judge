"""
Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

Entrada
O arquivo de entrada contém um valor inteiro.

Saída
Imprima a saída conforme exemplo fornecido.

Exemplo de Entrada:
400
800
30	

Exemplo de Saída:
1 ano(s)
1 mes(es)
5 dia(s)

2 ano(s)
2 mes(es)
10 dia(s)

0 ano(s)
1 mes(es)
0 dia(s)

"""
## Code: ##

total_dias = int (input(''))

idade_em_ano=total_dias/365 # 400/365 = 1.095890410958904
total_dias=total_dias%365 # 400%365 = 35
idade_em_meses=total_dias/30 # 35/30 = 1.1666666666666667
total_dias=total_dias%30 # 35%30 = 5
idade_em_dias=total_dias

print(int(idade_em_ano),'ano(s)')
print(int(idade_em_meses),'mes(es)')
print(int(idade_em_dias),'dia(s)')