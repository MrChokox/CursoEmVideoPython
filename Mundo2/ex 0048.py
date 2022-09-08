soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c)
        cont = cont + 1
        soma = soma + c
print(f'A soma entre esses {cont} valores é {soma}')



