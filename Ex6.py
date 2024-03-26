def calcular_arrecadacao(smartphones_vendidos, tablets_vendidos):
    preco_smartphone = 1000.00
    preco_tablet = 1500.00

    # Calcula o total arrecadado com a venda de smartphones e tablets
    total_smartphones = smartphones_vendidos * preco_smartphone
    total_tablets = tablets_vendidos * preco_tablet
    total_arrecadado = total_smartphones + total_tablets

    return total_arrecadado

def main():
    # Solicita ao usuário a entrada do número de smartphones e tablets vendidos
    smartphones_vendidos = int(input("Digite o número de smartphones vendidos: "))
    tablets_vendidos = int(input("Digite o número de tablets vendidos: "))

    # Chama a função para calcular o total arrecadado
    total_arrecadado = calcular_arrecadacao(smartphones_vendidos, tablets_vendidos)

    # Exibe o resultado na tela
    print(f"O total arrecadado com a venda de smartphones e tablets é: R$ {total_arrecadado:.2f}")

# Chama a função principal
if __name__ == "__main__":
    main()
