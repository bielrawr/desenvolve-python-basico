import os
import re

arquivo_frase = "frase.txt"
arquivo_palavras = "palavras.txt"

#diretório atual do script
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

#caminho completo dos arquivos
caminho_frase = os.path.join(diretorio_atual, arquivo_frase)
caminho_palavras = os.path.join(diretorio_atual, arquivo_palavras)

# Lê o conteúdo do arquivo "frase.txt"
with open(caminho_frase, 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()

# Remove todos os caracteres não alfabéticos e separa as palavras
palavras = re.findall(r'\b[a-zA-Z]+\b', conteudo)

# Salva as palavras no arquivo "palavras.txt", uma palavra por linha
with open(caminho_palavras, 'w', encoding='utf-8') as arquivo:
    for palavra in palavras:
        arquivo.write(palavra + '\n')

# Lê e imprime o conteúdo do arquivo "palavras.txt"
with open(caminho_palavras, 'r', encoding='utf-8') as arquivo:
    conteudo_palavras = arquivo.read()

print("Conteúdo do arquivo 'palavras.txt':")
print(conteudo_palavras)