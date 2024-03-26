def celsius_para_fahrenheit(temp_celsius):
    # Fórmula de conversão de Celsius para Fahrenheit: (C * 9/5) + 32
    temp_fahrenheit = (temp_celsius * 9/5) + 32
    return temp_fahrenheit

def main():
    # Solicita ao usuário a entrada da temperatura em Celsius
    temp_celsius = float(input("Digite a temperatura em Celsius: "))

    # Chama a função para converter a temperatura para Fahrenheit
    temp_fahrenheit = celsius_para_fahrenheit(temp_celsius)

    # Exibe o resultado na tela
    print(f"A temperatura em Fahrenheit é: {temp_fahrenheit:.2f} °F")

# Chama a função principal
if __name__ == "__main__":
    main()
