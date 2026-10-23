num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    cont = int(input('Digite um número entre 0 e 20: '))
    
    if cont >= 0 and cont <= 20:
        print(f'Você digitou o número {num[cont]}')
        break
    else:
        print('Tente novamente. Digite um número entre 0 e 20')
        