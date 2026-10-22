tot_salario = cont = sup5k = 0
maior_idade = menor_idade = 0
mais_velho = mais_novo = ' '

print('-' * 50)
print(f'{'SISTEMA DE GESTÃO DE PESSOAL':^50}')
print('-' * 50)
while True:
    nome = str(input('Insira o nome do funcionário: ')).strip()
    idade = int(input('Insira a idade do funcionário: '))
    salario = float(input('Insira o salário do funcionário: R$'))

    tot_salario = tot_salario + salario
    cont = cont + 1

    if salario > 5000:
        sup5k = sup5k + 1

    if cont == 1 or idade > maior_idade:
        maior_idade = idade
        mais_velho = nome
    if cont == 1 or idade < menor_idade:
        menor_idade = idade
        mais_novo = nome

    resp = ' '
    while resp not in 'SN':
        resp = str(input('\nQuer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

if cont > 0:
    media = tot_salario / cont
    print('-' * 60)
    print(f'o salário total de todos os funcionários é de: R${tot_salario:.2f}')
    print(f'A média salarial da emprensa é de: R${media:.2f}')
    print(f'Existem {sup5k} funcionários que ganham mais que R$5000.00')
    print(f'O funcionário(a) mais velho é {mais_velho} com {maior_idade} anos')
    print(f'O funcionario(a) mais novo é {mais_novo} com {menor_idade} anos')
    print('-' * 60)
else:
    print('Nenhum funcionário foi cadastrado.')
