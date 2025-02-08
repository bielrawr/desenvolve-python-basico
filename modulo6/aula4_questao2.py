frase = input("Digite uma frase: ")
frase = frase.lower()

# Listas de vogais e consoantes
vogais = "aeiouAEIOU"
consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"


lista_vogais = sorted([char for char in frase if char in vogais])
lista_consoantes = [char for char in frase if char in consoantes]


print("Vogais:", lista_vogais)
print("Consoantes:", lista_consoantes)