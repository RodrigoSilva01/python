from random import shuffle

aluno1 = input('Insira o nome do aluno 1: ')
aluno2 = input('Insira o nome do aluno 2: ')
aluno3 = input('Insira o nome do aluno 3: ')
lista = [aluno1, aluno2, aluno3]
shuffle(lista)

print(f'A ordem será:')
print(lista)



