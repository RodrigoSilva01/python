nota1 = float(input('Insira a nota do aluno: '))
nota2 = float(input('Insira a nota do aluno: '))
media = (nota1 + nota2) / 2

if media < 5.0:
    print(f'REPROVADO, sua média é {media}.')
elif 5.0 <= media <= 6.9:
    print(f'RECUPERAÇÃO, sua média é {media}.')
else: 
    media >= 7.0 
    print(f'APROVADO, sua média é {media}.')
