primeiro = int(input('Digite o primeiro termo:'))
razão = int(input('Digite a razão:'))
décimo = primeiro + (10-1) * razão
for pa in range(primeiro, décimo + razão ,razão):
    print(pa, end=' -> ')
print('KBOU')