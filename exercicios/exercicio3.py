PALAVRA_COMPLETA = "PARALELEPIPEDO"
PALAVRA_INCOMPLETA = "PAREALELE_PEDO"
SILABA_FALTANTE = "PI"

silabas_usadas = []

print(f" A palavra é:{PALAVRA_INCOMPLETA}")
while True:
    silaba_inserida = input("Qual a sílaba?" ).upper()

    if silaba_inserida == SILABA_FALTANTE:
        print("Você acertou a sílaba")
        break
    elif silaba_inserida in silabas_usadas:
        print("Essa silaba está incorreta e já foi tentada!")
    else:
        silabas_usadas.append(silaba_inserida)
        print(f"silaba incorreta:{silabas_usadas}")

