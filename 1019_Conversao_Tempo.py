"""
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.

Exemplo de Entrada:
556
1
140153

Exemplo de Saída:
0:9:16
0:0:1
38:55:53

"""
## Code: ##

a = int(input())
h = int(a/3600) # 556/3600 = 0,15444 1 hora -> 60*60=3600
m = int(a%3600/60) # 556%3600/60 = 9,2666 
s = int(a%60) # 556%60 = 16

print(f"{h}:{m}:{s}")
print("{}:{}:{}".format(h,m,s))
print("%d:%d:%d"%(h,m,s))