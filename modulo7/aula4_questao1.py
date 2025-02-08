import os

frase = input("Digite uma frase: ")
nome_arquivo = "frase.txt"

#diretório atual do script
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

#caminho completo do arquivo
caminho_completo = os.path.join(diretorio_atual, nome_arquivo)

# Salva a frase no arquivo
with open(caminho_completo, 'w', encoding='utf-8') as arquivo:
    arquivo.write(frase)

print(f"Frase salva em {caminho_completo}")