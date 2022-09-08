distancia = float(input('Qual a distancia da sua viagem em Km:'))
if distancia > 200:
    preço = distancia * 0.45
    print(f'O valor para sua viagem é de R${preço:.2f}')
else:
    preço = distancia * 0.50
    print(f'O valor de sua viagem vai ser de R${preço:.2f}')
