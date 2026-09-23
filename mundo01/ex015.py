km = float(input('Quantos km foram rodados com o carro: '))
days = float(input('Por quantos dias o carro foi alugado: '))
price = (km * 0.15) + (days * 60)

print('-'*50)
print(f'O carro foi alugado por {days} e percorreu {km}km.')
print(f'o valor do alugel ficou, portanto R${price}')
print('-'*50)
