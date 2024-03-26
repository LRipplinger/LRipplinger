def calcular_valor_compra(camisetas, calcas, cintos):
    preco_camiseta = 25.00
    preco_calca = 100.00
    preco_cinto = 40.00

    # Calcula o valor total da compra
    valor_total = (camisetas * preco_camiseta) + (calcas * preco_calca) + (cintos * preco_cinto)

    return valor_total

def aplicar_desconto(valor_total):
    desconto = valor_total * 0.10  # 10% de desconto sobre o total
    valor_com_desconto = valor_total - desconto
    return desconto, valor_com_desconto

def main():
    # Solicita ao usuário o número de camisetas, calças e cintos comprados
    camisetas = int(input("Digite o número de camisetas compradas: "))
    calcas = int(input("Digite o número de calças compradas: "))
    cintos = int(input("Digite o número de cintos comprados: "))

    # Calcula o valor total da compra
    valor_total = calcular_valor_compra(camisetas, calcas, cintos)

    # Aplica o desconto sobre o total da compra
    desconto, valor_com_desconto = aplicar_desconto(valor_total)

    # Exibe o valor do desconto e o valor da compra com desconto na tela
    print(f"O valor do desconto é: R$ {desconto:.2f}")
    print(f"O valor da compra com desconto é: R$ {valor_com_desconto:.2f}")

# Chama a função principal
if __name__ == "__main__":
    main()
