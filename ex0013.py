salario = float(input('Qual o salario do funcionario ?'))
novo = salario + (salario * 15/100)
print('Um funcionario que ganhava R${:.2f}, com 15% de aumento passa a receber R${:.2f}'.format(salario, novo))
