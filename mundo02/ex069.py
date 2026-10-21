maioridade = homem = mulhersub20 = 0

while True:
    print('-' * 20)
    print('CADRASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

    if idade >= 18:
        maioridade = maioridade + 1
    if sexo == 'M':
        homem = homem + 1
    if sexo == 'F' and idade < 20:
        mulhersub20 = mulhersub20 + 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        
    if continuar == 'N':
        break

print(f'\nTotal de pessoas com mais de 18 anos: {maioridade}')
print(f'Ao todo temos {homem} homem(ns) cadastrados')
print(f'E temos {mulhersub20} mulher(es) com menos de 20 anos')
