viagem = float(input('Qual a distância da viagem: '))

print(f'Você está prestes a começar uma viagem de {viagem}km.')
if viagem <= 200:
    print(f'A viagem custará: R${viagem * 0.50:.2f}')
else:
    print(f'A viagem custará: R${viagem * 0.45:.2f}')
