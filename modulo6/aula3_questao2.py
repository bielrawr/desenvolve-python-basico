# Lista de URLs
urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]

dominios = []

for url in urls:
    # Remove o prefixo "www." e o sufixo ".com"
    dominio = url[4:-4]
    dominios.append(dominio)

print("dominios:", dominios)