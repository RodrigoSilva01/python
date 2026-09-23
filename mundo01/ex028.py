import random
from time import sleep

n_secret = random.randint(0, 5)
sorteio = int(input('Escolha um número de 0 a 5: '))

print('CALCULANDO...')
sleep(3)
if sorteio == n_secret:
    print('Parabéns você acertou o número secreto!!!')
else:
    print(f'Você não acertou, o número sorteado foi {n_secret} e você escolheu {sorteio}, tente de novo na próxima!')
