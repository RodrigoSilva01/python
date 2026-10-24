palavras = ('estudar', 'programar', 'curso', 'rodrigo', 'misterio', 'viagem', 'problemas', 'inconstitucional', 'admirar', 'corrida', 'carro', 'mulheres')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
