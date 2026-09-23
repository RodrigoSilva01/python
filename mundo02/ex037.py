num = int(input('Insira um número: '))

print(20 * '-=-')
print('Escolha a base para conversão: ')
print('[1] converter para BINÁRIO')
print('[2] converter para OCTAL')
print('[3] converter para HEXADECIMAL')
print(20 * "-=-")

opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'\nO número {num}, quando convertido para BINÁRIO é {num:b}')
elif opcao == 2:
    print(f'\nO número {num}, quando convertido para OCTAL é {num:o}')
elif opcao == 3:
    print(f'\nO número {num}, quando convertido para HEXADECIMAL é {num:x}')
else:
    print(f'\nopção invalida. Tente novamente escolhendo 1, 2 ou 3.')
