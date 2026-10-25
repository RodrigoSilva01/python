lista = [3, 4, 7, 1, 9]
lista[3] = 8
lista.append(2)
lista.sort(reverse=True)
lista.insert(2, 2)
lista.remove(2)
print(lista)
print(f'Essa lista tem {len(lista)} elementos')
