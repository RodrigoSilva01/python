resp = 'S'
soma = quantidade = media = maior = menor = 0

while resp in 'Ss':
    num = int(input('Insira um valor: '))
    soma = soma + num
    quantidade = quantidade + 1
    if quantidade == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num  
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    while resp not in 'SN':
        resp = str(input('Opção inválida. Tente novamente [S/N]: ')).upper().strip()[0]
media = soma / quantidade

print('\n----RESULTADOS----')
print(f'Média dos números: {media:.2f}')
print(f'maior número digitado: {maior}')
print(f'Menor número digitado: {menor}')
