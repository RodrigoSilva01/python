speed = float(input('Qual a velocidade atual do carro: '))

if speed > 80:
    multa = (speed - 80) * 7
    print('MULTADO! Você excedeu o limite de velociade permitido de 80km/h')
    print(f'Você deve pagar uma multa de R${multa:.2f}!')
print('Tenha um bom dia, diriga com segurança!')