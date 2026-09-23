name = str(input('Insira seu nome: ')).strip()
first_name = name.split()[0]
last_name = name.split()[-1]

print('Seja muito bem vindo!')
print(f'Seu primeiro nome é: {first_name}')
print(f'Seu ultimo nome é: {last_name}')
