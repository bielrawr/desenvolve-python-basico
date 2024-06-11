n1, n2, n3 = int(input("Insira a primeira nota: ")), int(input("Insira a segunda nota: ")), int(input("Insira a terceira nota: "))

media = (n1 + n2 + n3) / 3
while media>60:
    print("Aprovado")
    print("Fim")
    exit()
while media>40:
    print("Recuperação")
    print("Fim")
    exit()
print("Reprovado")
print("Fim")