
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
while True:

    try:
        hour = int(input("Que horas são? (0 ~ 23): "))

        if 0 <= hour <= 11:
            print("Bom dia")

        elif 12 <= hour <= 17:
            print("Boa tarde")

        elif 18 <= hour <= 23:
            print ("Boa noite")

        else: 
            print("Você não digitou uma hora válida")

    except ValueError:
        print("Digite um numero inteiro entre 0 e 23")
    except Exception:
        print("Ocorreu um erro inesperado!!")