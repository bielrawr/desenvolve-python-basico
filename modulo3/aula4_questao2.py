# 2) Você está criando um sistema de classificação de filmes com base nas avaliações dos usuários. 
# Escreva um programa em Python que solicita ao usuário para inserir a avaliação de um filme em uma escala de 1 a 5. 
# O programa deve imprimir uma mensagem correspondente à classificação do filme:
# Se a avaliação for 5, imprima "Excelente!"
# Se a avaliação for 4, imprima "Muito Bom!"
# Se a avaliação for 3, imprima "Bom!"
# Se a avaliação for 2, imprima "Regular."
# Se a avaliação for 1, imprima "Ruim."

avaliação = int(input("Insira a nota de avaliação do filme numa escala de 1 a 5, sendo 5 (excelente), 4 (muito bom), 3 (bom), 2 (regular) e 1 (ruim): "))
if avaliação == 5:
    print("Excelente!")
elif avaliação == 4:
    print("Muito bom!")
elif avaliação == 3:
    print("Bom!")
elif avaliação == 2:
    print("Regular.")
elif avaliação == 1:
    print("Ruim.")