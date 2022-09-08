num1 = int(input('Digite um valor:'))
num2 = int(input('Digite outro valor:'))

if num1 > num2:
    print(f'O número {num1} é maior que {num2}')
elif num1 < num2:
    print(f'O número {num2} é maior que {num1}')
else:
    print(f'Ambos os valores {num1} e {num2} são iguais')
