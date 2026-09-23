nome = str(input('Qual seu nome: ')).strip()

print(f'Seu nome em letras maisculas é: {nome.upper()}')
print(f'Seu nome com letras minusculas é: {nome.lower()}')
print(f'Seu nome tem um total de {len(nome) - nome.count(" ")} letras sem os espaços!')
print(f'O seu primeiro nome tem: {len(nome.split()[0])} letras!')
