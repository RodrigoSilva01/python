v_casa = float(input('Insira o valor da casa: '))
salario = float(input('Insira o seu salario: '))
anos = int(input('insira em quantos anos será pago: '))
pres_mensal = v_casa / (anos * 12)
final = salario * 0.30

if final < pres_mensal:
    print(f'Seu emprestimo foi negado, estabelecemos um limite de 30% da renda, você tem disponível o valor de R${final:.2f}, o que inferior as parcelas de R${pres_mensal:.2f} da casa.')
else: 
    print(f'Seu emprestimo foi aprovado, suas parcelas são de R${pres_mensal:.2f}, o que é menor que o seu limite disponivel de R${final}, ficando dentro do nosso limite de 30% do salário')
print(f'Seu salário é de R${salario:.2f}, o valor da casa é de R${v_casa:.2f}, e será pago em {anos} anos')
