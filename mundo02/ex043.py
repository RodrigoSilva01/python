peso = float(input('Insira seu peso em kg: '))
altura = float(input('Insira sua altura em metros: '))
imc = round(peso / (altura ** 2),2)
print(f'Seu IMC é de {imc:.1f}')

if imc < 18.5:
    print(f'Você está ABAIXO DO PESO normal!')
elif 18.5 <= imc < 25:
    print(f'Você está com o PESO ideal!')
elif 25 <= imc < 30:
    print(f'Você está com SOBREPESO!')
elif 30 <= imc < 40:
    print(f'Você está com OBESIDADE!')
else:
    print(f'Você está com OBESIDADE MÓRBIDA, cuidado!')
