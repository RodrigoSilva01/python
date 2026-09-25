casa = float(input('Valor da casa: '))
salario = float(input('Salário do comprador: '))
anos = int(input('Quantos anos de financiamento: '))
prestacao = casa / (anos * 12)
minimo = salario * 0.30

if prestacao <= minimo: 
    print(f'Seu emprestimo foi APROVADO, suas parcelas são de R${prestacao:.2f}.')
    print(f'Você tem disponivel R${minimo:.2f}. Estabelecemos um limite de 30% do salário, o qual você se enquadra.')
else:
    print(f'Seu emprestimo foi NEGADO, suas parcelas são de R${prestacao:.2f}.')
    print(f'Você tem disponivel R${minimo:.2f}. Estabelecemos um limite de 30% do salário, o qual você se enquadra.')
print(f'Seu salário é de R${salario:.2f}, o valor da casa é de R${casa:.2f}, e será pago em {anos} anos')
