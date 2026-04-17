import os

lista_cadastro = {}
while True:
    os.system("cls")
    print(lista_cadastro)



    nome = input("digite um nome: ")
    idade = int(input("digite a idade: "))

    dicionario_base = {
        "nome": nome,
        "idade": idade,
    }

    if dicionario_base in lista_cadastro:
        print("pessoa já cadastrada!")
    else:
        lista_cadastro.append(dicionario_base)

    pergunta = input("Quer continuar a cadastrar? ")
    if pergunta not in ["Sim","sim","SIM","s","S","Yes","yes","Y","y"]:
        break

