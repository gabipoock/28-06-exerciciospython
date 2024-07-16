#Desenvolva um programa que leia três
#notas e seus respectivos pesos, calcule e mostre a média ponderada

print('Olá, boa noite! :)')
n1 = float(input('Por favor, digite uma nota: '))
n2 = float(input('Digite outra nota: '))
n3 = float(input('Digite a última nota: '))
media = (n1 + n2 + n3)/3

print('A média ponderada das 3 notas é {:.2f}.'.format( media))
