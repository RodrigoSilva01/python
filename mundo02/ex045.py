import random
from time import sleep

jogadas = ('pedra', 'papel', 'tesoura')

while True:
    print('-----NOVA RODADA-----')
    print('Decida sua jogada: ')
    print('[pedra]')
    print('[papel]')
    print('[tesoura]')
    print('[sair]')

    opcao = input('Sua opção: ').strip().lower()
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!!')

    if opcao == 'sair':
        print('Obrigado por jogar! Até a próxima.')
        break
    if opcao not in jogadas:
        print('Opção inválida! Tente novamente.')
        continue

    opcao_pc = random.choice(jogadas)

    if opcao == opcao_pc:
        print('Resultado: EMPATE!')
    elif (opcao == 'pedra' and opcao_pc == 'tesoura') or \
        (opcao == 'tesoura' and opcao_pc == 'papel') or \
        (opcao == 'papel' and opcao_pc == 'pedra'):
        print('Você GANHOU!')
    else:
        print('Você PERDEU!')
        
    print(f'Sua escolha foi {opcao}.')
    print(f'O computador escolheu {opcao_pc}.')
