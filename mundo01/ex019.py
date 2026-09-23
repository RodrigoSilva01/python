from random import choice

aluno1 = input('Insira o nome do aluno 1: ')
aluno2 = input('Insira o nome do aluno 2: ')
aluno3 = input('Insira o nome do aluno 3: ')
lista = [aluno1, aluno2, aluno3]

print(f'Dentres os alunos(as) {aluno1}, {aluno2} e {aluno3} \nO escolhido para limpar o quadro foi o(a): {choice(lista)}')