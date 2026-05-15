class Praca:
    def __init__(self, nome, quadra, iluminacao, localizacao):
        self.nome = nome
        self.quadra = quadra
        self.iluminacao = iluminacao
        self.localizacao = localizacao

    def usar_quadra(self: Praca, quadra: str) -> str:
        self.quadra = quadra
        if self.quadra == "aberta":
            return "Você pode usar a quadra para jogar."
        else:            
            return "A quadra não está disponível para uso."
        

    def __str__(self):
        return f"Praca(nome={self.nome}, quadra={self.quadra}, iluminacao={self.iluminacao}, localizacao={self.localizacao})"


praca1 = Praca("Praca do Sol", "Quadra de esportes", "adequada", "Centro da cidade")
print("Nome da praça:", praca1.nome)
print("Quadra:", praca1.quadra)
print("Iluminação:", praca1.iluminacao)
print("Localização:", praca1.localizacao)

print(praca1.usar_quadra("fechada"))