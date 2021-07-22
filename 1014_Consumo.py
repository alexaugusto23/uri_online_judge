"""
Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) e o total de combustível gasto (em litros).

Entrada
O arquivo de entrada contém dois valores: um valor inteiro X representando a distância total percorrida (em Km), e um valor real Y representando o total de combustível gasto, com um dígito após o ponto decimal.

Saída
Apresente o valor que representa o consumo médio do automóvel com 3 casas após a vírgula, seguido da mensagem "km/l".

Exemplo de Entrada:	
500
35.0

2254
124.4

4554
464.6

Exemplo de Saída:

14.286 km/l
18.119 km/l
9.802 km/l

"""
## Code: ##

x, y = int(input()), float(input())
consumo_medio = x/y
print(f"{consumo_medio:.3f} km/l")