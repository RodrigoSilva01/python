nome = str(input('Digite seu nome: ')).lower().strip()
A = nome.count('a')
first = nome.find('a') + 1
last = nome.rfind('a') + 1

print(f'Existem {A} "a" no seu nome')
print(f'Aparece pela primeira e ultima vez respectivamente nas posições {first} e {last}')