sexo = input("Digite o sexo [M/F]: ").strip().upper()[0]
while sexo not in 'MF':
    sexo = input("Opção inválida! Por favor, digite usando M ou F: ").strip().upper()[0]
print(f'Obrigado, sexo {sexo} resgistrado com sucesso.')
