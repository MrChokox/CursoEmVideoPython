soma = 0
cont = 0
for c in range(0,6):
    num = int(input('Digite um valor:'))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Voce informou {cont} números pares e a soma dele é {soma}')



