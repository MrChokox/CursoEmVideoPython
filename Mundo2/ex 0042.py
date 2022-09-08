valor1 = int(input('Digite o primeiro valor:'))
valor2 = int(input('Digite o segundo valor:'))
valor3 = int(input('Digite o terceiro valor:'))

if valor1 < valor2 + valor3 and valor2 < valor1 + valor3 and valor3 < valor1 + valor2:
    print('Você pode formar um triangulo')
    if valor1 == valor2 == valor3:
        print('Você vai formar um triangulo Equilátero')
    elif valor1 == valor2 or valor2 == valor3 or valor3 == valor1:
        print('Você vai formar um triangulo Isósceles')
    elif valor1 != valor2 != valor3 != valor1:
        print('Você vai formar um triangulo Escaleno')
else:
    print('Você não consegue formar um triangulo')

