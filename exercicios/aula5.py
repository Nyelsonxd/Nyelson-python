def e_par(num):
    if num == 0:
        return False
    return num % 2 == 0

numero = input("insira um numero: ")
numero_convertido = 0.0

try:
    numero_convertido = float(numero)
except ValueError as e:
    print(f"numero inserido invalido, {e} nao e um numero valido")
if e_par(numero_convertido):
    print("acesso permitido")
else:
    print(f"acesso negado, {numero_convertido}") 

