n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))

while True:
    print('\n======MENU======')
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] maior')
    print('[4] Novos números')
    print('[5] Sair')
    opcao = int(input('Selecione uma opção: '))

    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é igual a {soma}')
    elif opcao == 2:
        multi = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} é igual a {multi}')
    elif opcao == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2} o maior número é {n1}')
        elif n1 < n2:
            print(f'Entre {n1} e {n2} o maior número é {n2}')
        else:
            print(f'Entre {n1} e {n2} os dois números são iguais')
    elif opcao == 4:
        print('\nInforme novos valores:')
        n1 = int(input('Insira um número: '))
        n2 = int(input('Insira outro número: '))
    elif opcao == 5:
        print('finalizando o programa... Até logo!')
        break
    else:
        print('Opção inválida! Tente novamente.')
print('-' * 20)

