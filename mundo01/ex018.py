from math import radians, sin, cos, tan

grau = float(input('Digite o valor do ângulo: '))

print(f'O seno do ângulo é {sin(radians(grau)):.2f}')
print(f'O cosseno do ângulo é {cos(radians(grau)):.2f}')
print(f'A tangente do ângulo é {tan(radians(grau)):.2f}')
