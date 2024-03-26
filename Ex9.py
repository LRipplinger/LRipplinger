def calcular_desconto(valor_compra):
    desconto = valor_compra * 0.15  # 15% do valor da compra
    valor_com_desconto = valor_compra - desconto
    return valor_com_desconto

def main():
    # Solicita ao usuário o valor da compra
    valor_compra = float(input("Digite o valor da compra: R$ "))

    # Calcula o valor da compra com desconto
    valor_com_desconto = calcular_desconto(valor_compra)

    # Exibe o resultado na tela
    print(f"O valor da compra com desconto de 15% é: R$ {valor_com_desconto:.2f}")

# Chama a função principal
if __name__ == "__main__":
    main()
