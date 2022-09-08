velocidade = float(input('Qual a velocidade do carro:'))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você deve pagar uma multa no valor de R${multa}')
else:
    print('Você não ultrapassou o limite de velocidade :) continue assim')

