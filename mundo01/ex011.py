B = float(input('Qual a largura da parede: '))
H = float(input('Qual a altura da parede: '))
A = B * H
T = A / 2

print(f'A parede tem dimensões de {B}x{H}. \nCom base nisso a área da parede é de {A}m².')
print(f'Se para cada litro de tinta sejam pintados 2m² então para pintar a parede usaremos {T}L de tinta.')