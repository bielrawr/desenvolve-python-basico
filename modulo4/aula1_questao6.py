n = int(input("Insira a quantidade de experimentos: "))
count = 0
soma_sapo, soma_rato, soma_coelho = 0, 0, 0
while count < n:
    quantia = int(input("Insira a quantidade de cobaias: "))
    tipo = (input("Insira o tipo de cobaia usada: "))
    if tipo == 'S':
        soma_sapo += quantia
    elif tipo == 'R':
        soma_rato += quantia
    elif tipo == 'C':
        soma_coelho += quantia
    count += 1
total_cobaias = soma_coelho + soma_rato + soma_sapo
porcentagem_sapos = (soma_sapo / total_cobaias) * 100 if total_cobaias > 0 else 0
porcentagem_ratos = (soma_rato / total_cobaias) * 100 if total_cobaias > 0 else 0
porcentagem_coelhos = (soma_coelho / total_cobaias) * 100 if total_cobaias > 0 else 0

print("Total de cobaias:", total_cobaias)
print("Total de sapos:", soma_sapo)
print("Total de ratos:", soma_rato)
print("Total de coelhos:", soma_coelho)
print(f"Percentual de sapos {porcentagem_sapos:.2f} %")
print(f"Percentual de ratos {porcentagem_ratos:.2f} %")
print(f"Percentual de coelhos {porcentagem_coelhos:.2f} %")