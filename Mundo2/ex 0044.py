produto = input('Qual produto você está comprando?')
preço = float(input('Qual o preço do produto?'))
pagamento = int(input('''Qual vai ser o meio de pagamento?'
[ 1 ] dinheiro
[ 2 ] Cartão
[ 3 ] Cheque
Opção: '''))

if pagamento == 1 or pagamento == 3:
    print(f'O preço passa a ser R${preço - (preço*10)/100:.2f} com um desconto de 10%')
elif pagamento == 2:
    parcela = int(input('''Em quantas vezes?
    [ 1 ] a vista
    [ 2 ] 2x
    [ 3 ] 3x ou mais
    opção: '''))
    if parcela == 1:
        print(f'O preço passa a ser R${preço - (preço*5)/100:.2f} com um desconto de 5%')
    elif parcela == 2:
        print(f'O valor continua R${preço:.2f} em duas vezes de R${preço/2:.2f}')
    elif parcela >= 3:
        print(f'O valor passa a ser R${preço + (preço * 20)/100} com juros de 20%')
else:
    print('Algo está errado')
