soma = 0
maiorhomem = 0
nome_velho = ''
totmulher20 = 0

for p in range(1, 5):
    nome = str(input('Insira seu nome: ')).strip()
    idade = int(input('Insira sua idade: '))
    sexo = str(input('insira seu sexo [M/F]: ')).strip().lower()

    soma = soma + idade
    if p == 1 and sexo in 'Mm':
        maiorhomem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maiorhomem:
        maiorhomem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 = totmulher20 + 1
media = soma / 4
print(f'A média de idade do grupo é de {media:.1f} anos.')
print(f'O nome do homem mais velho é {nome_velho} com idade de {maiorhomem} anos')
print(f'Ao todo temos {totmulher20} mulher(es) com menos de 20 anos')
