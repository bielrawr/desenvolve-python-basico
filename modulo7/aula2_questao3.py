def eh_palindromo(frase):
    # Remove espaços e pontuações, e converte para minúsculas
    frase_limpa = ''.join(c.lower() for c in frase if c.isalnum())
    # Verifica se a frase limpa é igual à sua inversa
    return frase_limpa == frase_limpa[::-1]

while True:
    frase = input('Digite uma frase (digite "fim" para encerrar): ')
    if frase.lower() == 'fim':
        break
    if eh_palindromo(frase):
        print(f'"{frase}" é palíndromo')
    else:
        print(f'"{frase}" não é palíndromo')