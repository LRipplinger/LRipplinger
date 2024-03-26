def calcular_total_em_reais(cotacao_dolar, quantidade_dolares):
    total_em_reais = cotacao_dolar * quantidade_dolares
    return total_em_reais

def main():
    # Solicita ao usuário a entrada da cotação do dólar e a quantidade de dólares
    cotacao_dolar = float(input("Digite a cotação do dólar para real: "))
    quantidade_dolares = float(input("Digite a quantidade de dólares que deseja comprar: "))

    # Chama a função para calcular o total em reais
    total_em_reais = calcular_total_em_reais(cotacao_dolar, quantidade_dolares)

    # Exibe o resultado na tela
    print(f"O valor total em reais que o turista precisará pagar é: R$ {total_em_reais:.2f}")

# Chama a função principal
if __name__ == "__main__":
    main()
