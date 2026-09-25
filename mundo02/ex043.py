peso = float(input('Insira seu peso em kg: '))
altura = float(input('Insira sua altura em metros: '))
imc = round(peso / (altura * altura),2)

if imc < 18.5:
    print(f'Seu imc é de {imc}, está abaixo do peso!')
elif 18.5 < imc <= 25:
    print(f'Seu imc é de {imc}, está com o peso ideal!')
elif 25 < imc <= 30:
    print(f'Seu imc é de {imc}, está com sobrepeso!')
elif 30 < imc <= 40:
    print(f'Seu imc é de {imc}, está com obesidade!')
else:
    print(f'Seu imc é de {imc}, está com obesidade mórbida!')
