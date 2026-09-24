from datetime import date

ano_nasc = int(input('Insira seu ano de nascimento: '))
idade = date.today().year - ano_nasc

if idade < 18:
    tempo_falta = 18 - idade
    print(f'Sua idade é de {idade} anos, ainda falta {tempo_falta} ano(s) para seu alistamento no exército!')
elif idade == 18:
    print(f'Sua idade é de {idade} anos, está na hora de alistar no exército brasileiro!')
else:
    tempo_passou = idade - 18
    print(f'Sua idade é de {idade} anos, você está atrasado em {tempo_passou} ano(s) para seu alistamento no exército!')
