primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
decimo_termo = primeiro + (10 - 1) * razao

print('Os 10 primeiros termos são: ')

for c in range(primeiro, decimo_termo + razao, razao):
    print(f'{c}', end=' -> ')
print('FIM!')
