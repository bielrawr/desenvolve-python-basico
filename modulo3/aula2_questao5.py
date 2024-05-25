# 5) Solicite de um usuário seu gênero ("M" ou "F"), sua idade e seu tempo de serviço (em anos)
# e escreva uma expressão que imprima True se a pessoa já pode se aposentar, ou False caso contrário, de acordo com as seguintes regras:
# A: Para mulheres, ter mais de 60 anos. Para homens, 65.
# B: Ou ter trabalhado pelo menos 30 anos
# C: Ou ter 60 anos  e trabalhado pelo menos 25.

# Entrada de dados
g = input("Digite o seu gênero (feminino ou masculino): ")
# Entrada de dados
i = int(input("Digite sua idade: "))
# Entrada de dados
t = int(input("Digite o total de anos trabalhados: "))

# Processamento
a = (g == 'feminino' and i >= 60) or (g == "masculino" and i >= 65)
# Processamento
b = t >= 30
# Processamento
c = i >= 60 and t >= 25

# Processamento
pode_ap = a or b or c

# Saída e impressão
print("Pode aposentar:", pode_ap)

