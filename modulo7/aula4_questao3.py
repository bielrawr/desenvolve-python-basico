import os
import re

# Nome do arquivo
filename = 'estomago.txt'

# Função para abrir o arquivo com diferentes codificações
def read_file_with_encoding(file_path, encodings=['utf-8', 'latin-1', 'cp1252']):
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                return file.readlines(), encoding
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError(f"Não foi possível decodificar o arquivo com as codificações fornecidas: {encodings}")

# Verificar se o arquivo existe no mesmo diretório do script
if not os.path.isfile(filename):
    print(f"Erro: Arquivo '{filename}' não encontrado no diretório atual.")
    print(f"Diretório atual: {os.getcwd()}")
else:
    try:
        lines, used_encoding = read_file_with_encoding(filename)
        print(f"Arquivo lido com a codificação: {used_encoding}")
        
        # Imprimir as primeiras 25 linhas
        print("Primeiras 25 linhas do arquivo:")
        for i in range(min(25, len(lines))):
            print(lines[i], end='')

        # Contar o número de linhas do arquivo
        num_linhas = len(lines)
        print(f"\n\nNúmero total de linhas no arquivo: {num_linhas}")

        # Encontrar a linha com o maior número de caracteres
        linha_mais_longa = max(lines, key=len)
        print(f"\nLinha com o maior número de caracteres: {linha_mais_longa.strip()}")
        print(f"Número de caracteres nessa linha: {len(linha_mais_longa.strip())}")

        # Contar menções aos nomes "Nonato" e "Íria" (considerando variações de maiúsculas e minúsculas)
        nonato_count = 0
        iria_count = 0

        nonato_pattern = re.compile(r'\bnonato\b', re.IGNORECASE)
        iria_pattern = re.compile(r'\bíria\b', re.IGNORECASE)

        for line in lines:
            nonato_count += len(nonato_pattern.findall(line))
            iria_count += len(iria_pattern.findall(line))

        print(f"\nNúmero de menções ao nome 'Nonato': {nonato_count}")
        print(f"Número de menções ao nome 'Íria': {iria_count}")
    except UnicodeDecodeError as e:
        print(e)