soma = 0
quantidade = 0
num = int(input('Insira um valor (ou 0 para sair): '))

if num != 0:
    maior = num
    menor = num

    while num != 0:
        soma = soma + num
        quantidade = quantidade + 1

        if num > maior:
            maior = num
        if num < menor:
            menor = num

        num = num = int(input('Insira um valor (ou 0 para sair): '))

    media = soma / quantidade

    print('\n----RESULTADOS----')
    print(f'Média dos números: {media:.2f}')
    print(f'maior número digitado: {maior}')
    print(f'Menor número digitado: {menor}')
else:
    print('Nenhum número foi digitado.')
