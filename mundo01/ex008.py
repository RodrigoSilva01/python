m = float(input('insira uma medida em metros: '))
mm = m * 1000
cm = m * 100
dm = m * 10
dam = m / 10
hm = m / 100
km = m / 1000

print(f'O valor de {m}m em outras unidades de medida é:\n {mm:.0f}mm\n {cm:.0f}cm\n {dm:.0f}dm\n {dam}dam\n {hm}hm\n {km}km\n')