# Lista de livros com suas informações
livros = [
    ["1984", "George Orwell", 1949, 328],
    ["To Kill a Mockingbird", "Harper Lee", 1960, 281],
    ["The Great Gatsby", "F. Scott Fitzgerald", 1925, 180],
    ["One Hundred Years of Solitude", "Gabriel Garcia Marquez", 1967, 417],
    ["Pride and Prejudice", "Jane Austen", 1813, 279],
    ["The Catcher in the Rye", "J.D. Salinger", 1951, 214],
    ["The Hobbit", "J.R.R. Tolkien", 1937, 310],
    ["Fahrenheit 451", "Ray Bradbury", 1953, 158],
    ["Jane Eyre", "Charlotte Bronte", 1847, 500],
    ["Animal Farm", "George Orwell", 1945, 112]
]

# Nome do arquivo CSV
nome_arquivo = 'meus_livros.csv'

# Abrir o arquivo para escrita
with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
    # Escrever os títulos das colunas
    arquivo.write("Título,Autor,Ano de publicação,Número de páginas\n")
    
    # Escrever as informações dos livros
    for livro in livros:
        arquivo.write(f"{livro[0]},{livro[1]},{livro[2]},{livro[3]}\n")

print(f"Arquivo {nome_arquivo} criado com sucesso.")