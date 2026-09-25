num = int(input('Insira um número inteiro: '))

print(12 * '-=-')
print('''Escolha uma das bases para conversão:
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
print(12 * "-=-")

opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'\nO número {num}, quando convertido para BINÁRIO é {num:b}') 
elif opcao == 2:
    print(f'\nO número {num}, quando convertido para OCTAL é {num:o}')
elif opcao == 3:
    print(f'\nO número {num}, quando convertido para HEXADECIMAL é {num:x}')
else:
    print(f'\nopção invalida. Tente novamente escolhendo 1, 2 ou 3.')
