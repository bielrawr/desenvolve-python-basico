# 4) Você está implementando um sistema de entrega expressa e precisa calcular o valor do frete com base na distância e no peso do pacote. 
# Escreva um código que solicita a distância da entrega em quilômetros e o peso do pacote em quilogramas. 
# O programa deve calcular e imprimir o valor do frete de acordo com as seguintes regras:
# Distância até 100 km: R$1 por kg.
# Distância entre 101 e 300 km: R$1.50 por kg.
# Distância acima de 300 km: R$2 por kg.
# Acrescente uma taxa de R$10 para pacotes com peso superior a 10 kg


# Entrada de dados
distancia = int(input("Qual a distância em km até o endereço de entrega: "))
# Entrada de dados
peso = float(input("Qual o peso do pacote em quilogramas?: "))
# Processamento
frete = peso
# Processamento
if distancia <= 100:
    # Processamento
    if peso >10:
        # Processamento
        frete = peso + 10
        # Saída e impressão
    print(f"R${frete:.2f}")
# Processamento
elif distancia > 100 and distancia <= 300:
    # Processamento
    if peso >10:
        # Processamento
        frete = float(frete)
        # Processamento
        frete = peso * 1.5 + 10
        # Saída e impressão
        print(f"R${frete:.2f}") 
        # Encerra a execução do script
        exit()
    # Processamento
    frete = float(frete)
    # Processamento
    frete = peso * 1.5
    # Processamento
    print(f"R${frete:.2f}")
# Processamento
elif distancia >= 300:
    # Processamento
    if peso >10:
        # Processamento
        frete = float(frete)
        # Processamento
        frete = peso * 2.0 + 10
        # Saída e impressão
        print(f"R${frete:.2f}") 
        # Encerra a execução do script
        exit()
    # Processamento
    frete = peso * 2
    # Saída e impressão
    print(f"R${frete:.2f}")