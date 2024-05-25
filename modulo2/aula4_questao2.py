# 2) Leia um valor inteiro correspondente a uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
# Fórmula de conversão: C = (F - 32) * (5/9), sendo C o valor em graus Celsius e F o valor em Fahrenheit.
# Antes de imprimir, converta o valor em Celsius para inteiro. A mensagem deve estar formatada da seguinte maneira:
# 86 graus Fahrenheit são 30 graus Celsius.

# Solicitação de entrada de dados - Temperatura desejada à ser convertida - Entrada
f_degrees = int(input("Insira os graus desejados a serem convertidos para Celsius: "))

# Definição da variável e armazenamento de seu respectivo valor - Processamento
c_degrees = (f_degrees - 32) * 5 / 9

# Impressão da conversão final da temperatura - Saída
print(f"{f_degrees} graus Fahrenheit são {int(c_degrees)} graus Celsius.")