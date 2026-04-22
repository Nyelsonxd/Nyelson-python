alunos = []   # pra armazenar
quantidade = int(input("qunatos alunos deseja cadastrar? ")) 

for i in range(quantidade):
    print(f"\ncadastro do aluno {i+1}") 

    nome = input(" nome: ")
    idade = int(input("idade: "))
    telefone = input("telefone: ")

    aluno = {
        "nome": nome,
        "idade": idade,
        "telefone": telefone # Dicionario
    }

    alunos.append(aluno) 

print("\nlista de alunos cadastrados: ")
for aluno in alunos:
    print("-" * 10)
    for chave, valor in aluno.items():
        print(f"{chave.capitalize()}: {valor}")

    