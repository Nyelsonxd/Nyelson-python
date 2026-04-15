# string = texto
# int = numeros inteiros (1,2,3,4)
# float = numeros de ponto flutuante
# list = lista
# dict = tipo de dicionário
# tupla 
# sets = conjuntos
# datetime = data e hora
# bool = boleano (verdadeiro ou salvo)
'''
type() - serve para validar tipos, assim verificando se o tipo corresponde ao pedido do código
'''

# texto = 'aluno'
# numero = '1'
# print("essa é a variável texto: ", texto)
# print("essa variável é do tipo: ",type(texto))
# print(type(type(texto) == type(numero)))


ponto_flutuante = 2.5
inteiro = 5
complexo = 10 + 2j
# f-string é um texto que recebe variaveis em chaves
# print(f"a soma de {inteiro} mais {ponto_flutuante} é; {inteiro + ponto_flutuante}")
# while True:
#     recebido = input("digite um numero: ")
#     try:
#         recebido = int(recebido)
#     except ValueError:
#         try:        
#             recebido = float(recebido)
#         except ValueError:
#             pass

#     print(bool(recebido))
# if type(recebido) == int:
#     print("esse numero é inteiro")
# else:
#     print("esse numero não é inteiro")
dicionario = {
    'chave': 7,
    'chave2': "valor"
}    
lista = [1,2,3,4]

chave = dicionario['chave']
chave2 = dicionario['chave2']
# print(f"o valor da chave é {chave}")
# print(f"o valor da chave2 é {chave2}")
# print(dicionario.keys())
# print(dicionario.values())
print(dicionario)
dicionario["chave2"] = "Nyelson"
print(dicionario)