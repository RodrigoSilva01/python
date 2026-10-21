from random import randint
vitorias = 0

print('=-' * 30)
print(f'{'VAMOS JOGAR PAR OU ÍMPAR':^55}')
print('=-' * 30)

while True:
    jogador = int(input('Diga um valor: '))
    escolha = str(input('Par ou Ímpar? [P/I]: ')).strip().upper() 
    pc = randint(0, 10)
    soma = jogador + pc

    if soma % 2 == 0:
        resultado = 'P'
    else:
        resultado = 'I'
    print(f'Você jogou {jogador} e o computador {pc}. Total de {soma} deu ', end='')
    print(f'PAR' if resultado == 'P' else 'ÍMPAR')
    print('=-' * 30)

    if escolha == resultado:
        print('Você VENCEU!\nVamos jogar novamente... \n')
        vitorias = vitorias + 1
    else:
        print('Você PERDEU!')
        break

print('=-' * 30)
print(f'GAME OVER! Você teve {vitorias} vitórias consecutivas.')
