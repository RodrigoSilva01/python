from random import randint
from time import sleep
jogos = []
lista = []
print('-=' * 15)
print(f'{'JOGO DA MEGA SENA':^30}')
print('-=' * 15)

quant = int(input('Quantos jogos você que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0 
    while True:
        num = randint(0, 60)
        if num not in lista:
            lista.append(num)
            cont = cont + 1
        if cont >= 6:
            break

    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot = tot + 1

print('-=' * 3, f'SORTEANDO {quant} JOGOS ', '-=' * 3)

for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)

print('-=' * 3, f' < BOA SORTE > ', '-=' * 3)
