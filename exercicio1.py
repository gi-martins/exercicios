nome = input("Digite seu nome:")
idade = input("Digite sua idade:")

if nome and idade: 
    print(f"Seu nome é {nome}")
    print(f"Sua idade é {idade}")
    print(f"Seu nome invertido é {nome [::-1]}")
    print(f"A primeira letra do seu nome é {nome [0]} ")
    print(f"A última letra do seu nome é {nome [-1]}")
    print(f"Seu nome tem {len(nome)} letras")

    if ' ' in nome:
        print("Seu nome contém espaços")

    else:
        print("Seu nome NÃO contém espaços")

else: 
    print("Informações inválidas - você deixou campos vazios")
