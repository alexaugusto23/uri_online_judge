"""
Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

Código Especificação     Preço
1      Cahorro Quente    R$ 4.00
2      X-Salada          R$ 4.50
3      C-Bacon           R$ 5.00
4      Torrada simples   R$ 2.00
5      Refrigerante      R$ 1.50

Entrada
O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

Saída
O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.

Exemplo de Entrada:	

3 2
4 3
2 3

Exemplo de Saída:

Total: R$ 10.00
Total: R$ 6.00
Total: R$ 13.50

"""
## Code: ##


def caixa_lachonete(lanche, quantidade):
    lanches_descricao = {1:"Cachorro quente", 
                         2:"X-Salada", 
                         3:"X-Bacon", 
                         4:"Torrada simples", 
                         5:"Refrigerante"}
                         
    lanches_valores = {1: 4.00, 
                       2: 4.50, 
                       3: 5.00, 
                       4: 2.00, 
                       5: 1.50}
    soma = 0
    try:
        soma += lanches_valores[lanche] * quantidade

        return f"Total: R$ {soma:.2f}"
        
    except ValueError:
        return "Lache não existe"

try: 
    lanche, quantidade = map(int, input().split())
    print(caixa_lachonete(lanche, quantidade))
except ValueError: print("Somente número inteiros")

##############################################################

def caixa_lachonete(lanche, quantidade):
    soma = 0
    if lanche == 1:
        soma += 4.00 * quantidade
        return f"Total: R$ {soma:.2f}"
    
    elif lanche == 2:
        soma += 4.50 * quantidade
        return f"Total: R$ {soma:.2f}"
    
    elif lanche == 3:
        soma += 5.00 * quantidade
        return f"Total: R$ {soma:.2f}"

    elif lanche == 4:
        soma += 2.00 * quantidade
        return f"Total: R$ {soma:.2f}"

    elif lanche == 5:
        soma += 1.50 * quantidade
        return f"Total: R$ {soma:.2f}"

    else: 
        return f"Código inexistente"                 
    
       
try: 
    lanche, quantidade = map(int, input().split())
    print(caixa_lachonete(lanche, quantidade))
except ValueError: print("Somente número inteiros")
