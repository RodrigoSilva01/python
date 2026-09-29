nome = input('Insira uma palavra: ')
invertido = ""

for letra in nome:
    invertido = letra + invertido
if nome == invertido:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
