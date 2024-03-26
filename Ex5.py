def calcular_litros_abastecidos(preco_gasolina, valor_disponivel):
    # Calcula quantos litros o motorista pode comprar
    litros_abastecidos = valor_disponivel / preco_gasolina
    return litros_abastecidos

def main():
    # Solicita ao usuário a entrada do preço do litro da gasolina e o valor disponível para abastecer
    preco_gasolina = float(input("Digite o preço do litro da gasolina: "))
    valor_disponivel = float(input("Digite o valor disponível para abastecer: "))

    # Chama a função para calcular os litros abastecidos
    litros_abastecidos = calcular_litros_abastecidos(preco_gasolina, valor_disponivel)

    # Exibe o resultado na tela
    print(f"O motorista conseguiu colocar {litros_abastecidos:.2f} litros no tanque.")

# Chama a função principal
if __name__ == "__main__":
    main()
