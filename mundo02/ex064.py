num = cont = soma = 0 
num = int(input('Insira um número [999 para parar]: '))

while num != 999:
    cont = cont + 1
    soma = soma + num
    num = int(input('Insira um número [999 para parar]: '))
print(f'Foram feitas {cont} tentativas e a soma deles é de {soma}.')
