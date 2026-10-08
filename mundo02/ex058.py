from random import randint
pc = randint(0, 10)
print('Sou seu computador... Acabei de escolher um número entre 0 e 10.')
print('Consegue adivinhar qual foi?')
acertou = False
tentativas = 0

while not acertou:
    num = int(input('Qual é seu palpite? '))
    tentativas = tentativas + 1
    if num == pc:
        acertou = True
    else:
        if num < pc:
            print('Mais... Tente novamente.')
        else:
            print('Menos... Tente novamente.')
print(f'Você acertou, foram necessarias {tentativas} tentativas para acertar')
