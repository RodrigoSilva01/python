produtos = {'ps5': 4500, 'tv': 3000, 'iphone': 17000}

print('Escolha o item a comprar: ')
print('[ps5] R$4500')
print('[tv] R$3000')
print('[iphone] R$17000')

opcao = input('Sua opção: ').strip().lower()

if opcao in produtos:
    preco_produto = produtos[opcao]

    print('Escolha um método de pagamento: ')
    print('[1] A vista em dinheiro/cheque')
    print('[2] A vista no cartão')
    print('[3] Parcelar no cartão')

    opcao2 = (input('seu método de pagamento: ')).strip()

    if opcao2 == '1':
        valor_desconto = preco_produto * 0.90
        print(f'Seu método de pagamento escolhido foi dinheiro/cheque. \nIncluindo o desconto automático de 10%, o valor com desconto aplicado é de R${valor_desconto:.2f}')

    elif opcao2 == '2':
        valor_desconto = preco_produto * 0.95
        print(f'Seu método de pagamento escolhido foi a vista no cartão. \nIncluindo o desconto automático de 5%, o valor com com desconto aplicado é de R${valor_desconto:.2f}')

    elif opcao2 == '3':
        parcelas = int(input('Em quantas vezes deseja parcelar? '))
        if parcelas <= 2:
            valor_parcela = preco_produto / parcelas
            print(f'Seu método de pagamento escolhido foi parcelado no cartão em {parcelas}x SEM JUROS.')
            print(f'O valor das parcelas será de R${valor_parcela:.2f}')
            print(f'O valor total do produto será de R${preco_produto:.2f}')

        else: 
            preco_juros = preco_produto * 1.20
            valor_parcela = preco_juros / parcelas
            print(f'Seu método de pagamento escolhido foi parcelado no cartão em {parcelas}x COM 20% DE JUROS.')
            print(f'O valor das parcelas será de R${valor_parcela:.2f}')
            print(f'O valor total do produto será de R${preco_juros:.2f}')
