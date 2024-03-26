def calcular_valor_a_pagar(peso_do_prato):
    valor_por_quilo = 40.00
    valor_a_pagar = peso_do_prato * valor_por_quilo
    return valor_a_pagar

def main():
    # Solicita ao usuário a entrada do peso do prato em quilos
    peso_do_prato = float(input("Digite o peso do prato em quilos: "))

    # Chama a função para calcular o valor a ser pago
    valor_a_pagar = calcular_valor_a_pagar(peso_do_prato)

    # Exibe o resultado na tela
    print(f"O valor a ser pago pelo prato é: R$ {valor_a_pagar:.2f}")

# Chama a função principal
if __name__ == "__main__":
    main()
