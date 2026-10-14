primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

termo = primeiro
contador = 1
total = 0
mais_termos = 10

while mais_termos != 0:
    total = total + mais_termos
    while contador <= total:
        print(f'{termo} -> ', end='')
        termo = termo + razao
        contador = contador + 1
    print('PAUSA')
    mais_termos = int(input('Quantos termos você quer mostrar a mais? (digite 0 para encerrar): '))

print(f'O total de termos é de {total}')
print('FIM!')
