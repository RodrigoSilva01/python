soma = 0
maior = 0
nome_velho = ''
mulher_sub20 = 0

for c in range(1, 5):
    nome = str(input('Insira seu nome: ')).strip()
    idade = int(input('Insira sua idade: '))
    sexo = str(input('insira seu sexo [M/F]: ')).strip().lower()

    soma = soma + idade

    if c == 1:
        maior = idade
        nome_velho = nome
    else:
        if idade > maior:
            maior = idade
            nome_velho = nome

    if sexo == 'f' and idade < 20:
        mulher_sub20 = mulher_sub20 + 1

media = soma / 4

print(f'A média de idade do grupo é de {media:.1f} anos.')
print(f'O nome do individuo mais velho é {nome_velho} com idade de {maior} anos')
print(f'Ao todo temos {mulher_sub20} mulher(es) com menos de 20 anos')
