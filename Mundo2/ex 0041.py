idade = int(input('Qual o ano de nascimento ?'))
from datetime import date
idade_vdd = date.today().year - idade
print(f'Quem nasceu em {idade} tem {idade_vdd} anos está na classificação:')

if idade_vdd <= 9:
    print('Você está na categoria MIRIM')
elif idade_vdd <= 14:
    print('Você está na categoria INFANTIL')
elif idade_vdd <= 19:
    print('Você está na categoria JUNIOR')
elif idade_vdd <= 25:
    print('Você está na categoria SÊNIOR')
else:
    print('Você está na categoria MASTER')
