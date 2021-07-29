"""

Leia quatro números (N1, N2, N3, N4), cada um deles com uma casa decimal, correspondente às quatro notas de um aluno. Calcule a média com pesos 2, 3, 4 e 1, respectivamente, para cada uma destas notas e mostre esta média acompanhada pela mensagem "Media: ". Se esta média for maior ou igual a 7.0, imprima a mensagem "Aluno aprovado.". Se a média calculada for inferior a 5.0, imprima a mensagem "Aluno reprovado.". Se a média calculada for um valor entre 5.0 e 6.9, inclusive estas, o programa deve imprimir a mensagem "Aluno em exame.".

No caso do aluno estar em exame, leia um valor correspondente à nota do exame obtida pelo aluno. Imprima então a mensagem "Nota do exame: " acompanhada pela nota digitada. Recalcule a média (some a pontuação do exame com a média anteriormente calculada e divida por 2). e imprima a mensagem "Aluno aprovado." (caso a média final seja 5.0 ou mais ) ou "Aluno reprovado.", (caso a média tenha ficado 4.9 ou menos). Para estes dois casos (aprovado ou reprovado após ter pego exame) apresente na última linha uma mensagem "Media final: " seguido da média final para esse aluno.

Entrada
A entrada contém quatro números de ponto flutuante correspendentes as notas dos alunos.

Saída
Todas as respostas devem ser apresentadas com uma casa decimal. As mensagens devem ser impressas conforme a descrição do problema. Não esqueça de imprimir o enter após o final de cada linha, caso contrário obterá "Presentation Error".

Exemplo de Entrada:	

2.0 4.0 7.5 8.0
6.4

2.0 6.5 4.0 9.0

9.0 4.0 8.5 9.0

Exemplo de Saída:

Media: 5.4
Aluno em exame.
Nota do exame: 6.4
Aluno aprovado.
Media final: 5.9

Media: 4.8
Aluno reprovado.

Media: 7.3
Aluno aprovado.

"""
## Code: ##


n1, n2, n3, n4 = map(float, input().split())

p1 = 2 
p2 = 3 
p3 = 4 
p4 = 1
pesos = p1+p2+p3+p4
notas = (n1 * p1)+(n2 * p2)+(n3 * p3)+(n4 * p4)
media = notas/pesos

if media >= 7:
    print(f"Media: {media:.1f}")
    print(f"Aluno aprovado.")

elif media >= 5 and media <= 6.9:
    nota_exame = float(input())
    nova_media = (media + nota_exame) / 2
    if nova_media >= 5: 
        print(f"Media: {media:.1f}")
        print(f"Aluno em exame.")
        print(f"Nota do exame: {nota_exame:.1f}")
        print(f"Aluno aprovado.")
        print(f"Media final: {nova_media:.1f}")
    elif nova_media <= 4.9: 
        print(f"Media: {media:.1f}")
        print(f"Aluno em exame.")
        print(f"Nota do exame: {nota_exame:.1f}")
        print(f"Aluno reprovado.")
        print(f"Media final: {nova_media:.1f}")
     
elif media < 5:
    print(f"Media: {media:.1f}")
    print(f"Aluno reprovado.")

#####################################################################

def media():
    notas = list(map(float, input().split()))
    pesos = [2, 3, 4, 1]
    somatoria_notas =  [ notas[item] * pesos[item] for item in range(len(notas)) ]
    media = sum(somatoria_notas)/sum(pesos)


    if media >= 7:
        print(f"Media: {media:.1f}")
        print(f"Aluno aprovado.")

    elif media >= 5 and media <= 6.9:
        nota_exame = float(input())
        nova_media = (media + nota_exame) / 2
        if nova_media >= 5: 
            print(f"Media: {media:.1f}")
            print(f"Aluno em exame.")
            print(f"Nota do exame: {nota_exame:.1f}")
            print(f"Aluno aprovado.")
            print(f"Media final: {nova_media:.1f}")
        elif nova_media <= 4.9: 
            print(f"Media: {media:.1f}")
            print(f"Aluno em exame.")
            print(f"Nota do exame: {nota_exame:.1f}")
            print(f"Aluno reprovado.")
            print(f"Media final: {nova_media:.1f}")
        
    elif media < 5:
        print(f"Media: {media:.1f}")
        print(f"Aluno reprovado.")

media()