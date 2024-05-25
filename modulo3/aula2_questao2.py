# 2) Dando continuidade à questão anterior, um outro bar permite a entrada de grupos onde pelo menos
# uma pessoa é maior de idade (ficando responsável pelas outras). Ajuste sua resposta da questão anterior, 
# ainda solicitando as idades de Juliana e Cris, mas ajustando a expressão para esse novo cenário, imprimindo 
# True se puderem entrar no bar, e False caso contrário.

# Entrada de dados e processamento
idade_ju = int(input("Juliana, por favor, digite sua idade: "))
# Entrada de dados e processamento
idade_cris = int(input("Cris, por favor, digite sua idade: "))
# Saída     ###variável(ju) é maior ou igual a 18 ((OU)) variável(cris) é maior ou igual a 18 - se sim (True) senão (False)
print(idade_ju >=18 or idade_cris >= 18)
