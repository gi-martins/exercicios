""" 
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

number = input("Digite um número inteiro: ")

if number.isdigit():

    resto = int(number) % 2

    if resto == 0:
        print(f"{number} é par")

    else:
        print(f"{number} é ímpar")

else:
    print("Não é um numero inteiro")
