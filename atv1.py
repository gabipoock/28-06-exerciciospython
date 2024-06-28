#crie um programa que leia dois números e a operação desejada
#(=,-,*, /) e exiba o resultado.

print('Olá, bom dia! :)')
n1 = int(input('Por favor, digite um número: '))
n2 = int(input('Digite outro número: '))
adição = n1 + n2
subtração = n1 - n2
multiplicação = n1 * n2
divisão = (n1/n2)

print('O primeiro valor digitado foi {} e o segundo valor digitado foi {}, a adição desses valores é {}.'.format(n1, n2, adição))
print('A subração dos dois valores é {}.'.format(subtração))
print('A multiplicação dos dois valores é {}.'.format(multiplicação))
print('A divisão dos dois valores é {}.'.format(divisão))