from datetime import date



for pess in range(1,8):
    ano = int(input(f'Qual o ano de nascimento da {pess}ª pessoa:'))
    idade = date.today().year - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1

print(f'{maior} pessoas ja são maior de idade e {menor} são de menor')
    