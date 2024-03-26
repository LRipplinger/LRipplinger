def calcular_racao_necessaria(num_passaros):
    # Cada pássaro consome 30 gramas de ração por dia
    consumo_por_passaro = 30  # gramas
    # Calcula a quantidade total de ração necessária
    total_racao = num_passaros * consumo_por_passaro
    return total_racao

def main():
    # Solicita ao usuário a entrada do número de pássaros
    num_passaros = int(input("Digite o número de pássaros que você possui: "))

    # Chama a função para calcular a quantidade total de ração necessária
    total_racao = calcular_racao_necessaria(num_passaros)

    # Exibe o resultado na tela
    print(f"A quantidade total de ração necessária por dia é: {total_racao} gramas")

# Chama a função principal
if __name__ == "__main__":
    main()
