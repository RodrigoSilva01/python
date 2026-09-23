nome = str(input('Qual o seu nome? '))

if nome == 'Rodrigo':
    print('Que nome bonito!')
elif nome == 'eldenor':
    print('Que nome horrível!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil!')
else:
    print('Seu nome é bem normal!')
print(f'Tenha um bom dia, {nome}!')
