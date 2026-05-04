# calculadora







def somar(*args):
    valor = 0
    for n in args:
        valor += int(n)
    return valor 

def subtrair(*args):
    valor = 0
    for n in args:
        valor -= int(n)
    return valor 

def mutiplicar(*args):
    valor = 1
    for n in args:
        valor *= float(n)
    return valor

def dividir(*args):
    valor = 1
    for n in args:
        valor /= float(n)
    return valor


while True:
    realize_operaçao = input("qual operaçao deseja realizar?:  ")
    numeros = input("digite numeros:  ")
    if realize_operaçao == "somar":
        print(somar(*numeros.split(",")))

    if realize_operaçao == "subtrair":
       print("subtrair")

    if realize_operaçao == "mutiplicar":
        print("mutiplicar")

    if realize_operaçao == "dividir":  
        print("dividir")



    

