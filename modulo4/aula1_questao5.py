respondentes = int(input("Insira a quantidade de respondentes: "))

soma = 0
cont = 0
while cont < respondentes:
    idade = int(input("Insira a idade do respondente: "))
    soma += idade
    cont += 1

print(f"A média das idades é {soma/respondentes:.0f}")
