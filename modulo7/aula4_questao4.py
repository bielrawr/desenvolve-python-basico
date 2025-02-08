import random

def escolhe_palavra(arquivo_palavras):
    with open(arquivo_palavras, 'r', encoding='utf-8') as file:
        palavras = file.read().splitlines()
    return random.choice(palavras)

def carrega_estagios(arquivo_estagios):
    with open(arquivo_estagios, 'r', encoding='utf-8') as file:
        estagios = file.read().split("\n\n")
    return estagios

def imprime_enforcado(erros, estagios):
    print(estagios[erros])

def jogo_da_forca():
    palavra = escolhe_palavra('gabarito_forca.txt')
    estagios = carrega_estagios('gabarito_enforcado.txt')

    letras_adivinhadas = set()
    palavra_oculta = ['_' for _ in palavra]
    tentativas_restantes = 6
    erros = 0

    print("Bem-vindo ao jogo da forca!")
    print("A palavra tem {} letras: {}".format(len(palavra), ' '.join(palavra_oculta)))

    while tentativas_restantes > 0 and ''.join(palavra_oculta) != palavra:
        letra = input("Digite uma letra: ").lower()

        if letra in letras_adivinhadas:
            print("Você já tentou essa letra. Tente outra.")
        elif letra in palavra:
            letras_adivinhadas.add(letra)
            for i, char in enumerate(palavra):
                if char == letra:
                    palavra_oculta[i] = letra
            print("Boa! A palavra agora é: {}".format(' '.join(palavra_oculta)))
        else:
            letras_adivinhadas.add(letra)
            erros += 1
            tentativas_restantes -= 1
            imprime_enforcado(erros, estagios)
            print("Errado! Você tem {} tentativas restantes.".format(tentativas_restantes))

    if ''.join(palavra_oculta) == palavra:
        print("Parabéns! Você adivinhou a palavra: {}".format(palavra))
    else:
        print("Que pena! Você foi enforcado. A palavra era: {}".format(palavra))

if __name__ == "__main__":
    jogo_da_forca()