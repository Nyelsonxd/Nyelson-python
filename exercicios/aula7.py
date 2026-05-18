lista_compras = []

while True:
    item = input("digite o nome do produto: ")
    lista_compras.append(item)
    pergunta = input("deseja add outro item, remover ou sair: ")
    if pergunta == "add":
        continue
    elif pergunta == "remover":
        lista_compras.remove()


