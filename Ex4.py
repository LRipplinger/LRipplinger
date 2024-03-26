def calcular_media_final(nota_grau_a, nota_grau_b):
    # O grau A vale 1/3 e o grau B vale 2/3 da média final
    media_final = (nota_grau_a * (1/3)) + (nota_grau_b * (2/3))
    return media_final

def main():
    # Solicita ao usuário a entrada das notas dos graus A e B
    nota_grau_a = float(input("Digite a nota do Grau A: "))
    nota_grau_b = float(input("Digite a nota do Grau B: "))

    # Chama a função para calcular a média final
    media_final = calcular_media_final(nota_grau_a, nota_grau_b)

    # Exibe o resultado na tela
    print(f"A média final do aluno é: {media_final:.2f}")

# Chama a função principal
if __name__ == "__main__":
    main()
