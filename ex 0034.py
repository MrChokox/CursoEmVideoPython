salario = float(input('Qual o salario do funcionario, R$'))
if salario > 1250:
   aumento = (salario * 10) / 100
   print(f'Voce ira receber um aumento de R${aumento:.2f}')
if salario <= 1250:
    aumento = (salario * 15) / 100
    print(f'O seu salario de R${salario:.2f} vai ter um aumento de R${aumento:.2f}')




