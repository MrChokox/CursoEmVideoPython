from time import sleep
print('Você está solicitando um emprestimo')
print('Aguarde enquanto o banco entra em contato....')
sleep(3)
valor = float(input('Qual o valor do imovel?'))
salario = float(input('Qual o seu salário?'))
anos = int(input('Em quantos anos pretende pagar?'))
print('Obrigado pelos dados, aguarde alguns segundos.....')
sleep(3)
anos2 = anos * 12
preço = valor/anos2
p = (salario * 30)/100

if preço > p:
    print('O emprestimo foi negado pois a prestação excedeu 30% do seu salario')
else:
    print(f'O emprestimo foi aprovado, você vai pagar R${preço:.2f} por {anos}anos')
