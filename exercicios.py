# 1 - Escreva um programa que leia o nome de um funcionário,
# seu número de horas trabalhadas, o valor que recebe por hora
# e calcula o salário desse funcionário.
# A seguir, mostre o nome e o salário do funcionário.
import random as rd
import random
nome = input('Qual o seu nome? ')
horas = int(input('Quantas horas você trabalhou? '))
valor = float(input('Quanto ganha por hora? '))
salario = (valor*horas)*22
print('Olá' + str(nome) + ' o valor do seu salario é de R$' + str(salario))

# 2 - crie uma função que receba uma lista de 20 valores aleatórios, retornar
# apenas o maior valor e printar em tela.
lista = []
numeros = 0

while numeros < 30:
    lista.append(random.randrange(1, 100))
    numeros += 1


def m_numero(lista):
    valormax = lista[0]
    for numeros in lista:
        if numeros > valormax:
            valormax = numeros
    return valormax
    
def mr_numero(lista):
        return max(lista, key=int)


print(f'Dentro da sua lista: {lista}')
print(f'O numero de maior valor é:{mr_numero(lista)}')

# 3 - crie uma lista com 10 números aleatórios,
# itere essa lista e printar em tela os
# valores que são ímpares e pares.

# exemplo de resultado em tela:

# Essa foi a lista gerada aleatóriamente:
# [37, 52, 73, 91, 49, 67, 19, 64, 58, 22]
# ímpares: [37, 73, 91, 49, 67, 19]
# pares: [52, 64, 58, 22]

import random as rd
pares = []
impares = []
lista = []
n = 0

while n<10:
    lista.append(rd.randint(0, 100))
    if lista[n]%2 == 0:
        pares.append(lista[n])
    else:
        impares.append(lista[n])
    n +=1

print('Essa foi a lista gerada aleatóriamente:'+ str(lista))
print('ímpares: '+str(impares))
print('pares: '+str(pares))

# 4 - Crie uma função python que cálcule uma função de 2º Grau

a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))
raiz = ''
delta = 0
x1 = 0
x2 = 0

print('Sua equação é: ' + str(a) + 'x² + ' + str(b) + 'x + ' + str(c) + ' = 0')
def baskara(a,b,c):
delta= ((b ** 2)-(4*a*c))
raiz = (delta ** 0.5) 
x1 = ((-b) + (raiz/(2*a)))
x2 = ((-b) - (raiz/(2*a)))

print('Suas raizes são: ' + str(x1) + ',' + str(x2))
}
print(baskara)

# 5 - Faça um programa que leia o raio de um círculo e faça duas
# funções: uma que calcule a área do círculo e outra que calcule
# o comprimento do círculo.

raio= int(input(" Digite o valor do raio: "))
area= 3.14*(raio*raio)
comprimento= int(2*3.14*raio)

print('O valor da área é: ' +str(area))
print('O valor da circuferência é: ' +str(comprimento))
