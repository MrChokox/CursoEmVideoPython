a = int(input('Digite o primeiro valor:'))
b = int(input('Digite o segundo valor:'))
c = int(input('Digite o terceiro valor:'))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = c
if b > a and b > c:
    maior = b
if a > c and a > b:
    maior = a

print(f'Entre os valores{a, b, c}')
print(f'O maior número é {maior} e o menor número é {menor}')
