i = 0
cont = 0
maioridadehomem = 0
nomevelho = ''

for p in range(1,5):
    print(f'----- {p}ª Pessoa -----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    i += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

print('a média de idade do grupo é:', i/4,'anos')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}')



