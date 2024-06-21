import random

numero = random.randint(0, 10)
while True:
    palpite = int(input("Adivinhe um número de 0 a 10: "))
    if palpite > numero:
        print("Muito alto! Tente novamente")
    elif palpite < numero:
        print("Muito baixo! Tente novamente")
    else:
        print("Você acertou! O número é", numero)
        break
        
