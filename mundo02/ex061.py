primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite o termo da PA: '))

termo = primeiro
contador = 1

print('Os 10 primeiros termos da PA são: ')
while contador <= 10:
    print(f'{termo}', end=' -> ')
    termo = termo + razao
    contador = contador + 1
    
print('FIM!')
