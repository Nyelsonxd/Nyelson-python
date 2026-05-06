"""
Operadores:
    - São símbolos que realizam operações em variáveis e valores.
    - Exemplos de operadores:
        - Aritméticos: +, -, *, /, // (divisão inteira), % (módulo), ** (exponenciação)
        - Relacionais: (==, !=, >, <, >=, <=) -> Sempre vai retornar um valor booleano (True ou False)
        - Lógicos: and, or, not

"""
variavel_1 = int(input("digite o primeiro numero: "))
variavel_2 = int(input("digite o segundo numero: "))
variavel_3 = int(input("digite o terceiro numero: "))
variavel_4 = int(input("digite o quarto numero: "))

if variavel_1 == variavel_2 or variavel_3 < variavel_4:
    print ("variavel_1 é igual a variavel_2 ou a variavel_3 é menor que a variavel_4 ")
    input("Aperte enter pra continuar...\n")

if variavel_3 > variavel_1 and variavel_2 != variavel_4:
    print("variavel_3 é maior que a variavel_1 e variavel_2 é diferente que a variavel_4 ")
    input("Aperte enter pra continuar...\n")

if variavel_2 < variavel_4 and variavel_3 == variavel_1:
    print("variavel_2 é menor a variavel_4 e variavel_3 é igual a variavel_1")
    input("Aperte enter pra continuar...\n")

if variavel_4 < variavel_3 or variavel_2 >= variavel_1:
    print("variavel_4 é menor que a variavel_3 ou variavel_2 é maior igual que a variavel_1")
    input("Aperte enter pra continuar...\n")
