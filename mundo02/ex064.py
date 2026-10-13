num = 0
tentativas = 0
soma = 0

while num != 999:
    num = int(input('Insira um número: '))
    if num != 999:
        tentativas = tentativas + 1
        soma = soma + num
print(f'Foram feitas {tentativas} tentativas e a soma deles é de {soma}.')
