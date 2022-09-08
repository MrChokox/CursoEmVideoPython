from datetime import date
print('SISTEMA DE TEMPO PARA ALISTAMENTO MILITAR')

print('''Qual seu sexo?
[ 1 ] Masculino
[ 2 ] Feminino ''')

sexo = int(input('Sua opção 1 ou 2: '))

if sexo == 2:
    print('Você não é obrigada a se alitar')
elif sexo == 1:
    ano = int(input('Em qual ano você nasceu:'))
    atual = date.today().year
    idade = atual - ano
    print(f'Quem nasceu em {ano} tem {idade} anos em {atual}')
    if idade > 18:
        print(f'Já passou do tempo de se alistar, você devia ter se alistado a {idade - 18} anos')
    elif idade < 18:
        print(f'Você vai ter que se alistar daqui a {(18 - idade)} anos')
    else:
        print('Você tem que se alistar esse ano')
else:
    print('Você digitou alguma coisa errada. Tente novamente')



